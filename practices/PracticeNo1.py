# دو عدد بگیره و عدد مختلط بسازه



real_part = input('Please enter the "Real Part":')
imaginary_number = input('Please enter the "Imaginary Number":')

try:
    real_part = float(real_part)
except ValueError:
    print("invalid real part")
else:
    try:
        imaginary_number = float(imaginary_number)
    except ValueError:
        print("invalid imaginary number")
    else:
        print(complex(real_part,imaginary_number))