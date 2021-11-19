# TODO Выcокостный год
print("Введите год")
year = int(input(""))
if (year > 1900) and (year < 1000000):
    print("Заданный год верный")
else:
    print("Заданный год не верный")

if (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
    print(year, "Год высокостный")
else:
    print(year, "Год не высокостный")



