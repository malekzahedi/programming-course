# بزرگترین عدد یک مجموعه را پیدا کند


# راه اول 

def the_biggest_number(*args):
    x = -float('inf')
    for i in args:
        if x < i:
            x = i
    return x
r = the_biggest_number(2,3,6,13,95,12,181,1,4)
print(r)



# راه دوم

sorce_list = [5,3,9,23,64,15]
x = -float('inf')
for i in sorce_list:
    if x < i:
        x = i
print(x)