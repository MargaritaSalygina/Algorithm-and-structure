'''Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
 Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой – не больше медианы.Задачу можно решить без сортировки исходного массива. Но если это слишком
сложно, то используйте метод сортировки, который не рассматривался на уроках.

'''
import random

START = 0
END = 50
SIZE = 10

array = [2 * (random.randint(START, END)) + 1 for _ in range(SIZE)]
print(array)


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heap_sort_with_mediana(arr):    # взяла хип сорт
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr, arr[(len(arr) - 1) // 2]


print(heap_sort_with_mediana(array))