# # دو عدد بگیره و اولی رو به توان دومی برسونه


def get_powered_number(base, power):
    x = 1
    for i in range(power):
        x = x * base
    return x

print(get_powered_number(2,3))