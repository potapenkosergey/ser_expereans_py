# TODO Поключаемый модуль, выполнение функций, файла module_13_03.
from new_package import module_13_03

print('Напишите свой простой класс исключений')
name = input('Введите логин(правильный логин serg.7777):')
module_13_03.f_login(name)

print('В примере работы декорированых функций вызвать функции с одинаковыми '
      'последовательностями и одинковыми числами для поиска - и сравнить какой '
      'метод работы в выигрше по првемени')
print(f"Первый линейный поиск занимает {module_13_03.compare1} , второй "
      f"линейный "
      f"поиск "
      f"{module_13_03.compare1} секунд на " f""
      f"{module_13_03.compare1-module_13_03.compare2} "
      f"секунд "
      f"меньше")
print('Напишите функцию используя обрабатку исключений, которая запрашивает '
      'ввод двух значений.Если хотя бы одно из них не является числом, то'
      ' должна выполняться конкатенация')
module_13_03.tapeerror()
print(help(module_13_03))
