# TODO Создание списков и операции с ними

nums = [5, 10, 1, 60, 25, 3]
print("Список из чисел:", nums)
print("Длина списка", len(nums))
print("Первый элемент:", nums[0])
print("Последний элемент:", nums[-1])
print("Наиболшее значение:", max(nums))
print("Наименьшее значение:", min(nums))
print("Сумма:", sum(nums))
print("Список в обратном порядке:", list(reversed(nums)))
print("По возрастанию значений:", sorted(nums))
print("По убыванию значений", sorted(nums, reverse=True))
print("Исходный текст", nums)
nums[1] = "Текст"
print("После внесения изменений:", nums)
print("Получение среза:", nums[1: len(nums)-1])
nums[1:-1]=["A","B"]
print("После замены элементов:", nums)
nums = list(range(5, 11))
print("Список чисел от 5 до 10", nums)
nums[2:4]=[]
print("После удаления двух элементов", nums)
del nums[len(nums)-1]
print("Удалён последний элемент", nums)
nums = [2*k+1 for k in range(5)]
print("Нечётный числа", nums)
symbs =list("Python")
print("Список из симвалов:", symbs)
print("Два первых символа:", symbs[:2])
print("Остальные символы", symbs[2:])




