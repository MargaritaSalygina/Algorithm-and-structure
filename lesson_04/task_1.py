'''В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import timeit
import cProfile
# ВЫВОД
# На мой взгляд, во всех трех вариантах прослеживается линейная сложность.
# Первый вариант (домашка) оказался самым долгим.
# Во втором варианте я обернула куски кода в функцию, в надежде, что будет работать дольше.
# К удивлению, второй вариант отработал быстрее первого и третьего варианта, написаного на встроенных min max функциях.
# Профайлер оказался не очень информативным в моем случае и,
# по больше части, указывал на проблему в генерации списка случайных чисел.
#
#
#


#######################################################################################################################
# ВАРИАНТ 1
# 0.006366200000000002
# 0.02020749999999999
# 0.16787080000000004
# 18.8796098


first = '''
import random

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
#print(array)
max_num = array[0]
min_num = array[0]

for i in range(0, len(array) - 1):   # нахождение максимального числа
    if max_num < array[i + 1]:
        max_num = array[i + 1]

for i in range(0, len(array) - 1):   # нахождение минимального числа
    if min_num > array[i + 1]:
        min_num = array[i + 1]

#print(max_num)
#print(min_num)

# нахожу позицию максимального и минимального числа
a = array.index(min_num)
b = array.index(max_num)

# обмен значений
array[a], array[b] = max_num, min_num

#print(array)

'''

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
print(timeit.timeit(first, number=100, globals=globals()))  # 0.006366200000000002
cProfile.run(first)
'''
    59 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:2(<module>)
        1    0.000    0.000    0.000    0.000 <string>:4(<listcomp>)
       10    0.000    0.000    0.000    0.000 random.py:200(randrange)
       10    0.000    0.000    0.000    0.000 random.py:244(randint)
       10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       11    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
'''
print('*' * 100)

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 1000
print(timeit.timeit(first, number=100, globals=globals()))  # 0.02020749999999999
cProfile.run(first)
'''        512 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:2(<module>)
        1    0.000    0.000    0.000    0.000 <string>:4(<listcomp>)
      100    0.000    0.000    0.000    0.000 random.py:200(randrange)
      100    0.000    0.000    0.000    0.000 random.py:244(randint)
      100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      104    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}'''
print('*' * 100)

SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 10000
print(timeit.timeit(first, number=100, globals=globals()))  # 0.16787080000000004
cProfile.run(first)
''' 5690 function calls in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:2(<module>)
        1    0.001    0.001    0.003    0.003 <string>:4(<listcomp>)
     1000    0.001    0.000    0.002    0.000 random.py:200(randrange)
     1000    0.001    0.000    0.003    0.000 random.py:244(randint)
     1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1682    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
'''
print('*' * 100)

SIZE = 100000
MIN_ITEM = 0
MAX_ITEM = 1000000
print(timeit.timeit(first, number=100, globals=globals()))  # 18.8796098
cProfile.run(first)
'''504817 function calls in 0.330 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.047    0.047    0.330    0.330 <string>:2(<module>)
        1    0.047    0.047    0.280    0.280 <string>:4(<listcomp>)
   100000    0.088    0.000    0.179    0.000 random.py:200(randrange)
   100000    0.054    0.000    0.233    0.000 random.py:244(randint)
   100000    0.062    0.000    0.091    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.330    0.330 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   100000    0.012    0.000    0.012    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   104809    0.016    0.000    0.016    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.002    0.001    0.002    0.001 {method 'index' of 'list' objects}
'''
print('*' * 100 + 'ВАРИАНТ 2')












#######################################################################################################################
# ВАРИАНТ 2
# 0.001255400000001572
# 0.012639000000000067
# 0.17029359999999727
# 14.031134899999998



second = '''
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
#print(array)


def max_num(array):
    max_num = array[0]
    for i in range(0, len(array) - 1):   # нахождение максимального числа
        if max_num < array[i + 1]:
           max_num = array[i + 1]
    return max_num


def min_num(array):
    min_num = array[0]
    for i in range(0, len(array) - 1):   # нахождение минимального числа
        if min_num > array[i + 1]:
             min_num = array[i + 1]
    return min_num


def mm(array):
    a = array.index(min_num(array))
    b = array.index(max_num(array))
    array[a], array[b] = array[b], array[a]
    return array


#print(mm(array))
'''


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
print(timeit.timeit(second, number=100, globals=globals()))  # 0.001255400000001572
cProfile.run(second)
'''
         56 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:2(<listcomp>)
        1    0.001    0.001    0.001    0.001 <string>:2(<module>)
       10    0.000    0.000    0.000    0.000 random.py:200(randrange)
       10    0.000    0.000    0.000    0.000 random.py:244(randint)
       10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       12    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

