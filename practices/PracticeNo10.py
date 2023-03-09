# پرتکرارترین عضو یک لیست رو معرفی کند



source_list = [5,3,9,23,64,15,3,7]

number_of_repeat = -float('inf')
most_repeated = None
for i in source_list:
    repeat_counter_of_i = 0
    for j in source_list:
        if i == j:
            repeat_counter_of_i = repeat_counter_of_i + 1
    if repeat_counter_of_i > number_of_repeat:
        number_of_repeat = repeat_counter_of_i
        most_repeated = i
print(most_repeated)    