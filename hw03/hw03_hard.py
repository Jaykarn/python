# Написать консольное меню вида:

# 1. Добавить
# 2. Удалить
# 3. Распечатать
# 4. Посчитать
# 5. Выйти

# Надо чтобы
# а) Можно было удобно менять порядок меню и\или добавлять\удалять пункты меню
# б) Каждое действие (добавить, удалить и тд) должно быть функцией
# в) У пользователя надо спросить номер команды
# г) Программа не должна завершаться пока не введется команда Выйти
# д) Проверять на ввод ошибочных данных, там где они могут появиться


class Menu:
    def AddItem(self,item):
        class Item:
            def __init__(self,text,ToDoNext):
                self.text=text
                ??????????????
        self.item.append(Item())
    def Show():
        for i in range(len(self.item)):
            print(str(i+1)+") "+str(self.item[i])+"\n")
        print("0) Back\n")
        option=int(input())
        self.item[option].????????????