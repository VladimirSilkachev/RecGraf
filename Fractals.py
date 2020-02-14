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

long = 120
num = 12

# функция, которая вращает набор поворотов для дракона, чтобы мы могли пройти в обратном напровлении
def revers(lst):
      otpt = []
      for i in lst:
            otpt.append(-1 * i)
      otpt.reverse()
      return otpt

# функция, которая склеивает [набор повортов предыдущего дракона] + [поворто направо] + [набор поворотов в обратном направвлении]
def dragon(n):
      if n == 0:
            return []
      return dragon(n-1) + [1] + revers(dragon(n-1))

# рисуем дракона по набору повортов
t.forward(long / (num + 1))
for i in dragon(num):
      t.right(90*i)
      t.forward(long / (num + 1))


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
