number = 31221

number_of_digits = 1

while True:
    if 10**number_of_digits > number:
        break
    else:
        # number_of_digits = number_of_digits + 1
        number_of_digits += 1

print(number_of_digits)
