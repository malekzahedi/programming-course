import sys
sys.setrecursionlimit(1000)


def wallis_product(n):
    c = 1
    for i in range(1,n):
        a = 4 * i ** 2
        b = 4 * i ** 2 - 1
        c = c * (a/b)
    return c   


def recursive_wallis_product(n):
    a = 4 * n ** 2
    b = 4 * n ** 2 - 1
    c = a/b
    if n == 1:
        return c
    else:
        return c * recursive_wallis_product(n-1)


print('pi is almost: ', wallis_product(100)*2)
print('pi is almost: ', recursive_wallis_product(100)*2)
