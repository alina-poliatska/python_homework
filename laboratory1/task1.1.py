import re

def is_number(int):
    return bool(re.match('^\d[0,1]*$',int))


def get_number1():
    number1 = input('Enter number 1 : ')
    while not is_number(number1):
        number1 = input('Enter number 1 : ')
    return number1


def get_number2():
    number2 = input('Enter number 2 : ')
    while not is_number(number2):
        number2 = input('Enter number 2 : ')
    return number2


a = int(get_number1(), 2)
b = int(get_number2(), 2)

print(bin(a&b))
print(bin(a|b))
print(bin(a^b))




