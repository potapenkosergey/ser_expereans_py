# TODO Список, удаление элемента со сдвигом в лево.
# Генератор случайных чисел random, создание списка:
from random import randint
number = [randint(1, 10) for x in range(10)]
print("Созданный список:", number)
# Цикл for, поиск в созданном списке числа с введённым индексом k:
k = int(input("Введите числовой индекс от 0 до 10 'k' "))
for i in range(k + 1, len(number)):
    number[i - 1] = number[i]
# Метод pop удаление последнего элемента списка:
number.pop()
number = [print(number[i], end=' ')for i in range(len(number))]
