from argparse import Namespace

from io import StringIO
from pathlib import Path
from typing import List
from unittest import TestCase

from yaml import safe_load

from casec import CharacterType
from casec.command import SnakeCaseCommand, CommandInterface, CamelCaseCommand, PascalCaseCommand, KebabCaseCommand, \
    ConstantCaseCommand, PathCommand, DomainCommand, CsvCommand
from casec.operation import ParseCharacterDelimited, FormatCamelCase, FormatPascalCase, FormatKebabCase, \
    FormatConstantCase, FormatDomain, FormatPath, FormatCsv, ParseCaseDelimited, FormatSnakeCase


class TestCommand(TestCase):
    def test_snake_case(self):
        out = StringIO()
        command = SnakeCaseCommand(
            (
                ParseCharacterDelimited(CharacterType.UNDERSCORE),
                FormatCamelCase(),
                FormatPascalCase(),
                FormatKebabCase(),
                FormatConstantCase(),
                FormatDomain(),
                FormatPath(),
                FormatCsv()
            ),
            out
        )
        self._execute_tests(
            'snake_case',
            out,
            command,
            [
                'camel_case',
                'pascal_case',
                'kebab_case',
                'domain',
                'path',
                'csv',
                'constant_case'
            ]
        )

    def test_camel_case(self):
        out = StringIO()
        command = CamelCaseCommand(
            (
                ParseCaseDelimited(CharacterType.UPPERCASE),
                FormatSnakeCase(),
                FormatPascalCase(),
                FormatKebabCase(),
                FormatConstantCase(),
                FormatDomain(),
                FormatPath(),
                FormatCsv()
            ),
            out
        )
        self._execute_tests(
            'camel_case',
            out,
            command,
            [
                'snake_case',
                'pascal_case',
                'kebab_case',
                'domain',
                'path',
                'csv',
                'constant_case'
            ]
        )

    def test_pascal_case(self):
        out = StringIO()
        command = PascalCaseCommand(
            (
                ParseCaseDelimited(CharacterType.UPPERCASE),
                FormatSnakeCase(),
                FormatCamelCase(),
                FormatKebabCase(),
                FormatConstantCase(),
                FormatDomain(),
                FormatPath(),
                FormatCsv()
            ),
            out
        )
        self._execute_tests(
            'pascal_case',
            out,
            command,
            [
                'snake_case',
                'camel_case',
                'kebab_case',
                'domain',
                'path',
                'csv',
                'constant_case'
            ]
        )

    def test_kebab_case(self):
        out = StringIO()
        command = KebabCaseCommand(
            (
                ParseCharacterDelimited(CharacterType.DASH),
                FormatSnakeCase(),
                FormatCamelCase(),
                FormatPascalCase(),
                FormatConstantCase(),
                FormatDomain(),
                FormatPath(),
                FormatCsv()
            ),
            out
        )
        self._execute_tests(
            'kebab_case',
            out,
            command,
            [
                'snake_case',
                'camel_case',
                'pascal_case',
                'domain',
                'path',
                'csv',
                'constant_case'
            ]
        )

    def test_constant_case(self):
        out = StringIO()
        command = ConstantCaseCommand(
            (
                ParseCharacterDelimited(CharacterType.UNDERSCORE),
                FormatSnakeCase(),
                FormatCamelCase(),
                FormatPascalCase(),
                FormatKebabCase(),
                FormatDomain(),
                FormatPath(),
                FormatCsv()
            ),
            out
        )
        self._execute_tests(
            'constant_case',
            out,
            command,
            [
                'snake_case',
                'camel_case',
                'kebab_case',
                'domain',
                'path',
                'csv',
                'pascal_case'
            ]
        )

    def test_path(self):
        out = StringIO()
        command = PathCommand(
            (
                ParseCharacterDelimited(CharacterType.SLASH),
                FormatSnakeCase(),
                FormatCamelCase(),
                FormatPascalCase(),
                FormatConstantCase(),
                FormatKebabCase(),
                FormatDomain(),
                FormatCsv()
            ),
            out
        )
        self._execute_tests(
            'path',
            out,
            command,
            [
                'snake_case',
                'camel_case',
                'kebab_case',
                'domain',
                'constant_case',
                'csv',
                'pascal_case'
            ]
        )

    def test_domain(self):
        out = StringIO()
        command = DomainCommand(
            (
                ParseCharacterDelimited(CharacterType.DOT),
                FormatSnakeCase(),
                FormatCamelCase(),
                FormatPascalCase(),
                FormatConstantCase(),
                FormatPath(),
                FormatKebabCase(),
                FormatCsv()
            ),
            out
        )
        self._execute_tests(
            'domain',
            out,
            command,
            [
                'snake_case',
                'camel_case',
                'kebab_case',
                'path',
                'constant_case',
                'csv',
                'pascal_case'
            ]
        )

    def test_csv(self):
        out = StringIO()
        command = CsvCommand(
            (
                ParseCharacterDelimited(CharacterType.COMMA),
                FormatSnakeCase(),
                FormatCamelCase(),
                FormatPascalCase(),
                FormatConstantCase(),
                FormatPath(),
                FormatKebabCase(),
                FormatDomain()
            ),
            out
        )
        self._execute_tests(
            'csv',
            out,
            command,
            [
                'snake_case',
                'camel_case',
                'kebab_case',
                'path',
                'constant_case',
                'domain',
                'pascal_case'
            ]
        )

    def _execute_tests(
            self,
            name: str,
            out: StringIO,
            command: CommandInterface,
            cases: List[str]
    ):
        for i in range(len(cases)):
            file_object = self._make_file_object(name)
            kwargs = {'literals': [], 'format_literals': []}
            current_case = None
            for x, case in enumerate(cases):
                if i == x:
                    current_case = case
                    kwargs[f'format_{case}'] = True
                else:
                    kwargs[f'format_{case}'] = False

            namespace = Namespace(file_object=file_object, **kwargs)
            command.execute(namespace)
            out.seek(0)
            self.assertEqual(out.read(), self._make_file_object(current_case).read())
            out.seek(0)
            out.truncate()

    def _make_file_object(self, name: str):
        file_object = StringIO()
        directory = Path(__file__).parent
        with directory.joinpath(f'data/{name}.yml').open('r') as f:
            file_object.write('\n'.join(list(safe_load(f).keys())))

        file_object.seek(0)

        return file_object
