def print_hello_world():
    print('Hello world')


def print_hi():
    print('hi')


def print_hi_to_a_person(name):
    print('hi ' + name )


def print_they_are_friend(name_1, name_2):
    print(name_1, "and", name_2, "are friends")


def get_a_friendship_sentence(name_1, name_2):
    string = name_1 + " and " + name_2 + " are friends"
    # print(string)
    # print(type(string))
    return string


print_hello_world()
print_hi()


print_hi_to_a_person('Sogand')
print_hi_to_a_person('Ali')

print_they_are_friend('ali', 'reza')

get_a_friendship_sentence('ali', 'reza')

sentence = get_a_friendship_sentence('ali', 'reza')

sentence = sentence + "!"

print(sentence)


# scope
