# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть

from random import randint

number = int(input('Введите количество монеток: '))

coin_tails, coin_emblem = 0, 0
for i in range(number):
    temp = randint(0, 1)
    print(temp)
    
    if temp > 0:
        coin_emblem +=1
    else:
        coin_tails +=1
        
if coin_emblem > coin_tails:
        print(f' Общее количество монет {number}, количество монет орлом {coin_emblem}, нужно перевернуть {coin_tails} монет')
else:
        print(f' Общее количество монет {number}, количество монет решкой {coin_tails}, нужно перевернуть {coin_emblem} монет')
    

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

from random import randint

summa = int(input('Введите сумму чисел: '))
dev = int(input('Введете произведение чисел: '))

count = 0

for i in range(summa):
    for j in range(summa):
        if i + j == summa and i * j == dev:
            count += 1
            print(i, j)
                    


# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

from random import randint

number = randint(1, 30)
degree = 0
print(number)

while 2 ** degree <= number:
    print(degree, end='  ') 
    degree +=1