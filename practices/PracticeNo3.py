# چاپ مجموعه ای شامل اعداد زوج مجموعه اول و اعداد فرد مجموعه دوم


even_numbers_source = [4,5,8,18,26,33]
odd_numbers_source = [3,6,9,13,24,35]
result = []
for i in even_numbers_source:
    if i % 2 == 0:
        result.append(i)
for j in odd_numbers_source:
    if j % 2 != 0:
        result.append(j)
print(result)