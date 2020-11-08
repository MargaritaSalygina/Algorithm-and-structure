'''Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3
четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''


n = int(input('Введите число:'))
# even_1 = []          это все только для проверки!)
# not_even_1 = []


def f_rec(n, even=0, not_even=0):
    while n > 0:
        if (n % 10) % 2 == 0:
            # even_1.append(n % 10)
            even += 1
        else:
            # not_even_1.append(n % 10)
            not_even += 1
        return f_rec(n // 10, even, not_even)
    print(f'Четных чисел {even}, нечетных {not_even}')


f_rec(n)
