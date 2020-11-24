'''Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
 [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
  По возможности доработайте алгоритм (сделайте его умнее).
'''
import random

START = -100
END = 100
SIZE = 10

array = [random.randint(START, END) for _ in range(SIZE)]
print(array)


def bubble_sort(arr):
    flag = True       # добавляем остановку по готовности, чтобы не проходить отсортированную часть
    n = 1
    while n < len(arr):
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] > arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                flag = False
        n += 1
        if flag:
            break

    return arr


print(bubble_sort(array))

