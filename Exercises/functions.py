"""
This file contains all the functions that are being imported and utilized
as helper functions in the rest of the project files.
"""

import random
from types import NoneType


def string_generator(length=5, characters=None):
    """Generates a ``length`` character long string made of random characters from ``characters``.
    :type length: int
    :type characters: list[str]
    :param length: The length of the returned string. Default is 5.
    :param characters: List of unique characters that should be used per string.
    Only 1 random character will be used from list values with more than one character.
    Default is lowercase a-z.
    :return: The generated string.
    :rtype: str
    """
    if characters is None:
        characters = ['abcdefghijklmnopqrstuvwxyz']
    random_str = ""

    i = 0
    while i < length:
        character = characters[random.randint(0, len(characters) - 1)]
        char = character[random.randint(0, len(character) - 1)]
        random_str += char
        i += 1

    return random_str


def list_generator(length=5, items=None, str_gen_settings=None):
    """Generates a ``length`` long list using ``items`` at random.
    Supports string_generator usage through ``str_gen_settings`` parameter.
    :type length: int
    :type items: list[str]
    :type str_gen_settings: list[int] | list[int, list[str]]
    :param length: The elements count of the returned list. Default is 5.
    :param items: A list of strings used at random order to define each element
    in the generated list. Default is ["abc", "def", "ghi", "jkl", "mno"].
    :param str_gen_settings: A list of arguments to pass to the string generator
    if you want to use it for the generated list. Default is [].
    The string generator won't be used unless the list gets for the first element
    an integer and for the second element a list of strings.
    :return : asdasdas
    :rtype: list[str]
    """
    if str_gen_settings is None:
        str_gen_settings = []
    if items is None:
        items = ["abc", "def", "ghi", "jkl", "mno"]
    tmp_list = []

    i = 0
    while i < length:
        item = ""
        # Default behaviour
        if not str_gen_settings:
            item = items[random.randint(0, len(items) - 1)]
        # String Generator usage behaviour
        elif str_gen_settings:
            if isinstance(str_gen_settings[0], int):
                if (len(str_gen_settings) > 1
                        and (isinstance(str_gen_settings[1], NoneType)
                             or (isinstance(str_gen_settings[1], list)
                                 and isinstance(str_gen_settings[1][0], str)))):
                    item = string_generator(str_gen_settings[0], str_gen_settings[1])
                else:
                    item = string_generator(str_gen_settings[0])
        tmp_list.append(item)
        i += 1
    return tmp_list