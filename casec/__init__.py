from typing import List

from casec.container import CharacterType, CharacterContainer
from casec.formatter import CaseDelimitedFormatter, DelimitedFormatter
from casec.parser import DelimitedParser, CaseDelimitedParser


def parse_snake_case(string: str):
    return DelimitedParser(CharacterType.UNDERSCORE).parse(CharacterContainer(string))


def parse_camel_case(string: str):
    return CaseDelimitedParser(CharacterType.UPPERCASE).parse(CharacterContainer(string))


def parse_pascal_case(string: str):
    return CaseDelimitedParser(CharacterType.UPPERCASE).parse(CharacterContainer(string))


def parse_constant_case(string: str):
    return DelimitedParser(CharacterType.UNDERSCORE).parse(CharacterContainer(string))


def parse_kebab_case(string: str):
    return DelimitedParser(CharacterType.DASH).parse(CharacterContainer(string))


def parse_domain(string: str):
    return DelimitedParser(CharacterType.DOT).parse(CharacterContainer(string))


def parse_path(string: str):
    return DelimitedParser(CharacterType.SLASH).parse(CharacterContainer(string))


def snake_case_to_camel_case(string: str, acronyms: List[str]):
    words = parse_snake_case(string)
    return CaseDelimitedFormatter(CharacterType.LOWERCASE, acronyms).format(words)


def snake_case_to_pascal_case(string: str, acronyms: List[str]):
    words = parse_snake_case(string)
    return CaseDelimitedFormatter(CharacterType.UPPERCASE, acronyms).format(words)


def snake_case_to_constant_case(string: str):
    words = [CharacterContainer(str(word).upper()) for word in parse_snake_case(string)]
    return DelimitedFormatter('_').format(words)


def snake_case_to_kebab_case(string: str):
    words = parse_snake_case(string)
    return DelimitedFormatter('-').format(words)


def snake_case_to_domain(string: str):
    words = parse_snake_case(string)
    return DelimitedFormatter('.').format(words)


def snake_case_to_path(string: str):
    words = parse_snake_case(string)
    return DelimitedFormatter('/').format(words)


def camel_case_to_snake_case(string: str):
    words = parse_camel_case(string)
    return DelimitedFormatter('_').format(words)


def camel_case_to_pascal_case(string: str, acronyms: List[str]):
    words = parse_camel_case(string)
    return CaseDelimitedFormatter(CharacterType.UPPERCASE, acronyms).format(words)


def camel_case_to_constant_case(string: str):
    words = [CharacterContainer(str(word).upper()) for word in parse_camel_case(string)]
    return DelimitedFormatter('_').format(words)


def camel_case_to_kebab_case(string: str):
    words = parse_camel_case(string)
    return DelimitedFormatter('-').format(words)


def camel_case_to_domain(string: str):
    words = parse_camel_case(string)
    return DelimitedFormatter('.').format(words)


def camel_case_to_path(string: str):
    words = parse_camel_case(string)
    return DelimitedFormatter('/').format(words)


def pascal_case_to_snake_case(string: str):
    words = parse_pascal_case(string)
    return DelimitedFormatter('_').format(words)


def pascal_case_to_camel_case(string: str, acronyms: List[str]):
    words = parse_pascal_case(string)
    return CaseDelimitedFormatter(CharacterType.LOWERCASE, acronyms).format(words)


def pascal_case_to_constant_case(string: str):
    words = [CharacterContainer(str(word).upper()) for word in parse_pascal_case(string)]
    return DelimitedFormatter('_').format(words)


def pascal_case_to_kebab_case(string: str):
    words = parse_pascal_case(string)
    return DelimitedFormatter('-').format(words)


def pascal_case_to_domain(string: str):
    words = parse_pascal_case(string)
    return DelimitedFormatter('.').format(words)


def pascal_case_to_path(string: str):
    words = parse_pascal_case(string)
    return DelimitedFormatter('/').format(words)


def constant_case_to_snake_case(string: str):
    words = parse_constant_case(string)
    return DelimitedFormatter('_').format(words)


def constant_case_to_camel_case(string: str, acronyms: List[str]):
    words = parse_constant_case(string)
    return CaseDelimitedFormatter(CharacterType.LOWERCASE, acronyms).format(words)


def constant_case_to_pascal_case(string: str, acronyms: List[str]):
    words = parse_constant_case(string)
    return CaseDelimitedFormatter(CharacterType.UPPERCASE, acronyms).format(words)


def constant_case_to_kebab_case(string: str):
    words = parse_constant_case(string)
    return DelimitedFormatter('-').format(words)


def constant_case_to_domain(string: str):
    words = parse_constant_case(string)
    return DelimitedFormatter('.').format(words)


def constant_case_to_path(string: str):
    words = parse_constant_case(string)
    return DelimitedFormatter('/').format(words)


def kebab_case_to_snake_case(string: str):
    words = parse_kebab_case(string)
    return DelimitedFormatter('_').format(words)


def kebab_case_to_camel_case(string: str, acronyms: List[str]):
    words = parse_kebab_case(string)
    return CaseDelimitedFormatter(CharacterType.LOWERCASE, acronyms).format(words)


def kebab_case_to_pascal_case(string: str, acronyms: List[str]):
    words = parse_kebab_case(string)
    return CaseDelimitedFormatter(CharacterType.UPPERCASE, acronyms).format(words)


def kebab_case_to_constant_case(string: str):
    words = [CharacterContainer(str(word).upper()) for word in parse_kebab_case(string)]
    return DelimitedFormatter('_').format(words)


def kebab_case_to_domain(string: str):
    words = parse_kebab_case(string)
    return DelimitedFormatter('.').format(words)


def kebab_case_to_path(string: str):
    words = parse_kebab_case(string)
    return DelimitedFormatter('/').format(words)


def domain_to_snake_case(string: str):
    words = parse_domain(string)
    return DelimitedFormatter('_').format(words)


def domain_to_camel_case(string: str, acronyms: List[str]):
    words = parse_domain(string)
    return CaseDelimitedFormatter(CharacterType.LOWERCASE, acronyms).format(words)


def domain_to_pascal_case(string: str, acronyms: List[str]):
    words = parse_domain(string)
    return CaseDelimitedFormatter(CharacterType.UPPERCASE, acronyms).format(words)


def domain_to_constant_case(string: str):
    words = [CharacterContainer(str(word).upper()) for word in parse_domain(string)]
    return DelimitedFormatter('_').format(words)


def domain_to_kebab_case(string: str):
    words = parse_domain(string)
    return DelimitedFormatter('-').format(words)


def domain_to_path(string: str):
    words = parse_domain(string)
    return DelimitedFormatter('/').format(words)


def path_to_snake_case(string: str):
    words = parse_path(string)
    return DelimitedFormatter('_').format(words)


def path_to_camel_case(string: str, acronyms: List[str]):
    words = parse_path(string)
    return CaseDelimitedFormatter(CharacterType.LOWERCASE, acronyms).format(words)


def path_to_pascal_case(string: str, acronyms: List[str]):
    words = parse_path(string)
    return CaseDelimitedFormatter(CharacterType.UPPERCASE, acronyms).format(words)


def path_to_constant_case(string: str):
    words = [CharacterContainer(str(word).upper()) for word in parse_path(string)]
    return DelimitedFormatter('_').format(words)


def path_to_kebab_case(string: str):
    words = parse_path(string)
    return DelimitedFormatter('-').format(words)


def path_to_domain(string: str):
    words = parse_path(string)
    return DelimitedFormatter('.').format(words)
