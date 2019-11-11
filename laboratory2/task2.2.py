import re


def reg(text):
    return bool(re.match('^[1-9][0-9]*$', text))


def get_number():
    number = input('Enter n : ')
    while not reg(number):
        number = input('Enter n : ')
    return int(number)


k = 0
n = int(get_number())
while k ** 2 <= n:
    k += 1

print('k = ', k - 1)
