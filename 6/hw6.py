# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

f_number = int(input('Введите первый элемент: '))
n = int(input('Введите количество элементов: '))
const = int(input('Введите константу: '))
list_numbers = []

for i in range(1, n + 1):
     list_numbers.append(f_number  + (i - 1)*const)
print(list_numbers)

#Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
from random import randint

list_numbers = []
min_number = int(input('Введите минимальное число: '))
max_number = int(input('Введите максимальный число: '))

for _ in range(10):
    list_numbers.append(random.randint(1, 10))
print(list_numbers)

list_index = []
for i in range(len(list_numbers)):
    if min_number <= list_numbers[i] >= max_number:
        list_index.append(i)
print(list_index)


