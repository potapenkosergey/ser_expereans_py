# TODO Выcокостный год
print("Введите год для проверки")
year = int(input(""))
if year < 1900:
    print("Введеный год не отвечает условиям")
elif year > 1000000:
    print("Введеный год не отвечает условиям")
elif (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
    print(year, "Год высокостный")
else:
    print(year, "Год не высокостный")




