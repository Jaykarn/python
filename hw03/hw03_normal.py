# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
a = int(input('Введите число из ряда фибоначи с которого необходимо вывести:'))
b = int(input('Введите число из ряда фибоначи до которого необходимо вывести:'))
def fib(n, m):
    a = 1
    b = 1
    c = 0
    l = []
    pinus = 0
    while pinus < m:
        c = a + b
        a = b
        b = c
        pinus = pinus + 1
        if pinus >= n:
            l.append(c)
    return(l)
e = fib(a, b)
print('Ряд фибоначи запрошен от', a, 'до', b, 'и им является:', e)
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

l = [10, 15, 20, 982, 21, 5, 1, 22, 754]
def shmyak(n):
    for i in range(len(n)):
        v = n[i]
        j = i
        while (n[j-1] > v) and (j > 0):
            n[j] = n[j-1]
            j = j - 1
        n[j] = v
        print(n)
    return n

e = shmyak(l)
print(e)