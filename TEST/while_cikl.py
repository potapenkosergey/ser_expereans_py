# while Цикл с предусловием:
i = 1
while i <= 10:
    print(i)
    i += 1
# Остановка повторяющегося цикала break:
i = 1
while i <= 10:
    print(i)
    i += 1
    break
# Прерывание цикла continue:
i = 1
while i <= 10:
    if i != 5:
        print(i)
    i += 1
    continue
