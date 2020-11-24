'''В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
(оба являться минимальными), так и различаться.
'''
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
min_num = array[0]
min_num_2 = array[0]

for i in range(0, len(array) - 1):   # нахождение минимального числа
    if min_num > array[i + 1]:
        min_num = array[i + 1]

array.remove(min_num)

for i in range(0, len(array) - 1):   # очевидно. не самое адекватное решение =\
    if min_num_2 > array[i + 1]:
        min_num_2 = array[i + 1]

print(min_num, min_num_2)