# ده عدد بگیره، هربار عدد جدید رو با قبلی حمع کنه



# # راه اول

def print_sum_of_two_last_numbers():
    previous_number = 0
    counter = 0
    while counter != 10:
        current_number = float(input("Enter a number:"))
        sum = previous_number + current_number
        print(sum)
        counter = counter + 1
        previous_number = current_number

print_sum_of_two_last_numbers()



# # راه دوم

def print_sum_of_two_last_numbers():
    previous_number = float(input("Enter first number:"))
    counter = 0
    while counter != 9:
        current_number = float(input("Enter another number:"))
        sum = previous_number + current_number
        print(sum)
        counter = counter + 1
        previous_number = current_number

print_sum_of_two_last_numbers()



# # راه سوم

def print_sum_of_two_last_numbers():
    previous_number = 0
    counter = 0
    while counter != 10:
        current_number = float(input("Enter a number:"))
        if counter != 0:
            sum = previous_number + current_number
            print(sum)
        counter = counter + 1
        previous_number = current_number

print_sum_of_two_last_numbers()