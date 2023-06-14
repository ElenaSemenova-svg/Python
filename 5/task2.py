# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму 
# двух целых неотрицательных чисел. Из всех арифметических операций 
# допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

first_number = abs(int(input('Введите первое число: ')))
second_number = abs(int(input('Введите второе число: ')))

def summa_number(first_number, second_number):
    if first_number == 0:
        return second_number
    else:
        return summa_number(first_number - 1, second_number + 1)
    
print(summa_number(first_number, second_number))