# اجتماع و اشتراک دو مجموعه رو پرینت کنه



first_Set_of_numbers = [1, 3, 4, 10, 13, 25]
second_Set_of_numbers = [3, 5, 10, 16, 20, 25]


# اشتراک دو مجموعه

intersection_of_sets = []
for i in first_Set_of_numbers:
    for j in second_Set_of_numbers:
        if i == j:
            intersection_of_sets.append(i)
print('Intersection of sets =', intersection_of_sets)


# اجتماع دو مجموعه

for i in first_Set_of_numbers:
    for j in second_Set_of_numbers:
        if i == j:
            second_Set_of_numbers.remove(j)
union_of_sets = first_Set_of_numbers + second_Set_of_numbers
print('Union of sets =', union_of_sets)