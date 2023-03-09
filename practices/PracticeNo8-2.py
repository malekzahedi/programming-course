# اجتماع و اشتراک دو مجموعه رو پرینت کنه






# اشتراک دو مجموعه

def intersection_of_two_sets():
    first_Set_of_numbers = [1, 3, 4, 10, 13, 25]
    second_Set_of_numbers = [3, 5, 10, 16, 20, 25]
    intersection_of_sets = []
    for i in first_Set_of_numbers:
        for j in second_Set_of_numbers:
            if i == j:
                intersection_of_sets.append(i)
                result = set(intersection_of_sets)
    return result

r = intersection_of_two_sets()
print('Intersection of sets =', r)


# اجتماع دو مجموعه

def union_of_two_sets():
    first_Set_of_numbers = (1, 3, 4, 10, 13, 25)
    second_Set_of_numbers = (3, 5, 10, 16, 20, 25)
    # union_of_sets = ()
    # for i in first_Set_of_numbers:
    #     for j in second_Set_of_numbers:
    #         if i == j:
    #             second_Set_of_numbers.remove(j)
    result = set(first_Set_of_numbers + second_Set_of_numbers)
    return result

r = union_of_two_sets()
print('Union of sets =', r)