# یک عدد ورودی بگیره و ارقامش رو جمع بزنه


def get_sum_of_digits_of_a_number(number):
    sum = 0
    number = str(number)
    for i in number:
        sum = int(i) + sum
    return sum

print(get_sum_of_digits_of_a_number(365))