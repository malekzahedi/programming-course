# سومین عدد بزرگ یک لیست رو پیدا کن


source = [16, 7, 26]
source_1 = source.copy()
source_2 = list(set(source_1))
if len(source_2) >= 3:
    source_2.sort(reverse=True)
    the_third_largest_number = source_2[2]
    print('The third largest number of list is:', the_third_largest_number)
else:
    print('len of list in not enough')