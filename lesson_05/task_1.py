'''Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

'''
from collections import defaultdict, Counter

# ВАРИАНТ 1

lst = []
quarter = 4
quant = int(input('Сколько будет компаний? '))
for i in range(quant):
    name = input("Название компании: ")
    for j in range(quarter):
        gain = int(input(f'Выручка за {j + 1} квартал: '))
        lst.append((name, gain))

total = 0
c = defaultdict(list)
for company, gain in lst:
    c[company].append(gain)
    total += gain

avg = total / quant
print(f'Средняя выручка компаний: {avg}.')

for k, v in c.items():
    if sum(v) < avg:
        print(f'Компания "{k}" имеет выручку ниже среднего.')


# ВАРИАНТ 2
# lst = []
# quarter = 4
# quant = int(input('Сколько будет компаний? '))
# for i in range(quant):
#     name = input("Название компании: ")
#     for j in range(quarter):
#         gain = int(input(f'Выручка за {j + 1} квартал: '))
#         lst.append((name, gain))
#
# total = 0
# c = Counter()
# for company, gain in lst:
#     c[company] += gain
#     total += gain
#
# print(c)
#
# for k, v in c.items():
#     if v < (total / quant):
#         print(f'Компания "{k}" имеет выручку ниже среднего.')