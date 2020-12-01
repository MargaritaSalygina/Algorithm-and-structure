'''Определить количество различных подстрок с использованием хеш-функции. Задача: на вход функции дана строка,
требуется вернуть количество различных подстрок в этой строке.Примечание: в сумму не включаем пустую строку и
строку целиком.
'''
import hashlib


def sub_count(s):
    l = len(s)
    hash_counter = []
    for i in range(l):
        if i == 0:
            l = len(s) - 1
        else:
            l = len(s)
        for j in range(l, i, -1):
            hash_counter.append(hashlib.sha3_512(s[i:j].encode('utf-8')).hexdigest())
    return len(hash_counter)


print(sub_count('abcd'))

