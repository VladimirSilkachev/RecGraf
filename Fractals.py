from turtle import *

print('Выберите что хотите увидеть:\n 1-Снежинка Коха\n 2-Фрактал Коха\n 3-Дракон\n'
      ' 4-Бинарное дервево\n(введите число)')
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
        snow(a, b)
        right(120)


def ice():
    pass


def dragon():
    pass


def tree(a):
    if a >= 1:
        forward(a * 10)
        right(30)
        tree(a * 0.75)
        left(60)
        tree(a * 0.75)
        right(30)
        backward(a * 10)



a = int(input('Введите глубину фрактала'))
if chose != '4':
    b = int(input('Введите размер'))
if chose == 1:
    snow(a, b)
if chose == 2:
    ice(a, b)
if chose == 3:
    dragon(a, b)
if chose == 4:
    left(90)
    tree(a)


done()
