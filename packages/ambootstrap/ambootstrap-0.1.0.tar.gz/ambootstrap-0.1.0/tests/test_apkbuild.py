import os.path

import yaml

from amb.apkbuild import Apkbuild


def test_pattern_to_regex():
    cases = [
        ('a b c', 'a b c'),
        ('/path/*/awesome', '/path/.*/awesome'),
        ('file???.jpg', 'file...\\.jpg'),
        ('file.{jpg,png}', 'file\\.(jpg|png)'),
    ]

    impl = Apkbuild()
    for data, expected in cases:
        result = impl._pattern_to_regex(data, greedy=True)
        assert result == expected


def test_parse_conditional():
    cases = [
        ('"$CARCH" == "x86_64"', True),
        ('"$CARCH" == "aarch64"', False),
    ]

    impl = Apkbuild()
    impl.data['CARCH'] = "x86_64"

    for data, expected in cases:
        result = impl._parse_condition(data)
        assert result == expected


def test_apkbuild_parse():
    fixtures = os.path.join(os.path.dirname(__file__), '../fixtures/apkbuild')
    testfiles = [
        'APKBUILD.uboot',
        'APKBUILD.conditional-depends',
        'APKBUILD.lint',
        'APKBUILD.depends-in-depends',
        'APKBUILD.variable-replacements',
    ]

    for testfile in testfiles:
        result = Apkbuild.from_file(os.path.join(fixtures, testfile), {
            'CARCH': 'aarch64',
            'srcdir': '/home/build',
        })

        yamlfile = os.path.join(fixtures, testfile + ".yaml")
        with open(yamlfile, "r") as handle:
            reference = yaml.load(handle, yaml.Loader)

        # Verify the metadata
        for field in reference['metadata']:
            assert field in result.metadata
            assert len(reference['metadata'][field]) == len(result.metadata[field])
            for val in reference['metadata'][field]:
                assert val in result.metadata[field]

        # Check the variables
        for field in reference['data']:
            assert field in result
            assert result[field] == reference['data'][field]
