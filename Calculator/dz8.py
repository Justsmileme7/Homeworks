from dz8_1 import addition
from dz8_1 import subtraction
from dz8_1 import multiplication
from dz8_1 import division
from dz8_1 import exponentiation
from custom_exceptions import get_not_number
from custom_exceptions import wrong_operation


def get_number():
    x = input('Enter number 1\n')
    y = input('Enter number 2\n')
    return get_not_number(x, y)


def calculate():
    x, y = get_number()
    z = int(input('mathematical operation:\n'
                  'if you need addition - enter 1\n,'
                  'if you need subtraction - enter 2,\n'
                  'if you need multiplication - enter 3,\n'
                  'if you need division - enter 4,\n'
                  'if you need exponentiation - enter 5\n'))
    if int(z) == 1:
        addition(x, y)
    elif int(z) == 2:
        subtraction(x, y)
    elif int(z) == 3:
        multiplication(x, y)
    elif int(z) == 4:
        division(x, y)
    elif int(z) == 5:
        exponentiation(x, y)
    else:
        print('You need enter only one from five numbers')


calculate()
