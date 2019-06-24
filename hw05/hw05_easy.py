#import random - вызов функции
#import random as r - связка рандома в переменную для вызова по переменной
#from random import randint - вызов определенной функции
#import main2 - импортинг данных из файла рядом
#import os - все что связанно с работой с системой
#os.system("dir") - показать файлы в папке
#os.mkdir('new_folder") - создать папку рядом с файлом
#os.rmdir("new_folder") - удалить папку
#os.remove("data") - удалить файл
# for i in os.listdir(".") - показать все папки в текущей дериктории
#os.path.join() - соединить папка
#os.path.exist() - проверить есть папка или нет. возвращает bool
#.shutil.rmtree() - удалить папку даже если не пустая
#import sys - информация по системе
#os.system("python main2.py") - запуск скрипта
#
#EASY
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# Учесть проверку на то что папка не пуста и на то, что такая папка уже существует
import os
import shutil
#b = 1
#a = int(input('выберите пункт меню:\n'
#              '1.Создать папки\n'
#              '2.Удалить папки'))
#if a == 1:
#    for i in range(1,9):
#        i = str(i)
#        os.mkdir('dir_'+i)
#    print('Папки созданы!')
#if a == 2:
#    for i in range(1,9):
#        i = str(i)
#        g = os.listdir('dir_'+i)
#        print(g)
#        for d in g:
#            while d == 'test.txt':
#                e = print(int(input('папка не пуста. Всеравно хотите удалить все папки?:')))
#                while e == 1:
#                    b = str(b)
#                   shutil.rmtree('dir_' + i)
#                    b = int(b)
#                    b += 1
#                    print('папка с файлом удалена')
#                   d = 0
#                else:
#                    i = str(i)
#                    os.rmdir("dir_" + i)
#                    i = int(i)
#                    i += 1
#                    print('папка с файлом удалена')
#            else:
#                i = str(i)
#                os.rmdir("dir_"+i)
#              i = int(i)
#               i += 1
#                print('папка с файлом удалена')


import os
import shutil
import re

a = int(input('Выберете пункт меню:\n'
              '1.Создать директории\n'
              '2.Удалить директории\n'))
if a == 1:
    for i in range(1,10):
        i = str(i)
        if not os.path.exists('dir_'+i):
            os.mkdir('dir_'+i)
            i = int(i)
        else:
            print('Папка' ,'dir_'+i, 'уже создана')
if a == 2:
    for i in range(1,10):
        i = str(i)
        if os.path.exists('dir_'+i):
            print('папка', 'dir_'+i, 'есть')
            d = os.listdir(path='dir_'+i)
            os.rmdir('dir_'+i)
            print('папка', 'dir_'+i, 'удалена')
            if d != []:
                e = int(input('Папка не пуста. Всеравно удалить?'))
                if e == 1:
                    shutil.rmtree('dir_'+i)
                    print('папка', 'dir_'+i, 'удалена')
        else:
            print('папки', 'dir_'+i, 'не существует')
# Задача-2:
# Напишите скрипт, который выводит в консоль список файлов и папок в указанной директории.
a = input('Введите полный путь до необходимой вам дериктории:')
b = os.listdir(f'{a}')
print(b)

