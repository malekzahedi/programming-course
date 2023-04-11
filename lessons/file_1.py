with open('read_from_me.txt', 'r') as file:
    a = file.read()


print(a)
print(type(a))


# context manager
with open('write_to_me.txt', 'a') as file:
    file.write('\nsalam pedar sag ')



file1 = open("myfile.txt", "w")  # write mode
file1.write("Tomorrow \n")
file1.close()
