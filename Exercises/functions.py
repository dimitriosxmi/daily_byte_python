"""
This file contains all the functions that are being imported and utilized
as helper functions in the rest of the project files.
"""

import random
import sys
from types import NoneType


def clamp(clamp_value, min_value, max_value):
    """
    Clamps the ``clamp_value`` between the ``min_value`` and the ``max_value``.
    :type clamp_value: int | float
    :type min_value: int | float
    :type max_value: int | float
    :param clamp_value: The value you want to clamp.
    :param min_value: The minimum value your clamped value must have.
    :param max_value: The maximum value your clamped value must have.
    :return: The clamped ``clamp_value`` between ``min_value`` and ``max_value``.
    :rtype: int | float
    """
    return max(min_value, min(clamp_value, max_value))


def string_generator(length=5, characters=None):
    """Generates a ``length`` character long string made of random characters
    from ``characters``.
    :type length: int
    :type characters: list[str]
    :param length: The length of the returned string. The default value is 5.
        The supplied value clamps between 1 and 1000.
    :param characters: List of characters that intended for the string generation.
        Only 1 random character will be used from list values made of more than
        one character. Default is lowercase a-z.
    :return: The generated string.
    :rtype: str
    """
    length = clamp(length, 1, 1000)

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
        The string generator won't be used unless the list gets for the first
        element an integer (the second list element expects a list of strings).
    :return: The generated list.
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


def replace_random_chars_in_string(string_value="", start_index=0, end_index=sys.maxsize, list_of_chars=None,
                                   replace_attempts=1):
    """
    Replaces a ``replace_attempts`` amount of random characters of a ``string_value``
    between the ``start_index`` and ``end_index``, using a random character from
    the ``list_of_chars``.
    :type string_value: string
    :type start_index: int
    :type end_index: int
    :type list_of_chars: list[string]
    :type replace_attempts: int
    :param string_value: The string value intended for change. If the supplied
        string's length isn't more than 0, then method prints a message.
    :param start_index: The first string's index point the changes should take
        effect from.
        The supplied value clamps between 0 and the **string_value**'s length.
    :param end_index: The last string's index point the changes should take.
        effect to.
        The supplied value clamps between 0 and the **string_value**'s length.
    :param list_of_chars: The list of randomly selected strings to replace the
        **string_value**'s string characters.
    :param replace_attempts: Amount of character replacement attempts intended
        to be executed in order to replace a random character in the
        **string_value**. The value clamps between 1 and 1000.
    :return: A string value with all the successfully applied changes
    :rtype: str
    """
    str = ""
    str_length = len(string_value)
    if str_length > 0:
        start_index = clamp(start_index, 0, str_length - 1)
        end_index = clamp(end_index, 0, str_length - 1)
        replace_attempts = clamp(replace_attempts, 1, 1000)

        if list_of_chars is None:
            list_of_chars = [".", "+", "-", "*", "/", "@"]

        i = 0
        while i < replace_attempts:
            index_to_replace = random.randint(start_index, end_index)
            chars_length = len(list_of_chars)

            replacement_char = list_of_chars[random.randint(0, chars_length - 1)]
            str = string_value[:index_to_replace] + replacement_char + string_value[index_to_replace:]

            i += 1

        return str
    else:
        print("string_value length can't be smaller than 1")


def random_fake_email_generator(min_char_count=4, max_char_count=12, min_domain_char_count=1, max_domain_char_count=5, top_level_domains=None):
    """
    Generates a fake email from random characters
    :type min_char_count: int
    :type max_char_count: int
    :type min_domain_char_count: int
    :type max_domain_char_count: int
    :type top_level_domains: list[str]
    :param min_char_count: The minimum amount of characters used in the email's
        local name. The default value is 4.
        The supplied value clamps between 1 and 64.
    :param max_char_count: The maximum amount of characters used in the email's
        local name. The default value is 12.
        The supplied value clamps between 1 and 64.
    :param min_domain_char_count: The minimum amount of characters used in the
        email's domain name. The default value is 1.
        The supplied value clamps between 1 and 255.
    :param max_domain_char_count: The maxium amount of characters used in the
        email's domain name. The default is 5.
        The supplied value clamps between 1 and 255.
    :param top_level_domains: The top-level domains meant to be used in the
        generation process. such as .com, .org, etc., If none is supplied
        the default value is ["com", "net", "org", "edu"]
    :return:
    """
    # String size capping
    min_char_count = clamp(min_char_count, 1, 64)
    max_char_count = clamp(max_char_count, 1, 64)
    min_domain_char_count = clamp(min_domain_char_count, 1, 255)
    max_domain_char_count = clamp(max_domain_char_count, 1, 255)

    email = ""
    local_name = string_generator(random.randint(min_char_count, max_char_count))
    ln_length = len(local_name)

    # Replace a character with a "+" (plus) character
    if ln_length > 1:
        ln_with_plus = replace_random_chars_in_string(local_name, 1, list_of_chars=['+'])
        local_name = ln_with_plus
    # Replace a few character with a "." (dot) character
    if ln_length > 4:
        ln_with_dots = replace_random_chars_in_string(local_name, 1, list_of_chars=['.'])
        local_name = ln_with_dots

    # Default alternative in case no argument is provided.
    if top_level_domains is None:
        top_level_domains = ["com", "net", "org", "edu"]

    domain_name = string_generator(random.randint(min_domain_char_count, max_domain_char_count))
    top_level_domain = top_level_domains[random.randint(0, len(top_level_domains) - 1)]
    email = local_name + "@" + domain_name + "." + top_level_domain

    return email
