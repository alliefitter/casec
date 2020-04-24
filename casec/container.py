from enum import Enum
from string import ascii_uppercase, ascii_lowercase
from typing import NamedTuple, Tuple, Generator


class CharacterType(Enum):
    LOWERCASE = 0
    UPPERCASE = 1
    UNDERSCORE = 2
    DASH = 3
    DOT = 4
    SLASH = 5
    OTHER = 6


class Character(NamedTuple):
    character: str
    case: CharacterType


class CharacterContainer:
    def __init__(self, string: str = ''):
        self._string = string
        self._characters = tuple(self._map_casing())
        self._iter = None

    def __iter__(self) -> 'CharacterContainer':
        self._iter = iter(self.characters)
        return self

    def __next__(self) -> Character:
        return next(self._iter)

    def __str__(self):
        return ''.join([c.character for c in self.characters])

    @property
    def characters(self) -> Tuple[Character, ...]:
        return self._characters

    def append_str(self, string: str):
        self._string += string
        self._characters = tuple(self._map_casing())

    def _map_casing(self) -> Generator[Character, None, None]:
        for character in self._string:
            if character in ascii_uppercase:
                yield Character(character, CharacterType.UPPERCASE)
            elif character in ascii_lowercase:
                yield Character(character, CharacterType.LOWERCASE)
            elif character == '_':
                yield Character(character, CharacterType.UNDERSCORE)
            elif character == '-':
                yield Character(character, CharacterType.DASH)
            else:
                yield Character(character, CharacterType.OTHER)
