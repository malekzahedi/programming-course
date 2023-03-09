# تابعی که استرینگ بگیره و تعداد حروف صدا دار و بی صدا رو توش بشماره و به صورت دیکشنری بده



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
    
r = vowels_and_consonants_counter('Sogand!')
print(r)