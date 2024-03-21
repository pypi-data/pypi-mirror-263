import logging


class AmbLogFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    white = "\x1b[97;20m"
    blue = "\x1b[36;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = '[%(levelname)-8s] %(name)-8s - %(message)s'

    FORMATS = {
        logging.DEBUG: blue + format + reset,
        logging.INFO: white + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def init_logging(verbose=False, debug=False):
    ch = logging.StreamHandler()
    ch.setFormatter(AmbLogFormatter())
    if verbose:
        logging.basicConfig(level=logging.INFO, handlers=[ch])
    elif debug:
        logging.basicConfig(level=logging.DEBUG, handlers=[ch])
    else:
        logging.basicConfig(handlers=[ch])
