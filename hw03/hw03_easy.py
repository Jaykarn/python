# EASY

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
def a(n, ndigits=0):
    b = 10 ** ndigits
    n = b * n
    e = int(n + 1) / b
    d = int(n) / b
    d = str(d)
    print(type(d))
    if int((n * 10) % 10) >= 5:
        if e == '.0':
            print(e[-2:])
        else:
            return e
    else:
        if d >= 1:
            print(d[-2:])
        else:
            return d[-2:]

print(a(0.9939567, 3))
print(a(10, 4))
print(a(0.9939567, 8))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
def lucky(s):
    t = tuple(map(int, s))
    n = len(s) // 2
    if sum(t[:n]) == sum(t[n:]):
        return 'счастливый'
    else:
        return 'не счастливый'

a = str(121212)
d = lucky(a)
print('Ваш билет', d)

