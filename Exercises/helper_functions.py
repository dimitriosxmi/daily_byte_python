import random


def string_generator(length=5, characters=None):
    """Generates a ``length`` character long string made of ``characters``.
    :type length: int
    :type characters: list[str]
    :param length: The length of the returned string. Default is 5.
    :param characters: List of unique characters that should be used per string.
    Only 1 random character will be used from list values with more than one character.
    Default is lowercase a-z.
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


print(string_generator())
