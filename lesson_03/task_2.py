'''Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если
индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
'''
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
second_array = []
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# for i in array:
#     if i % 2 == 0:
#         second_array.append(array.index(i))

ter = [second_array.append(array.index(i)) for i in array if i % 2 == 0]
print(second_array)

