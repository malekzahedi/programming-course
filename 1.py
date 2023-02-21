physic_number = input("Type Number please type a valid integer be joone maderet: ")


try:
    physic_number = int(physic_number)
except ValueError:
    print('your input is not in correct format')
except NameError:
    print('your code has name error')
else:
    print(physic_number * 1.2)
