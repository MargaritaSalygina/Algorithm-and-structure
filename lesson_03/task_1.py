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

for i in range(0, len(count_ls)):
    print(f'для числа {i+2} найдено {count_ls[i]} кратных чисел')

