# TODO Pyramid
meaning = int(input(" Введите число от 3 до 9: "))
# Проверка на правильность введеного числа
if (meaning < 10) and (meaning >= 3):
    # Основной цикл программы
    for i in range(1, meaning + 1):
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()
else:
    print("Введенное число не соответствет диапазону")
