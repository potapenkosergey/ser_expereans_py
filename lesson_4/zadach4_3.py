# TODO Поиск цифр стоящих рядом
print("Введите натуральное число")
s = input()
print("Да" if any(str(i)*2 in s for i in range(10)) else "Нет")