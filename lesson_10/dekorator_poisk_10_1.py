# TODO Декоратор, счётчик выполнения.
import random
def benchmark(function):
    """Декоратор время выполнения функции"""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        function(*args, **kwargs)
        end = time.time()
        return_value = end-start
        print('Время выполнения: {} секунд.'.format(end-start))
        return return_value
    return wrapper
#вызываем функции для сравнения linear_search_1 и linear_search_2
@benchmark
def linear_search_1(sequence1, look_for1):
    i = 0
    length1 = len(sequence1)
    while i < length1 and look_for1 != sequence1[i]:
        i += 1
    return i if i < length1 else None
#вызывае рандомный список для сравниния функций
random_spisok = [random.randint(1,1000000000)for i in range(1000000)]+[1000]
random_number = 1000
compare1 = linear_search_1(random_spisok, random_number)
@benchmark
def linear_search_2(sequence2, look_for2):
    k = 0
    sequence2.append(look_for2)
    lenght2 = len(sequence2)-1
    while look_for2 != sequence2[k]:
        k += 1
    return k if k < lenght2 else None
compare2 = linear_search_2(random_spisok, random_number)
print(f"Первый вариант поиска занимает {compare1} , второй вариант поиска "
      f"{compare2} на " f"{compare1-compare2} секунд меньше.")
