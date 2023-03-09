def is_vowel(value):
    return value.capitalize() in ('A','E','I','O','U')


def is_consonant(value):
    return value.capitalize() in ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z')


def count_vowels(value):
    result = 0
    for i in value:
        if is_vowel(i):
            result = result + 1
    return result


def count_consonants(value):
    result = 0
    for i in value:
        if is_consonant(i):
            result = result + 1
    return result


def count_vowels_and_consonants(value):
    return {'vowels': count_vowels(value), 'consonants': count_consonants(value)}


def count_vowels_and_consonants_of_some_strings(*args):
    result = {}
    for i in args:
        result[i] = count_vowels_and_consonants(i)
    return result
