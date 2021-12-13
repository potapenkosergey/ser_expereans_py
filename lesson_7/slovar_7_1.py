# TODO Создание списка, reversed
# Создание списка случайных целых чисел:
from random import randint
numbers = [randint(0, 10) for i in range(10)]
print(numbers)
# Уникальные числа в списке:
unique_numbers = list(set(numbers))
print(unique_numbers)
# Элементы списка в обратном порядке, кортеж:
unique_numbers = tuple(reversed(unique_numbers))
print(unique_numbers)
