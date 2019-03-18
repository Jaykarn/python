#Задание-1:
#Пользователь вводит число определите, является ли данное число простым. Делится только на себя и на единицу
n = int(input("Введите число, чтобы узнать простое ли оно: "))
b = 0
for i in range(1, n + 1):
    if n % i == 0:
        b += 1

if b == 2:
    print("Число простое")
else:
    print("Число не простое")


num = int(input("Input num: "))

#Задание-2
#Найдите n-ое число Фибоначчи
a = int(input("введите число 1: "))
b = int(input("введите число 2: "))

n = input("Номер  ряда Фибоначчи: ")
n = int(n)

i = 0
while i < n - 2:
    c = a + b
    a = b
    b = c
    i = i + 1
print(b)

#Задание-3
#Вывести на экран:
#AAABBBAAABBBAAABBB
#BBBAAABBBAAABBBAAA
#AAABBBAAABBBAAABBB
#(таких строк n, в каждой строке m троек AAA)
