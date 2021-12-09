names = ["name1", "name2", "name3"]
print(names)
# Добавление в список метод: append
names.append("Попугай")
print(names)
# Удаление последнего элемента: pop
names = ["name1", "name2", "name3"]
names.pop()
print(names)
# Получение индекса, метод: index
names = ["name1", "name2", "name3"]
n = names.index("name2")
print(n)
# Функция длина списка: len
print(len(names))
# Сортировка, метод: sort
numbers = [4, 6, 81, 95, 108, 56]
numbers.sort()
print(numbers)
# Сортировка в обратном порядке: reverse
numbers = [4, 6, 81, 95, 108, 56]
numbers.sort(reverse=True)
print(numbers)
# Замена в списке:
numbers = [4, 6, 81, 95, 108, 56]
numbers[1] = "B"
print(numbers)

