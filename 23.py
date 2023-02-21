# dict
# water: a liquid 


person = {"age": "20", "name": "ali", "gender": "male"}


o = {1:2}

a = {True: 'salam'}


print(type(person))
print(person['name'])


print(o[1])

# key, value


person_age = person.get('age')

print(person_age)


e = person.get('last_name', 'Akbari')
print(e)


# print(person.items())


for key, value in person.items():
    print(key, value)


a  = [2,7,5]

for index, value in enumerate(a):
    print(index, value)


print(person.keys())
print(type(person.values()))


name = person.pop('name')
print(name)

print(person)

e = person.popitem()

print(type(e))
print(e)


print(person.setdefault('last_name', "Alavi"))
print(person)


# person.update('name')
# print(person)

# new_person = person.fromkeys([1,3,], 'a')
# print(new_person)


for i in person:
    print(i)


for value in person.values():
    print(value)



person['height'] = 170
print(person)


person['name'] = "reza"
print(person)

del person['name']
print(person)


print(len(person))





person = {'cars_names': ['ford', 'nissan'] }



students_of_class = [
    {'name':'ali'},
    {'name':'reza'},
]



print(students_of_class[0]['name'])
