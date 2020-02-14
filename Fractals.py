from turtle import *
# Project: Fractals.
# Members: Vladimir Silkachev 40%, Vinnikov Alexandr 40%, Popov Kirill 20%
print('Выберите что хотите увидеть:\n 1-Снежинка Коха\n 2-Фрактал Коха\n 3-Дракон\n'
      ' 4-Бинарное дервево\n(введите число)')
chose = int(input())


def Koh_Snow(a,b):
    def tubick(a,b):
        if a == 0:
            forward(b)
        else:
            tubick(a - 1, b / 3)
            left(60)
            tubick(a - 1, b / 3)
            right(120)
            tubick(a - 1, b / 3)
            left(60)
            tubick(a - 1, b / 3)
    for _ in range(3):
        tubick(4,200)
        right(120)


def Koh(a, b):
    if a == 0:
        forward(b)
    else:
        Koh(a - 1, b / 3)
        left(60)
        Koh(a - 1, b / 3)
        right(120)
        Koh(a - 1, b / 3)
        left(60)
        Koh(a - 1, b / 3)


def dragon(num,long):
    speed(100)
    # функция, которая возвращает набор поворотов для дракона, чтобы мы могли пройти в обратном напровлении
    def revers(lst):
          otpt = []
          for i in lst:
                otpt.append(-1 * i)
          otpt.reverse()
          return otpt

    # функция, которая склеивает [набор повортов предыдущего дракона] + [поворто направо] +
    # [набор поворотов в обратном направвлении]
    def drago(n):
          if n == 0:
                return []
          return drago(n-1) + [1] + revers(drago(n-1))

    # рисуем дракона по набору повортов
    forward(long / (num + 1))
    for i in drago(num):
          right(90*i)
          forward(long / (num + 1))

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
if chose != 4:
    b = int(input('Введите размер'))
if chose == 1:
    Koh_Snow(a, b)
if chose == 2:
    Koh(a, b)
if chose == 3:
    dragon(a, b)
if chose == 4:
    left(90)
    tree(a)

done()
