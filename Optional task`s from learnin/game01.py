import random
b = random.randint(1, 100)
print(b)
while True:
    a = int(input('Введите любое число от 1 до 100:'))
    if a == b:
        print("Вы угадали число! Поздравляем!")
        break
    else:
        print("Вы не угадали число! Попробуйте еще раз")