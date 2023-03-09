def f(value_1, value_2):
    pass

f(3, 2)



def f2(value_1 = 1):
    print(value_1)


# f2(value_1=34)



def f3(value_1 = 1, value_2 = 2):
    print(value_1)
    print(value_2)


f3(value_2=10, value_1=5)

f3(value_3=4)



def f4(value_1, value_2, value_3 = None, value_4 = None):
    print(value_1)
    print(value_2)
    print(value_3)
    print(value_4)


f4(1,2, value_4=3, value_3=2)

# f4(1,2, 3, 2)


def get_infinte_positional_arguments(*args):
    print(type(args))
    print(args)
    print(args[2])


get_infinte_positional_arguments(1,2,4,5,6,6,)


def get_infinte_keyword_arguments(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs['asghar'])


get_infinte_keyword_arguments(v1= 2, v2=3, valie=2, asghar=5)
# get_infinte_keyword_arguments(2,3,5)



def get_infinte_positional_arguments_and_keyword_arguments(*args, **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)


get_infinte_positional_arguments_and_keyword_arguments(2,3,5, v1='sdf', ffff='sdfds')
