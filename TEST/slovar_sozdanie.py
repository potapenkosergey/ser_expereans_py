# Создание пустого словаря:
student = {}
student1 = dict()
# Запись в словарь
student2 = {'name': "Sergey", 'age': 12, 'mon': "Lida", }
print(student2)
# Запись через функцию dict
d = dict(short='dict', long='dictionary')
print(d)
# Запись в словарь списка кортежей:
d = dict([(1, 1), (2, 4)])
print(d)
# Метод fromkeys
d = dict.fromkeys(['a', 'b'])
print(d)
d = dict.fromkeys(['a', 'b'], 100)
print(d)









