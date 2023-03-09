# چاپ مجموعه ای شامل اعداد زوج مجموعه اول و اعداد فرد مجموعه دوم


def get_a_list_of_odds_and_evens(even_numbers_source, odd_numbers_source):
    result = []
    for i in even_numbers_source:
        if i % 2 == 0:
            result.append(i)
    for j in odd_numbers_source:
        if j % 2 != 0:
            result.append(j)
    return result

print(get_a_list_of_odds_and_evens([4,5,8,18,26,33], [3,6,9,13,24,35]))