#NORMAL
# Задание-1:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import random
o = open('zuzzamen.txt', 'w')
b = [random.randint(0, 9) for i in range(2500)]
print(b)
for i in b:
    i = str(i)
    o.write(i)
o.close()

reard = open('zuzzamen.txt', 'r')
line = reard.read()
renum = ""
maxsr = ""
longsr = ""
for num in line:
    if num == renum:
        maxsr += num
        if len(maxsr) > len(longsr):
            longsr = maxsr
    else:
       maxsr = num
       renum = num
print('Саммая длинная последовательность цифр', len(longsr))

# Задание-2
# Сформировать квадратную матрицу, в каждой строке которой находится ровно один ноль на случайном месте, остальные элементы тоже рандомные. Пользователь вводит размер
import pprint
a = int(input('Введите размер матрицы:'))
matrix = [[random.randint(1,9) for i in range(a)] for j in range(a)]
for j in matrix:
    j[random.randint(0,a - 1)] = 0
pprint.pprint(matrix)




























#print('Вычисление стоимости покупки с учетом скидки')
#a = int(input('Введиту сумму покупкии нажмите enter:'))
#if a >= 1000:
#    b = a / 100 * 10
#    c = a - b
#    print("Вам предоставляется скидка 10%")
#    print('Сумма покупки с учетом скидки:', c)
#else:
#    print('Вам не предоставляется скидка, извините')