sogand_physic_number = input("Type Number please type a valid integer be joone maderet: ")


try:
    sogand_physic_number = int(sogand_physic_number)
except ValueError:
    print('your input is not in correct format')
except NameError:
    print('your code has name error')
else:
    print(sogand_physic_number * 1.2)
