# a = [1,3,7,10,45,20,8]


# for i in a:
#     if i % 2 == 0:
#         print(i)
#         break


a = [1,3,7,10,45,20,8]


counter = 0
for i in a:
    if i % 2 == 0:
        print(i)
        counter = counter + 1
    if counter == 2:
        break
