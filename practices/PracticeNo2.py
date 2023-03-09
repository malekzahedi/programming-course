# دو عدد بگیره و اولی رو به توان دومی برسونه



base = float(input("Enter Base:"))
power = int(input("Enter Power:"))
x = 1
for i in range(power):
   x = x * base
print(x)