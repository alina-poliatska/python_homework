import re

def reg(text):
    return bool(re.match('^\d*(\.){0,1}\d{0,1}$', text))


def get_number():
    number = input('Enter x : ')
    while not reg(number):
        number = input('Enter x : ')
    return float(number)

x = int(get_number())
x1 = 1.2*x**2-3*x -9
x2 = 12.1/(2*x**2+1)

if x > 3:
    print("1,2x^2-3x-9= ",round(x1,2))
else:
    print("12,1/(2x^2+1)= ",round(x2,2))
