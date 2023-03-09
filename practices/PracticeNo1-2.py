# # دو عدد بگیره و عدد مختلط بسازه



# # First Way : NONE ??????

# def get_a_complex_number():
#     real_part = float(input('Please enter the "Real Part":'))
#     imaginary_number = float(input('Please enter the "Imaginary Number":'))
#     result = print('Your complex number is:', complex(real_part,imaginary_number))
#     return result

# complex_number = get_a_complex_number()
# print(complex_number)



# # Second Way

def get_a_complex_number():
    real_part = float(input('Please enter the "Real Part":'))
    imaginary_number = float(input('Please enter the "Imaginary Number":'))
    result = complex(real_part,imaginary_number)
    return result

complex_number = get_a_complex_number()
print('Your complex number is:', complex_number)