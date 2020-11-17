from argparse import Namespace
from io import StringIO
from pathlib import Path
from unittest import TestCase

from yaml import safe_load

from casec import CharacterType, CharacterContainer
from casec.operation import OperationInterface, ParseCaseDelimited, ParseCharacterDelimited, FormatCamelCase, \
    FormatPascalCase, FormatSnakeCase, FormatPath, FormatKebabCase, FormatDomain, FormatConstantCase, FormatCsv


class TestOperation(TestCase):
    def test_format_camel_case(self):
        operation = FormatCamelCase()
        namespace = Namespace(format_camel_case=True, format_literals=[])
        self._execute_format_test(operation, namespace, 'camel_case')

    def test_format_camel_case_with_literals(self):
        operation = FormatCamelCase()
        namespace = Namespace(format_camel_case=True, format_literals=['iOS', 'iTunes', 'VPP', 'ID', 'IDs'])
        self._execute_format_test(operation, namespace, 'camel_case_with_literals')

    def test_format_constant_case(self):
        operation = FormatConstantCase()
        namespace = Namespace(format_constant_case=True, format_literals=[])
        self._execute_format_test(operation, namespace, 'constant_case')

    def test_format_csv(self):
        operation = FormatCsv()
        namespace = Namespace(format_csv=True, format_literals=[])
        self._execute_format_test(operation, namespace, 'csv')

    def test_format_domain(self):
        operation = FormatDomain()
        namespace = Namespace(format_domain=True, format_literals=[])
        self._execute_format_test(operation, namespace, 'domain')

    def test_format_kebab_case(self):
        operation = FormatKebabCase()
        namespace = Namespace(format_kebab_case=True, format_literals=[])
        self._execute_format_test(operation, namespace, 'kebab_case')

    def test_format_pascal_case(self):
        operation = FormatPascalCase()
        namespace = Namespace(format_pascal_case=True, format_literals=[])
        self._execute_format_test(operation, namespace, 'pascal_case')

    def test_format_pascal_case_with_literals(self):
        operation = FormatPascalCase()
        namespace = Namespace(format_pascal_case=True, format_literals=['iOS', 'iTunes', 'VPP', 'ID', 'IDs'])
        self._execute_format_test(operation, namespace, 'pascal_case_with_literals')

    def test_format_path(self):
        operation = FormatPath()
        namespace = Namespace(format_path=True, format_literals=[])
        self._execute_format_test(operation, namespace, 'path')

    def test_format_snake_case(self):
        operation = FormatSnakeCase()
        namespace = Namespace(format_snake_case=True, format_literals=[])
        self._execute_format_test(operation, namespace, 'snake_case')

    def test_parse_camel_case(self):
        namespace = Namespace(literals=[])
        operation = ParseCaseDelimited(CharacterType.UPPERCASE)
        self._execute_parse_test(operation, namespace, 'camel_case')

    def test_parse_camel_case_with_literals(self):
        namespace = Namespace(literals=['iOS', 'iTunes', 'VPP', 'IDs'])
        operation = ParseCaseDelimited(CharacterType.UPPERCASE)
        self._execute_parse_test(operation, namespace, 'camel_case_with_literals')

    def test_parse_constant_case(self):
        namespace = Namespace()
        operation = ParseCharacterDelimited(CharacterType.UNDERSCORE)
        self._execute_parse_test(operation, namespace, 'constant_case')

    def test_parse_domain(self):
        namespace = Namespace()
        operation = ParseCharacterDelimited(CharacterType.DOT)
        self._execute_parse_test(operation, namespace, 'domain')

    def test_parse_kebab_case(self):
        namespace = Namespace()
        operation = ParseCharacterDelimited(CharacterType.DASH)
        self._execute_parse_test(operation, namespace, 'kebab_case')

    def test_parse_pascal_case(self):
        namespace = Namespace(literals=[])
        operation = ParseCaseDelimited(CharacterType.UPPERCASE)
        self._execute_parse_test(operation, namespace, 'pascal_case')

    def test_parse_pascal_case_with_literals(self):
        namespace = Namespace(literals=['iOS', 'iTunes', 'VPP', 'IDs'])
        operation = ParseCaseDelimited(CharacterType.UPPERCASE)
        self._execute_parse_test(operation, namespace, 'pascal_case_with_literals')

    def test_parse_path(self):
        namespace = Namespace()
        operation = ParseCharacterDelimited(CharacterType.SLASH)
        self._execute_parse_test(operation, namespace, 'path')

    def test_parse_snake_case(self):
        namespace = Namespace()
        operation = ParseCharacterDelimited(CharacterType.UNDERSCORE)
        self._execute_parse_test(operation, namespace, 'snake_case')

    def _execute_format_test(self, operation: OperationInterface, namespace: Namespace, name: str):
        directory = Path(__file__).parent
        words = []
        formatted_strings = []
        with directory.joinpath(f'data/{name}.yml').open('r') as f:
            settings = safe_load(f)

        for field, words_ in settings.items():
            words.append([CharacterContainer(word) for word in words_])
            formatted_strings.append(field)

        namespace.parsed_words = words
        self.assertTrue(operation.should_perform(namespace))
        operation.perform(namespace)
        self.assertEqual(formatted_strings, namespace.formatted_strings)

    def _execute_parse_test(self, operation: OperationInterface, namespace: Namespace, name: str):
        file_object = StringIO()
        directory = Path(__file__).parent
        words = []
        with directory.joinpath(f'data/{name}.yml').open('r') as f:
            settings = safe_load(f)

        for field, words_ in settings.items():
            file_object.write(f'{field}\n')
            words.append([CharacterContainer(word) for word in words_])

        file_object.seek(0)
        namespace.file_object = file_object

        self.assertTrue(operation.should_perform(namespace))
        operation.perform(namespace)
        self.assertEqual(words, namespace.parsed_words)
