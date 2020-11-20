import sys

# Версия Python: 3.8(32-bit)
# Разрядность ОС: 64


def show(*mass, ids=None, sum_memory=0):                         # устанавливаю атрибут для расчета суммы занятой памяти
    # print(f'{type(x)=}, {sys.getsizeof(x)=}, {x=}', )

    for x in mass:
        # if ids is None:                                        # неудачная попытка исключить повторы
        #     ids = set()
        # obj_id = id(x)
        # if obj_id in ids:
        #     return 0
        # ids.add(obj_id)
                                                                 # нагло сдираю код с урока
        if hasattr(x, '__iter__'):
            if hasattr(x, 'items'):
                for k, v in x.items():
                    show(k)
                    sum_memory += sys.getsizeof(k)               # и использую его в своих нуждах для подсчета суммы
                    show(v)
                    sum_memory += sys.getsizeof(y)
            elif not isinstance(x, str):
                for item in x:
                    show(item)
                    sum_memory += sys.getsizeof(item)
        sum_memory += sys.getsizeof(x)
    return sum_memory


#######################################################################################################################
# ЗАДАЧА 1
'''Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
'''

n = int(input('Введите количество элементов:'))

a = 1
b = 1
i = 1

while i < n:
    a = a / 2
    if i % 2 == 0:
        b += a
    else:
        b -= a
    i += 1

# print(b)
print('Задача 1')
print(show(b, a, i, n))  # при n = 5 занимаемая память переменных равняется 60. При n = 100000000, память = 64
print(show(b, a, i,))    # без n занимаемая память равна 46. В обоих вариантах с изменением n значение занимаемой памяти
                         # не меняется, либо меняется незначительно. Выходит плохую задачу выбрала, с float-ами.
                         # Пробуем другую)


#######################################################################################################################
# ЗАДАЧА 2
x = int(input('Какую цифру искать?'))
n = int(input('Сколько чисел введешь?'))


def find_count(x, n, c=0):
    while n > 0:
        a = int(input('Введите число:'))
        while a > 0:
            for i in str(a):
                if int(i) == x:
                    c += 1
            else:
                break
        return find_count(x, n - 1, c)
    print(c)


# find_count(x, n)
print('Задача 2')
print(show(find_count, x, n))   # Занимаемая память = 96. Не уверена, что хорошая идея затолкать функцию.
                                # Но навеяно из общения в чатиках) Минус - скорее всего дважды считает переменные x,n


#######################################################################################################################
# ЗАДАЧА 3
'''В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''

count_ls = []
c = 0

for i in range(2, 9 + 1):
    for j in range(2, 99 + 1):
         if j % i == 0:
             c += 1
    count_ls.append(c)
    c = 0

#for i in range(0, len(count_ls)):
    #print(f'для числа {i+2} найдено {count_ls[i]} кратных чисел')


print('Задача 3')
print(f'Начальный вариант {show(count_ls, c, i)}')           # Занимаемая память = 198.
print(f'Вариант с кортежем {show(tuple(count_ls), c, i)}')   # Пробуем сделать из списка кортеж. Занимаемая память = 190. Не очень большая выгода
print(f'только кортеж {show(tuple(count_ls))}')              # 164. Что ж. Ну ладно
print(f'только список {show(count_ls)}')                     # 172.
print(f'Вариант с множеством {show(set(count_ls), c, i)}')   # Пробуем сделать из списка множество. Занимаемая память = 502.
