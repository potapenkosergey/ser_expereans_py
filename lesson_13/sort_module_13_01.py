# TODO Модуль методов сортировок: пузырька, камня, вставки.

__all__ = ["bubble_sort", "sort_stone_method", "insert_sort_method"]


def bubble_sort(array):
    """
    Функция сортировки методом пузырька:
    """
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 2, i - 1, -1):
            if array[j + 1] < array[j]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def sort_stone_method(array):
    """
    Функция сортировки методом камня:
    """
    # определим длину массива
    lenghth = len(array)
    # внешний цикл, кол-во проходов N-1
    for i in range(lenghth):
        # внутренний цикл,N-i-1 проходов
        for j in range(0, lenghth - i - 1):
            # меняем эл-ты местами
            if array[j] < array[j + 1]:
                # temp = array[j]
                # array[j], = array[j+1]
                # array[j], array[j+1] = array[j+1], array[j]
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def insert_sort_method(nums):
    """
    Функция сортировки методом вставки:
    """
    # сортируем со второго эл-та
    # считается что первый эл-т отсортирован
    # print(nums)
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # сылка на индекс предыдущего эл-та
        j = i - 1
        # элемент отсортирован и перемещен вперед
        # если он больше ел-та вставки
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
            # вставляем эл-т
        nums[j + 1] = item_to_insert

    return nums


if __name__ == "__main__":
    pass
