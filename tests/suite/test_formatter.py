from pathlib import Path
from unittest import TestCase

from yaml import safe_load

from delim import CaseDelimitedFormatter, CharacterType, CharacterContainer
from delim.formatter import FormatterBase, CharacterDelimitedFormatter


class TestFormatter(TestCase):
    def test_camel_case(self):
        formatter = CaseDelimitedFormatter(CharacterType.LOWERCASE)
        self._execute_tests(formatter, 'camel_case')

    def test_camel_case_with_literals(self):
        formatter = CaseDelimitedFormatter(CharacterType.LOWERCASE, ['iOS', 'iTunes', 'VPP', 'ID', 'IDs'])
        self._execute_tests(formatter, 'camel_case_with_literals')

    def test_domain(self):
        formatter = CharacterDelimitedFormatter(',')
        self._execute_tests(formatter, 'csv')

    def test_constant_case(self):
        directory = Path(__file__).parent
        formatter = CharacterDelimitedFormatter('_')
        with directory.joinpath('data/constant_case.yml').open('r') as f:
            settings = safe_load(f)

        for field, words in settings.items():
            self.assertEqual(field, formatter.format([CharacterContainer(word.upper()) for word in words]))

    def test_domain(self):
        formatter = CharacterDelimitedFormatter('.')
        self._execute_tests(formatter, 'domain')

    def test_kebab_case(self):
        formatter = CharacterDelimitedFormatter('-')
        self._execute_tests(formatter, 'kebab_case')

    def test_pascal_case(self):
        formatter = CaseDelimitedFormatter(CharacterType.UPPERCASE)
        self._execute_tests(formatter, 'pascal_case')

    def test_pascal_case_with_literals(self):
        formatter = CaseDelimitedFormatter(CharacterType.UPPERCASE, ['iOS', 'iTunes', 'VPP', 'ID', 'IDs'])
        self._execute_tests(formatter, 'pascal_case_with_literals')

    def test_path(self):
        formatter = CharacterDelimitedFormatter('/')
        self._execute_tests(formatter, 'path')

    def test_snake_case(self):
        formatter = CharacterDelimitedFormatter('_')
        self._execute_tests(formatter, 'snake_case')

    def _execute_tests(self, formatter: FormatterBase, name: str):
        directory = Path(__file__).parent
        with directory.joinpath(f'data/{name}.yml').open('r') as f:
            settings = safe_load(f)

        for field, words in settings.items():
            self.assertEqual(field, formatter.format([CharacterContainer(word) for word in words]))
