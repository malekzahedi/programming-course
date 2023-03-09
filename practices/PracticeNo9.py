# بزرگترین عدد یک مجموعه را پیدا کند


# راه اول 

sorce_list = [5,3,9,23,64,15]
x = sorce_list[0]
for i in sorce_list:
    if x < i:
        x = i
print(x)



# راه دوم

sorce_list = [5,3,9,23,64,15]
x = -float('inf')
for i in sorce_list:
    if x < i:
        x = i
print(x)