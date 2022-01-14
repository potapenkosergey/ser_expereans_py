# TODO Поключаемый модуль, выполнение функций, файла sort_module_13_01.
import sort_module_13_01

list_1 = [52, 155, 26, 3, 2, 88, 45, 22, 11, 104, 0, 1]

print('До сортировки', list_1)
print('Cортировка методом пузырька:', sort_module_13_01.bubble_sort(list_1))
print('Сортировка методом камня:', sort_module_13_01.sort_stone_method(list_1))
print('Сортировка методом вставки:', sort_module_13_01.insert_sort_method(
    list_1))
# print(help(sort_module))
