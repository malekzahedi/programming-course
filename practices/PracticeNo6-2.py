# تعداد رقم های صحیح یک عدد رو حساب کنه


def get_number_of_integers_in_a_number(number):
    result = len(str(int(number)))
    return result

print(get_number_of_integers_in_a_number(32.1))