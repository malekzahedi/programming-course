first_number = int(input('first_number: '))
second_number = int(input('second_number: '))

x = 0
for i in range(second_number):
    x = first_number + x

print(x)
