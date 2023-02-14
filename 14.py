my_string = 'salam che tori'

n = 5

result = ""
for counter, character in enumerate(my_string):
    if counter > n:
        result = result + character

print(counter)

if counter < n:
    print('n is greater than counter')


if len(my_string) <= n:
    print('n is greater than len of string')


print(result)

print(len(my_string))


result = ""
for index in range(len(my_string)):
    if index > n:
        result = result + my_string[index]

print(result)
