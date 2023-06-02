# Задача 16: Требуется вычислить, сколько раз встречается некоторое 
# число X в массиве A[1..N]. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

import random
from random import randint

number = int(input('Введите число: '))
list_numbers = []

for _ in range(10):
    list_numbers.append(random.randint(1, 10))
print(list_numbers)

count = 0
for i in range(len(list_numbers) - 1):
    if  number == list_numbers[i]:
        count +=1
print(f'Число {number} встречается {count} раз')