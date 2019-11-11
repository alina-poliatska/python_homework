import re
import math


def reg(text):
    return bool(re.match('^\d*(\.){0,1}\d{0,1}$', text))


def number(prompt):
    point_iv = input(prompt)
    while not reg(point_iv):
        point_iv = input(prompt)
    return float(point_iv)


def points():
    input_data = []
    name = ['Кількість балів, що набрав Іванов у першому турі: ', 'Кількість балів, що набрав Іванов у другому турі: ',
            'Кількість балів, що набрав Іванов у третьому турі: ', 'Кількість балів, що набрав Петров у першому турі: ',
            'Кількість балів, що набрав Петров у другому турі: ', 'Кількість балів, що набрав Петров у третьому турі: ',
            'Кількість балів, що набрав Сидоров у першому турі: ', 'Кількість балів, що набрав Сидоров у другому турі: ',
            'Кількість балів, що набрав Сидоров у третьому турі: ']
    for i in name:
        input_data.append(number("Введіть {}".format(i)))
    return input_data


s = points()
Ivanov_sum = sum(s[0:3])
Petrov_sum = sum(s[3:6])
Sidorov_sum = sum(s[6:9])
print('Кількість балів, набрана переможцем: ', max(Ivanov_sum, Petrov_sum, Sidorov_sum))
