# TODO Текст в одной строке, счётчик повторяющихся слов.
# Создание словаря:
counter = {}
# Счётчик повторяющихся слов в строке:
for word in input("Введите через пробел текс одной строкой:").split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')

