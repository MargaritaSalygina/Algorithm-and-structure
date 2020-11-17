'''В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
max_num = array[0]
min_num = array[0]

for i in range(0, len(array) - 1):   # нахождение максимального числа
    if max_num < array[i + 1]:
        max_num = array[i + 1]

for i in range(0, len(array) - 1):   # нахождение минимального числа
    if min_num > array[i + 1]:
        min_num = array[i + 1]

print(max_num)
#print(max(array))
print(min_num)
#print(min(array))

# нахожу позицию максимального и минимального числа
a = array.index(min_num)
b = array.index(max_num)

# обмен значений
array[a], array[b] = max_num, min_num

print(array)