'''
print('*' * 100)

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 1000
print(timeit.timeit(second, number=100, globals=globals()))  # 0.012639000000000067
cProfile.run(second)
'''  506 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:2(<listcomp>)
        1    0.000    0.000    0.000    0.000 <string>:2(<module>)
      100    0.000    0.000    0.000    0.000 random.py:200(randrange)
      100    0.000    0.000    0.000    0.000 random.py:244(randint)
      100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      102    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
'''
print('*' * 100)

SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 10000
print(timeit.timeit(second, number=100, globals=globals()))  # 0.17029359999999727
cProfile.run(second)
''' 5622 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:2(<listcomp>)
        1    0.000    0.000    0.003    0.003 <string>:2(<module>)
     1000    0.001    0.000    0.002    0.000 random.py:200(randrange)
     1000    0.001    0.000    0.003    0.000 random.py:244(randint)
     1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1618    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
'''
print('*' * 100)

SIZE = 100000
MIN_ITEM = 0
MAX_ITEM = 1000000
print(timeit.timeit(second, number=100, globals=globals()))  # 14.031134899999998
cProfile.run(second)
''' 504859 function calls in 0.285 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.050    0.050    0.285    0.285 <string>:2(<listcomp>)
        1    0.000    0.000    0.285    0.285 <string>:2(<module>)
   100000    0.090    0.000    0.181    0.000 random.py:200(randrange)
   100000    0.054    0.000    0.235    0.000 random.py:244(randint)
   100000    0.062    0.000    0.091    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.285    0.285 {built-in method builtins.exec}
   100000    0.013    0.000    0.013    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   104855    0.016    0.000    0.016    0.000 {method 'getrandbits' of '_random.Random' objects}
'''
print('*' * 100)










######################################################################################################################
# ВАРИАНТ 3
# 0.001368999999996845
# 0.012546999999997865
# 0.16650860000000023
# 14.564998699999997

third = """
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)

a = array.index(max(array))
b = array.index(min(array))

array[a], array[b] = array[b], array[a]

# print(array)
"""

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
print(timeit.timeit(third, number=100, globals=globals()))  # 0.001368999999996845
cProfile.run(third)
'''       61 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:2(<listcomp>)
        1    0.001    0.001    0.002    0.002 <string>:2(<module>)
       10    0.000    0.000    0.000    0.000 random.py:200(randrange)
       10    0.000    0.000    0.000    0.000 random.py:244(randint)
       10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       13    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
'''
print('*' * 100)

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 1000
print(timeit.timeit(third, number=100, globals=globals()))  # 0.012546999999997865
cProfile.run(third)
'''   508 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:2(<listcomp>)
        1    0.000    0.000    0.000    0.000 <string>:2(<module>)
      100    0.000    0.000    0.000    0.000 random.py:200(randrange)
      100    0.000    0.000    0.000    0.000 random.py:244(randint)
      100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      100    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
'''
print('*' * 100)

SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 10000
print(timeit.timeit(third, number=100, globals=globals()))  # 0.16650860000000023
cProfile.run(third)
''' 5687 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:2(<listcomp>)
        1    0.000    0.000    0.003    0.003 <string>:2(<module>)
     1000    0.001    0.000    0.002    0.000 random.py:200(randrange)
     1000    0.000    0.000    0.002    0.000 random.py:244(randint)
     1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1679    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
'''
print('*' * 100)

SIZE = 100000
MIN_ITEM = 0
MAX_ITEM = 1000000
print(timeit.timeit(third, number=100, globals=globals()))  # 14.564998699999997
cProfile.run(third)
''' 504816 function calls in 0.276 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.045    0.045    0.270    0.270 <string>:2(<listcomp>)
        1    0.000    0.000    0.275    0.275 <string>:2(<module>)
   100000    0.085    0.000    0.173    0.000 random.py:200(randrange)
   100000    0.052    0.000    0.225    0.000 random.py:244(randint)
   100000    0.059    0.000    0.088    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.276    0.276 {built-in method builtins.exec}
        1    0.002    0.002    0.002    0.002 {built-in method builtins.max}
        1    0.002    0.002    0.002    0.002 {built-in method builtins.min}
   100000    0.012    0.000    0.012    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   104808    0.016    0.000    0.016    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.001    0.000    0.001    0.000 {method 'index' of 'list' objects}
'''
print('*' * 100)


