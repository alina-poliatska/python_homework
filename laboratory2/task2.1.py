import re

def reg_n(text):
    return bool(re.match('^[1-9][0-9]*$', text))


def reg_x(text):
    return bool(re.match('^[+-]{0,1}\d*(\.){0,1}\d*$', text))



def get_number(typer,reg,name):
    number = input(name)
    typer = typer+"(number)"
    while not reg(number):
        number = input(name)
    return eval(typer)



n=get_number("int",reg_n,"Введіть n : ")
x=get_number("float",reg_x,"Введіть x : ")
a = 0
b = 0

for i in range(1,n+1):
    a = x/(2**i)
    b +=a
print('Відповідь: ',b)