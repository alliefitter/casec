from pathlib import Path
from unittest import TestCase

from yaml import safe_load

from delim import CaseDelimitedParser, CharacterType, CharacterContainer, CharacterDelimitedParser
from delim.parser import ParserBase


class TestParser(TestCase):
    def test_camel_case(self):
        self._execute_tests(CaseDelimitedParser(CharacterType.UPPERCASE), 'camel_case')

    def test_camel_case_with_literals(self):
        parser = CaseDelimitedParser(CharacterType.UPPERCASE)
        parser.literals = ['iOS', 'iTunes', 'VPP', 'IDs']
        self._execute_tests(parser, 'camel_case_with_literals')

    def test_domain(self):
        parser = CharacterDelimitedParser(CharacterType.DOT)
        self._execute_tests(parser, 'domain')

    def test_constant_case(self):
        parser = CharacterDelimitedParser(CharacterType.UNDERSCORE)
        self._execute_tests(parser, 'constant_case')

    def test_csv(self):
        parser = CharacterDelimitedParser(CharacterType.COMMA)
        self._execute_tests(parser, 'csv')

    def test_kebab_case(self):
        parser = CharacterDelimitedParser(CharacterType.DASH)
        self._execute_tests(parser, 'kebab_case')

    def test_pascal_case(self):
        self._execute_tests(
            CaseDelimitedParser(CharacterType.UPPERCASE),
            'pascal_case'
        )

    def test_pascal_case_with_literals(self):
        parser = CaseDelimitedParser(CharacterType.UPPERCASE, ['iOS', 'iTunes', 'VPP', 'IDs'])
        self._execute_tests(parser, 'pascal_case_with_literals')

    def test_path(self):
        parser = CharacterDelimitedParser(CharacterType.SLASH)
        self._execute_tests(parser, 'path')

    def test_snake_case(self):
        parser = CharacterDelimitedParser(CharacterType.UNDERSCORE)
        self._execute_tests(parser, 'snake_case')

    def _execute_tests(self, parser: ParserBase, name: str):
        directory = Path(__file__).parent
        with directory.joinpath(f'data/{name}.yml').open('r') as f:
            settings = safe_load(f)

        for field, words in settings.items():
            self.assertEqual(
                [CharacterContainer(word) for word in words],
                parser.parse(CharacterContainer(field))
            )
