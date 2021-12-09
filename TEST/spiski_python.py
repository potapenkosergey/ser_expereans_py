# Создание списка:
spisok = []

numbers = [3, 4, 5, 9, 10]
print(numbers)
numbers = [3, 4, 34.1, "name"]
print(numbers)
numbers = [3, 4, 34.1, [45, 7]]
print(numbers)
# Обращение к именам в списке по индексу:
names = ["name1", "name2", "name3"]
print(names[1])
print(names[-1])
# C помощью for вывести все имена итерируемого объекта:
for i in names:
    print(i)
