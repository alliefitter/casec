from abc import ABC, abstractmethod
from typing import List, Optional

from casec.container import CharacterType, CharacterContainer, Character


class ParserBase(ABC):
    def __init__(self, delimiter: CharacterType):
        self._delimiter = delimiter

    @property
    def delimiter(self) -> CharacterType:
        return self._delimiter

    def get_next_character(self, raw_container: CharacterContainer, index: int) -> Optional[Character]:
        next_character = None
        if index + 1 < len(raw_container.characters):
            next_character = raw_container.characters[index + 1]

        return next_character

    def get_previous_character(self, raw_container: CharacterContainer, index: int) -> Optional[Character]:
        previous_character = None
        if index - 1 >= 0:
            previous_character = raw_container.characters[index - 1]

        return previous_character

    @abstractmethod
    def parse(self, raw_container: CharacterContainer) -> List[CharacterContainer]:
        raise NotImplementedError


class DelimitedParser(ParserBase):
    def parse(self, raw_container: CharacterContainer) -> List[CharacterContainer]:
        delimiter = self._delimiter
        words = []
        index = 0
        container = CharacterContainer()
        while True:
            if index == len(raw_container.characters):
                break
            previous_character = self.get_previous_character(raw_container, index)
            next_character = self.get_next_character(raw_container, index)
            character: Character = raw_container.characters[index]
            if character.case == delimiter and len(container.characters) > 0 and previous_character \
                    and previous_character.case != delimiter and next_character \
                    and next_character.case != delimiter:

                index += 1
                character = raw_container.characters[index]
                words.append(container)
                container = CharacterContainer()

            elif character.case == delimiter and len(
                    container.characters) > 0 and next_character and next_character.case == delimiter:
                words.append(container)
                container = CharacterContainer()

            if previous_character and previous_character.case == delimiter \
                    and character.case != delimiter:

                words.append(container)
                container = CharacterContainer()

            container.append_str(
                character.character.lower() if character.case == CharacterType.UPPERCASE else character.character
            )
            index += 1

        words.append(container)

        return words


class CaseDelimitedParser(ParserBase):
    def parse(self, raw_container: CharacterContainer) -> List[CharacterContainer]:
        words = []
        index = 0
        delimiter = self._delimiter
        container = CharacterContainer()
        while True:
            if index == len(raw_container.characters):
                break
            character: Character = raw_container.characters[index]

            if (self._is_new_word(raw_container, index) or self._is_series_of_delimiters(raw_container, index)) \
                    and not self._is_plural_series_of_delimiters(raw_container, index):

                words.append(container)
                container = CharacterContainer()

            container.append_str(
                character.character.lower() if character.case == CharacterType.UPPERCASE else character.character
            )
            index += 1

        words.append(container)

        return words

    def _is_plural_series_of_delimiters(self, raw_container: CharacterContainer, index: int) -> bool:
        delimiter = self._delimiter
        previous_character = self.get_previous_character(raw_container, index)
        next_character = self.get_next_character(raw_container, index)
        two_characters_ahead = self.get_next_character(raw_container, index + 1)
        character: Character = raw_container.characters[index]

        return previous_character and previous_character.case == delimiter and character.case == delimiter \
               and next_character and next_character.character == 's' \
               and (not two_characters_ahead or two_characters_ahead.case == delimiter)

    def _is_new_word(self, raw_container: CharacterContainer, index: int):
        delimiter = self._delimiter
        normal_case = CharacterType.LOWERCASE if delimiter == CharacterType.UPPERCASE else CharacterType.UPPERCASE
        previous_character = self.get_previous_character(raw_container, index)
        character: Character = raw_container.characters[index]

        return character.case == delimiter and previous_character and previous_character.case == normal_case

    def _is_series_of_delimiters(self, raw_container: CharacterContainer, index: int):
        delimiter = self._delimiter
        normal_case = CharacterType.LOWERCASE if delimiter == CharacterType.UPPERCASE else CharacterType.UPPERCASE
        next_character = self.get_next_character(raw_container, index)
        character: Character = raw_container.characters[index]

        return next_character and next_character.case == normal_case and character.case == delimiter
