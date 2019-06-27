#HARD

# Написать программу для распаковки файлов в корневую из всех папок с расширениями (код взять с урока) и папки удалить
#os.path.isdir('dz1') - определяем папка выбрана или нет
import os
a = int(input('запаковать или распаковать:'))
while a == 1:
BASE_PATH = r'C:\Users\Night\Downloads'
#определяем расширение файлов
ext = set()
est = set
for i in os.listdir(BASE_PATH):#отделяем расширение от имени файла
    print(i)
    if os.path.isfile(os.path.join(BASE_PATH, i)):
        ext.add(os.path.splitext(i)[1])
print(ext)

for e in ext:#создаем папки которых нет вообще с именем расширений
    if not os.path.exists(os.path.join(BASE_PATH, e)):
        os.mkdir(os.path.join(BASE_PATH, e))

for i in os.listdir(BASE_PATH):# переносим файлы в каталоги
    if os.path.isfile(os.path.join(BASE_PATH, i)):
        os.rename(os.path.join(BASE_PATH, i),
                  os.path.join(BASE_PATH, os.path.splitext(i)[1], i))

