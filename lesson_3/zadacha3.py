# TODO Выcокостный год
print("Введите год для проверки")
year = int(input(""))
if year <= 1900:
    print("Введенный год не отвечает условиям")
elif year >= 1000000:
    print("Введенный год не отвечает условиям")
elif (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
    print(year, "Год високосный")
else:
    print(year, "Год не високосный")




