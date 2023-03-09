
a = [{'vowels': 0, 'consonants': 0},
     {'vowels': 0, 'consonants': 0},
     {'vowels': 0, 'consonants': 0}]


def vowels_and_consonants_counter(the_string_value):
    vowels = ('A','E','I','O','U')
    consonants = ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z')
    result = {'vowels': 0, 'consonants': 0}
    for i in the_string_value:
        if i.capitalize() in vowels:
            result['vowels'] = result['vowels'] + 1
        if i.capitalize() in consonants:
            result['consonants'] = result['consonants'] + 1
    return result



#  بی شمار استرینگ ورودی بگیره و حروف صداد دار و بی صدا بشمره و به صورت دیکشنری بده


def several_vowels_and_consonants_counter(*args):
    result = []
    for i in args:
        result.append(vowels_and_consonants_counter(i))
    return result
r = several_vowels_and_consonants_counter('Mohammad', 'Sogand', 'Sima')
print(r)


def fucking_vowels_and_consonants_counter(*args):
    result = {}
    for i in args:
        result[i] = vowels_and_consonants_counter(i)
    return result
r = fucking_vowels_and_consonants_counter('Mohammad', 'Sogand', 'Sima')
print(r)