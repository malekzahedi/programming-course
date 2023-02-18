a = [3, 5 ,7 ,333 ,4]

b = a

a[0] = 566

# pointer
print(a)
print(b)


c = a.copy()


a[1] = 323

print(a)
print(c)



d = 3
e = d

d = 5 
print(d)
print(e)
