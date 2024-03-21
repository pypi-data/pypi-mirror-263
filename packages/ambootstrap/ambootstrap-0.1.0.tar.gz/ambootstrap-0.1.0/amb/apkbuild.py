import os.path
import re
import shlex

_RE_VAR = re.compile(r'([^=\s]+)=')
_RE_TEST_AND = re.compile(r"^\[([^\]]+)\]\s+&&\s+(.+)")
_RE_IF_TEST = re.compile(r"^if\s+\[(\s+[^\]]+)\];\s+then")
_RE_FUNCTION = re.compile(r"^\w+\(\)\s*{")
_RE_CASE = re.compile(r"^case\s+(.+)\s+in$")
_RE_CASE_BLOCK = re.compile(r"([^\)]+)\)(.+?);;", re.MULTILINE | re.DOTALL)
_RE_LOOP = re.compile(r"^for\s+([^\s]+)\s+in\s+([^;]+);\s+do")


class Apkbuild:
    _IS_ARRAY = {
        "source",
        "sha512sums",
        "options",
        "depends",
        "makedepends",
        "checkdepends",
        "subpackages",
        "license",
    }

    def __init__(self):
        self.metadata = {}
        self.data = {}
        self.cwd = '/'
        self.functions = {}

    def __getitem__(self, item):
        if item not in self.data:
            return None

        if item in self._IS_ARRAY:
            return self.data[item].split()

        return self.data[item]

    def __contains__(self, item):
        return self.data.__contains__(item)

    @classmethod
    def from_file(cls, path, state=None):
        if not os.path.isfile(path):
            raise ValueError()
        with open(path, 'r') as handle:
            raw = handle.read()
        return cls.from_string(raw, state, os.path.dirname(path))

    @classmethod
    def from_string(cls, raw, state=None, cwd=None):
        result = Apkbuild()
        result.cwd = cwd if cwd is not None else '/'

        if state is not None:
            result.data.update(state)

        in_quotes = False
        in_function = None
        in_if = False
        in_case = False
        in_loop = False
        case_input = None
        case_buffer = ""
        loop_buffer = ""
        buffer = None
        key = None
        loop_varying = None
        loop_data = None

        linebuffer = list(reversed(raw.splitlines()))
        while len(linebuffer):
            line = linebuffer.pop()

            # Save raw data when in a quoted block
            if in_quotes:
                buffer += f"\n{line}"
                if line.rstrip().endswith('"'):
                    in_quotes = False
                    result._define_variable(key, buffer)

            if in_function is not None:
                if line.rstrip() == "}":
                    in_function = None
                    continue
                result.functions[in_function] += line
                continue

            if in_if:
                if line == "fi":
                    in_if = False
                continue

            if in_case:
                if line == "esac":
                    in_case = False
                    case_contents = result._parse_case(case_input, case_buffer)
                    linebuffer.extend(reversed(case_contents))
                else:
                    case_buffer += line + "\n"
                continue

            if in_loop:
                if line == "done":
                    in_loop = False
                    unrolled = result._parse_loop(loop_varying, loop_data, loop_buffer)
                    linebuffer.extend(reversed(unrolled))
                else:
                    loop_buffer += line + "\n"
                continue

            line = line.strip()

            # Ignore empty lines
            if line == "":
                continue

            # Parse the comment lines at the top for metadata
            if line.startswith('#'):
                part = line.split(maxsplit=2)
                if len(part) > 2 and part[1][-1] == ':':
                    key = part[1][0:-1]
                    if key not in result.metadata:
                        result.metadata[key] = []
                    result.metadata[key].append(part[2])
                else:
                    continue

            # Try to figure out conditionals
            match = _RE_TEST_AND.match(line)
            if match:
                condition = match.group(1)
                action = match.group(2)
                if result._parse_condition(condition):
                    line = action

            match = _RE_IF_TEST.match(line)
            if match:
                condition = match.group(1)
                if not result._parse_condition(condition):
                    in_if = True
                continue

            # Detect functions to skip them
            match = _RE_FUNCTION.match(line)
            if match:
                in_function = match.group(1).strip()
                result.functions[in_function] = ""
                continue

            # Parse case..esac
            match = _RE_CASE.match(line)
            if match:
                case_input = result._parse_variable(match.group(1))
                case_buffer = ""
                in_case = True
                continue

            match = _RE_LOOP.match(line)
            if match:
                in_loop = True
                loop_varying = match.group(1)
                loop_data = match.group(2)
                loop_buffer = ""
                continue

            # Parse variables
            match = _RE_VAR.match(line)
            if match:
                key = match.group(1)
                _, val = line.split('=', maxsplit=1)
                if val.startswith('"'):
                    try:
                        shlex.split(val)
                        result._define_variable(key, val)
                    except ValueError:
                        in_quotes = True
                        buffer = val
                else:
                    result._define_variable(key, val)
                    continue

        return result

    def _define_variable(self, key, val):
        self.data[key] = self._parse_variable(val)

    def _parse_variable(self, val):
        quoted = False
        buffer = ''
        escape = False
        var = False
        index = 0
        while index != len(val):
            char = val[index]

            if index == 0 and val[index] == '"':
                quoted = True
                index += 1
                continue

            if char == '\\':
                escape = True
                index += 1
                continue

            if not escape and quoted and char == '"':
                index += 1
                quoted = False
                continue

            if not escape and not quoted and char == '#':
                break

            if not escape and not var and char == '$':
                index += 1
                parsed, index = self._parse_var(val, index)
                buffer += parsed
                continue
            buffer += char
            index += 1

        return buffer

    def _parse_var(self, val, index):
        braced = val[index] == '{'
        buffer = ''
        parameter = ''
        data = ''
        in_name = True

        special = '-+?=%#:/'
        vstype = None

        if braced:
            index += 1

        while index < len(val):
            if braced and val[index] == '}':
                index += 1
                break

            if not braced and val[index] in ' -+?=%#:/$"\n\t':
                break

            if in_name and val[index] in special:
                vstype = val[index]
                if vstype in "%#/" and val[index + 1] == vstype:
                    vstype += vstype
                    index += 1
                elif vstype == ':' and val[index + 1] in '-+?=':
                    vstype = val[index + 1]
                    index += 1
                in_name = False
                index += 1
                continue

            if in_name:
                if val[index] == '$':
                    index += 1
                    temp, index = self._parse_var(val, index)
                    parameter += temp
                else:
                    parameter += val[index]
                    index += 1
            else:
                if val[index] == '$':
                    index += 1
                    temp, index = self._parse_var(val, index)
                    data += temp
                else:
                    data += val[index]
                    index += 1

        if vstype is None or vstype == '?':
            # Basic variable substition, or ? because there's no runtime errors
            if parameter in self.data:
                buffer = self.data[parameter]
            else:
                buffer = ''
        elif vstype == '-':
            # Use data if parameter is unset
            if parameter in self.data:
                buffer = self.data[parameter]
            else:
                buffer = data
        elif vstype == '+':
            # Use data if parameter is set
            if parameter in self.data:
                buffer = data
            else:
                buffer = ''
        elif vstype == '=':
            # Set variable if it was not set to the data
            if parameter in self.data:
                buffer = self.data[parameter]
            else:
                self.data[parameter] = data
        elif vstype == '%':
            if parameter in self.data:
                buffer = self.data[parameter]
            regex = self._pattern_to_regex(data, greedy=False)
            buffer = re.sub(regex + r'$', '', buffer)
        elif vstype == '%%':
            if parameter in self.data:
                buffer = self.data[parameter]
            regex = self._pattern_to_regex(data, greedy=True)
            buffer = re.sub(regex + r'$', '', buffer)
        elif vstype == '#' and parameter != '':
            if parameter in self.data:
                buffer = self.data[parameter]
            regex = self._pattern_to_regex(data, greedy=False)
            buffer = re.sub(r'^' + regex, '', buffer)
        elif vstype == '##' and parameter != '':
            if parameter in self.data:
                buffer = self.data[parameter]
            regex = self._pattern_to_regex(data, greedy=True)
            buffer = re.sub(r'^' + regex, '', buffer)
        elif vstype == '#':
            # strlen
            if parameter in self.data:
                buffer = str(len(self.data[parameter]))
            else:
                # This is actually a runtime error
                buffer = '0'
        elif vstype == ':':
            # Substring
            if ':' in data:
                position, length = data.split(':', maxsplit=1)
            else:
                position = data
                length = None
            position = int(position) if len(position) > 0 else 0
            if parameter in self.data:
                if length is not None:
                    length = int(length)
                    buffer = self.data[parameter][position:position + length]
                else:
                    buffer = self.data[parameter][position:]
            else:
                buffer = ''
        elif vstype == '/' or vstype == '//':
            # Substring substitution
            maxreplace = 1 if vstype == '/' else -1
            if '/' in data:
                search, replace = data.split('/', maxsplit=1)
            else:
                search = data
                replace = ''
            if parameter in self.data:
                buffer = self.data[parameter].replace(search, replace, maxreplace)
            else:
                buffer = ''
        else:
            raise NotImplementedError(f"Unimplemented vstype '{vstype}'")

        return buffer, index

    def _pattern_to_regex(self, pattern, greedy=False):
        index = 0
        escape = False
        result = ''
        in_group = False
        greed = '' if greedy else '?'

        while index < len(pattern):
            char = pattern[index]

            if not escape and char == '\\':
                escape = True
                index += 1
                continue

            if not escape and char == '*':
                result += '.*' + greed
            elif not escape and char == '?':
                result += '.' + greed
            elif not escape and char == '{':
                result += '('
                in_group = True
            elif not escape and in_group and char == ',':
                result += '|'
            elif not escape and in_group and char == '}':
                in_group = False
                result += ')'
            elif not escape and char in '.()[]':
                result += '\\' + char
            else:
                result += char

            index += 1
        return result

    def _parse_condition(self, condition):
        part = shlex.split(condition)
        negate = False
        if part[0] == '!':
            negate = True
            part = part[1:]
        if len(part) == 3:
            a = self._parse_variable(part[0])
            b = self._parse_variable(part[2])
            op = part[1]

            if op == '==' or op == '=' or op == '-eq':
                return (a == b) ^ negate
            elif op == '!=' or op == '-ne':
                return (a != b) ^ negate
            elif op == '>=' or op == '-ge':
                return (float(a) >= float(b)) ^ negate
            elif op == '>' or op == '-gt':
                return (float(a) > float(b)) ^ negate
            elif op == '<=' or op == '-le':
                return (float(a) <= float(b)) ^ negate
            elif op == '<' or op == '-lt':
                return (float(a) < float(b)) ^ negate
            else:
                raise NotImplementedError(f"Unimplemented op '{op}' in {part}")
        elif len(part) == 2:
            op = part[0]
            a = self._parse_variable(part[1])
            if op == '-z':
                return (len(a) == 0) ^ negate
            elif op == '-n':
                return (len(a) > 0) ^ negate
            elif op == '-f':
                return os.path.isfile(os.path.join(self.cwd, a)) ^ negate
            else:
                raise NotImplementedError(f"Unimplemented op '{op}' in {part}")
        else:
            raise NotImplementedError(f"Unimplemented condition {part}")

    def _parse_case(self, data, block):
        for block in _RE_CASE_BLOCK.findall(block):
            pattern = self._pattern_to_regex(block[0].strip())
            if re.match(pattern, data):
                return block[1].splitlines()
        return []

    def _parse_loop(self, varying, data, buffer):
        result = []
        raw = self._parse_variable(data)
        for value in raw.strip().replace('\n', ' ').split():
            result.append(f'{varying}="{value}"')
            result.extend(buffer.splitlines())
        return result


if __name__ == '__main__':
    Apkbuild.from_file(os.path.join(os.path.dirname(__file__), '../fixtures/apkbuild/APKBUILD.lint'))
