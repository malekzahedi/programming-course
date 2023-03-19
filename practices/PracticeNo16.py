# تابعی که بی شمار شعاع دایره بگیره و برای هر شعاع محیط و مساحت رو توی یه متغیر مناسب خروجی بده



import math


def circumference_and_area_of_one_circle(r):
    result = {'area': 0, 'circumference': 0}
    result['area'] = 2 * math.pi * r
    result['circumference'] = math.pi * (r ** 2)
    return result
x = circumference_and_area_of_one_circle(7)
print(x)


def circumference_and_area_of_many_circles(*args):
    result = {}
    for r in args:
        result[r] = circumference_and_area_of_one_circle(r)
    return result
x = circumference_and_area_of_many_circles(7,3,2)
print(x)