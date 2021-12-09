lst3 = []
for x in [1, 2, 3]:
    lst3.append(x**2)

lst = [x**2 for x in (1, 2, 3)]

print(lst3, lst)


lst3 = []
for x in [1, 2, 3, 4, 5]:
    if x % 2 == 0:
        lst3.append(x**2)

lst = [x**2 for x in (1, 2, 3, 4, 5) if x % 2 == 0]

print(lst3, lst)

