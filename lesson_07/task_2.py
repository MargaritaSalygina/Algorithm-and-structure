'''Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
 на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''
import random

START = 0
END = 50
SIZE = 10

array = [round(random.random() * END, 3) for _ in range(SIZE)]
print(array)


def merge_sort(arr):
    len_arr = len(arr)
    if len_arr > 2:
        first = merge_sort(arr[:len_arr//2])
        second = merge_sort((arr[len_arr//2:]))
        arr = first + second
        lst = len(arr) - 1

        for i in range(lst):
            min_num = arr[i]
            min_index = i

            for j in range(i + 1, lst + 1):
                if min_num > arr[j]:
                    min_num = arr[j]
                    min_index = j

            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]

    elif len(arr) > 1 and arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
    return arr


print(merge_sort(array))
