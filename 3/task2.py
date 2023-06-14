# Задача 18: Требуется найти в массиве A[1..N] самый близкий 
# по величине элемент к заданному числу X. Пользователь в первой 
# строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка 
# содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
#Мой вариант
# import random
# from random import randint

# number = int(input('Введите число: '))
# list_numbers = []

# for _ in range(10):
#     list_numbers.append(random.randint(1, 10))
# print(list_numbers)

# list_numbers = set(list_numbers)
# list_numbers=list(list_numbers)
# print(list_numbers)

# index = 0
# minimum = abs(number - list_numbers[0])
# for i in range (1, len(list_numbers)):
#     difference = abs(number - list_numbers[i])
#     if difference < minimum:
#         index = i
#         minimum = difference
# print(f'Число {list_numbers[index]} близко к числу {number} ')
   
    
#Вариант преподавателя

import random
from random import randint

number = int(input('Введите число: '))
list_numbers = []

for _ in range(10):
    list_numbers.append(random.randint(1, 100))
print(list_numbers)

nearest = 0
min_dist = float('inf')

for item in list_numbers:
    if abs(number - item) < min_dist: # Модуль числа
        nearest = item
        min_dist = abs(number - item)
    
print(f'Ближайшее Число к {number} будет {nearest}')