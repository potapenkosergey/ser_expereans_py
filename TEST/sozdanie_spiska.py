# создание списка
my_super_list = [1, 2, 3, 4, 5]
print(my_super_list)

# тип элиментом списка
my_list = [1, 1.4, "name", [1, 2, 3]]
for element in my_list:
    print(type(element), element)

# индекс
my_list.index(1.4)

# сортировка
a = [3, 7, 1, 15]
print(sorted([3, 7, 1, 15]))
a.sort()
print(a)
