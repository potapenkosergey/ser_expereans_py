# TODO Поключаемый модуль, выполнение функций, файла module_13_02.
from new_package import module_13_02

print("Функция должна проверить есть ли в списке 2 числа сума которых "
      "еквивалентна числу переданому 2 м параметром.")
print(module_13_02.my_scroll1)
print(module_13_02.my_spisok1)
print(module_13_02.function1(module_13_02.my_scroll1, module_13_02.my_spisok1))

print('Написать анонимную функцию которая приниммает 2 значения x,y  где y по'
      'умолчанию == числу . Результат работы функции - число x  в степени y.')
print(module_13_02.my_spisok)
print(module_13_02.my_function)

print('создать функцию генератор ПРОСТЫХ чисел в дипазоне заданых 2-мя '
      'аргументами чисел.')
module_13_02.prime_numbers(100)
# print(help(module_1))
