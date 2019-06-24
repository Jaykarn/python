#HARD

# Задание-1
# Куб состоит из n^3 прозрачных и непрозрачных элементарных кубиков. Имеется ли хотя бы один просвет по каждому из трех измерений?
# Если это так, вывести координаты каждого просвета. Куб задается трехмерной матрицей из 0 и 1.
import random
import pprint
n = int(input('введите размер куба:'))
coub = [[[random.randint(0, 1) for a in range(n)] for a in range(n)] for a in range(n)]
pprint.pprint(coub)

# Задание-2
# Дан pwd.txt с логинами и паролями. Найдите топ10 самых популярных паролей.
#
import re
text = open('pwd.txt', 'r')
line = text.read()
new_pass = {}
passwords = re.findall(r';(\w+)', line)
print(passwords)
for i in passwords:
    print(i)
    if passwords.count(i) > 1:
        new_pass[i] = passwords.count(i)
print(new_pass)
new_pass = sorted(new_pass.items(), key=lambda item: item[1], reverse=True)
i = 0
for password in new_pass[:10]:
    print('топ', i + 1, 'пароль:', password)
    i += 1
# Задание-3
# Пользователь вводит положительное целое число больше 1
# Нужно создать квадратную матрицу этого размера и по спирали заполнить её числами
# 5
#  1  2  3  4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

# 3
# 1 2 3
# 8 9 4
# 7 6 5
import pprint
a = int(input('Введите размер матрицы:'))
matrix = [[random.randint(1,9) for i in range(a)] for j in range(a)]
for j in matrix:
    j[random.randint(0,a - 1)] = 0
pprint.pprint(matrix)
