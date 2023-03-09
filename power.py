base = float(input('base: '))
power = int(input('power: '))

x = 1
for _ in range(power):
    x = base * x

print(x)
