def f():
    a = 2
    b = 3
    c = a * b


c = f()
print("c: ", c)



def f2(number):
    return len(str(int(number)))


def get_and_of_two_values(value_1, value_2):
    return value_1 and value_2

r = get_and_of_two_values(True, False)
print(r)



def is_number_greater_than_ten(number):
    if number > 10:
        return True
    else:
        return False



def is_number_greater_than_ten(number):
    if number > 10:
        return True
    return False


r = is_number_greater_than_ten(3)
print(r)


r = is_number_greater_than_ten(22)
print(r)



def func(value_1):
    pass


def func(value_1):
    ...

