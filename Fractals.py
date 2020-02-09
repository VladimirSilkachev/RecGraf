from turtle import *
print('Выберите что хотите увидеть:\n 1-Снежинка по Коху\n 2-Ледяные фракталы\n 3-Дракон\n'
      ' 4-Бинарное дервево\n 5- НЕ ЗАБЫТЬ ВСТАВИТЬ НАЗВАНИЕ\n(введите число)')
chose = input()


def snow(order, n):
    if order == 0:
        forward(n)
    else:
        snow(order - 1, n / 3)
        left(60)
        snow(order - 1, n / 3)
        right(120)
        snow(order - 1, n / 3)
        left(60)
        snow(order - 1, n / 3)
    for _ in range(3):
        snow(4, 240)
        right(120)

def ice():
    pass

def dragon():
    pass

def tree():
    pass

def kirill_func():
    pass
a = input('Введите глубину фрактала')
b = input('Введите размер')
if chose == 1:
    snow(a,b)
if chose == 2:
    ice(a,b)
if chose == 3:
    dragon(a,b)
if chose == 4:
    tree(a,b)
if chose == 5:
    tree(a,b)
done()