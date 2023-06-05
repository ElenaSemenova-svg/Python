# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в 
# обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит 
# сами элементы множеств.

import random
from random import randint

list_numbers_1 = []
list_numbers_2 = []

for _ in range(10):
    list_numbers_1.append(random.randint(1, 10))
print(list_numbers_1)

for _ in range(14):
    list_numbers_2.append(random.randint(-10, 10))
print(list_numbers_2)

list_numbers_1 = set(list_numbers_1)
list_numbers_2 = set(list_numbers_2)

all =sorted(list_numbers_1.intersection(list_numbers_2))
print(all)

