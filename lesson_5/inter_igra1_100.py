# TODO The game
# Импорт модулей random, math
from random import random
import math
number = round(random() * 100)
meaning = 1
# Вывод в консоль условия задачи
print("Отгодайте загаданное число от 1 до 100")
# Основной цикл программы
while meaning <= math.inf:
    try:
        u = int(input(str(meaning) + " - я попытка:"))
        if u > number:
            print("Число больше")
        elif u < number:
            print("Число меньше")
        else:
            print("Вы угадали с %d - й попытки" % meaning + " \U0001f646 ")
            break
    except ValueError:
        print("Ошибка, введите число ещё раз")
    meaning += 1


