# TODO Поиск числа
n = list(input("Введите натуральное число:"))
print('Да' if len(set(n)) != len(n) else 'Нет')
