# یک عدد ورودی بگیره و ارقامش رو جمع بزنه


number = str(input('Enter a number: '))
sum = 0
for i in number:
    sum = int(i) + sum
print(sum)