'''В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.
'''
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
max_num = 0

for i in array:     # устанавливаем в переменную max_num отрицательное значение
    if i < 0:
        max_num = i

for i in range(0, len(array) - 1):
    if (max_num < array[i]) and (array[i] < 0):
        max_num = array[i]
    elif (max_num < array[i + 1]) and (array[i + 1] < 0):
        max_num = array[i + 1]
print(f'Максимальное отрицательное число {max_num}, на позиции {array.index(max_num)}')



