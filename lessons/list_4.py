a = [3, 5 ,7 ,333 ,4, 3]

b = a.count(6)

print(b)


c = [2,5,6]

d = a.extend(c)

print(a)

print(d)


a = [3, 5 ,7 ,333 ,4, 3, 4]
b = a.copy()

b.extend(c)

print(a)
print(c)
print(b)



print(a.index(333))


a.insert(2, 555)
print(a)


e = a.pop(3)
print(e)
print(a)


a.remove(4)
print(a)


a.reverse()
print(a)


a.sort(reverse=True)
print(a)
