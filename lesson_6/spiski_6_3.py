# TODO Два списка, уникальные числа:
# Генератор случайных чисел random, создание списка:
from random import randint
# Создание переменных для двух списков:
number_list1 = set([randint(1, 10) for x in range(6)])
number_list2 = set([randint(1, 10) for i in range(6)])
print("Созданные списки:", number_list1, number_list2)
# Возвращает длину (количество элементов) в объекте
print("Уникальных чесел в списках: ", len(number_list1 & number_list2))

