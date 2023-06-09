''''
#Задача 2: Найдите сумму цифр трехзначного числа.
#*Пример:*
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) 
'''
number = int(input('Введите трехзначное число: '))
print(f'Сумма чисел трехзначного числа {number} равна {int(number%10 + ((number%100)//10) + number//100)}')

'''
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*
6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10
'''

total = int(input('Введите количество журавликов, которые сделали дети: '))
if total >= 4:
    i = total //6
    print(f'Петя сделал {i} журавлик(-ов), Сережа - {i}, Катя - {i*4}')
else:
    print('Введите количество журавликов больше или равно четырем')
'''
Задача 6: Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*
385916 -> yes
123456 -> no
'''
numberTicket=str(input('Введите шестизначный номер билета: '))
summ1 = int(numberTicket[0]) + int(numberTicket[1]) + int(numberTicket[2])
summ2 = int(numberTicket[3]) + int(numberTicket[4]) + int(numberTicket[5])
if summ1 == summ2:
    print('Билет счастливый')
else:
    print('Нет')
 
'''   
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
отломить k долек, если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no
'''
size1 = int(input('Введите количество долек шоколадки по горозонтали: '))
size2 = int(input('Введите количество долек шоколадки по вертикали: '))
number = int(input('Введите какое число долек вы хотите отломить: '))
if size1 == number or size2 == number or number == (size1-1)*size2 or number == (size2-1)*size1:
    print('Можно отломить за один раз')
else:
    print('Нельзя отломить за один раз')
