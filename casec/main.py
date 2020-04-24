from sys import stdout, argv

from casec.client import Client
from casec.command import RootCommandGroup, SnakeCaseCommand, CamelCaseCommand, PascalCaseCommand, KebabCaseCommand, \
    ConstantCaseCommand, DomainCommand, PathCommand
from casec.container import CharacterType
from casec.operation import ParseDelimited, FormatCamelCase, FormatKebabCase, FormatPascalCase, ParseCaseDelimited, \
    FormatSnakeCase, FormatConstantCase, FormatDomain, FormatPath


def main(args=None):
    args = args or argv[1:]
    Client(
        RootCommandGroup(
            (
                SnakeCaseCommand(
                    (
                        ParseDelimited(CharacterType.UNDERSCORE),
                        FormatCamelCase(),
                        FormatPascalCase(),
                        FormatKebabCase(),
                        FormatConstantCase(),
                        FormatDomain(),
                        FormatPath()
                    ),
                    stdout
                ),
                CamelCaseCommand(
                    (
                        ParseCaseDelimited(CharacterType.UPPERCASE),
                        FormatSnakeCase(),
                        FormatPascalCase(),
                        FormatKebabCase(),
                        FormatConstantCase(),
                        FormatDomain(),
                        FormatPath()
                    ),
                    stdout
                ),
                PascalCaseCommand(
                    (
                        ParseCaseDelimited(CharacterType.UPPERCASE),
                        FormatSnakeCase(),
                        FormatCamelCase(),
                        FormatKebabCase(),
                        FormatConstantCase(),
                        FormatDomain(),
                        FormatPath()
                    ),
                    stdout
                ),
                KebabCaseCommand(
                    (
                        ParseDelimited(CharacterType.DASH),
                        FormatSnakeCase(),
                        FormatCamelCase(),
                        FormatPascalCase(),
                        FormatKebabCase(),
                        FormatDomain(),
                        FormatPath()
                    ),
                    stdout
                ),
                ConstantCaseCommand(
                    (
                        ParseDelimited(CharacterType.DASH),
                        FormatSnakeCase(),
                        FormatCamelCase(),
                        FormatPascalCase(),
                        FormatKebabCase(),
                        FormatDomain(),
                        FormatPath()
                    ),
                    stdout
                ),
                PathCommand(
                    (
                        ParseDelimited(CharacterType.DASH),
                        FormatSnakeCase(),
                        FormatCamelCase(),
                        FormatPascalCase(),
                        FormatConstantCase(),
                        FormatKebabCase(),
                        FormatDomain()
                    ),
                    stdout
                ),
                DomainCommand(
                    (
                        ParseDelimited(CharacterType.DASH),
                        FormatSnakeCase(),
                        FormatCamelCase(),
                        FormatPascalCase(),
                        FormatConstantCase(),
                        FormatDomain(),
                        FormatKebabCase()
                    ),
                    stdout
                )
            )
        )
    ).run(args)


if __name__ == '__main__':
    main(argv[1:])
