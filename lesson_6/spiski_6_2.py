# TODO Список, добавление элемента, сдвиг в право.
# Генератор случайных чисел random, создание списка:
from random import randint
number_list = [randint(1, 10) for x in range(10)]
print("Созданный список:", number_list)
k, c = [int(s) for s in input("Введите через пробел, от 0 до 10 индекс k, "
                              "и числовое значение 'C'").split()]
# Метод append добавление элемента в список:
number_list.append(0)
for i in range(len(number_list) - 1, k, -1):
    number_list[i] = number_list[i - 1]
number_list[k] = c
number_list = [print(number_list[i], end=' ')for i in range(len(number_list))]


