# TODO Оператор цикла while
# Считывание верхней границы суммы:
n = int(input("Укажите верхнюю границу суммы:"))
# Начальное значение для суммы:
s = 0
# Начальное значение индексной переменной:
k = 0
# Опереатор цикла для вычесления суммы:
while k < n:
# Увелечение значения инднксной переменной на единицу:
    k = k +1
# Прибавление слагаемого к сумме:
    s = s + k
# Отображение результата:
print("Сумма чисел от 1 до", n, "равна", s)


