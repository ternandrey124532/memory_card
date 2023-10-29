from PyQt5.QtCore import Qt#функциональный модуль
from PyQt5.QtWidgets import*#За окно
w,h=600,800#размеры под окно
#tre=True
window2=QWidget()#делаем окно
window2.resize(w,h)#установка размеров 
window2.setWindowTitle("question layout")#установка названия окна
window2.move(100,100)
#лейбел
qlb1=QLabel('Введіть запитання:')#ставим текст
qlb2=QLabel('Введіть вірну відповідь')#ставим текст
qlb3=QLabel('Введіть першу хибну відповідь')#ставим текст
qlb4=QLabel('Введіть другу хибну відповідь')#ставим текст
qlb5=QLabel('Введіть третю хибну відповідь')#ставим текст
#кнопки батон
hrz1=QHBoxLayout()#создание горизонтальной линии
hrz2=QHBoxLayout()#создание второй горизонтальной линии
qb1=QPushButton('Додати запитання')#кнопка добавить вопрос
qb2=QPushButton('Очистити')#кнопка очистить
qb3=QPushButton('Старт')#кнопка старт
hrz1.addWidget(qb1)#добавление виджета добавить вопрос 
hrz1.addWidget(qb2)#добавление виджета очистить
hrz2.addWidget(qb3)#добавление виджета старт
#для ввода текста
qe1=QLineEdit()#создание полей ля ввода текстов
qe2=QLineEdit()#создание полей ля ввода текстов
qe3=QLineEdit()#создание полей ля ввода текстов
qe4=QLineEdit()#создание полей ля ввода текстов
qe5=QLineEdit()#создание полей ля ввода текстов
#вертикальніе линии прикрепление лейбелов
vert1=QVBoxLayout()#создание вертикальной линии
vert2=QVBoxLayout()#создание 2 вертикальной линии
vert1.addWidget(qlb1)#добавление виджета добавить вопрос
vert1.addWidget(qlb2)#добавление виджета правильного ответа
vert1.addWidget(qlb3)#добавление виджета неправильного ответа
vert1.addWidget(qlb4)#добавление виджета неправильного ответа
vert1.addWidget(qlb5)#добавление виджета неправильного ответа
#прикрипление текст полей
vert2.addWidget(qe1)#крепим текстовые поля на вертикальную линию
vert2.addWidget(qe2)#крепим текстовые поля на вертикальную линию
vert2.addWidget(qe3)#крепим текстовые поля на вертикальную линию
vert2.addWidget(qe4)#крепим текстовые поля на вертикальную линию
vert2.addWidget(qe5)#крепим текстовые поля на вертикальную линию
#линии горизонт
horz=QHBoxLayout()#создание горизонтальной линии
horz2=QHBoxLayout()#создание горизонтальную линию
horz3=QHBoxLayout()#создание горизонатьную линию
horz.addLayout(vert1)#добавление линии вертикальной
horz.addLayout(vert2)#добавление линии вертикальной
horz2.addWidget(qb1)#добавление виджета добавить вопрос
horz2.addWidget(qb2)#очистить виджет
horz3.addWidget(qb3)#старт
#главная вертикальная
vrtg=QVBoxLayout()#создание главной вертикальной
vrtg.addLayout(horz)#добавление горизонтальной линии
vrtg.addLayout(horz2)#добавление горизонтальной линии
vrtg.addLayout(horz3)#добавление горизонтальной линии
#закреп главной линии на єкране
window2.setLayout(vrtg)#закреп главной линии на єкране
#class
class Question():#создание класса вопросы
    def __init__(self,question,answer,wrong_answer1,wrong_answer2,wrong_answer3):
        self.question=question#сохранение переменной
        self.answer=answer#сохранение переменной
        self.wrong_answer1=wrong_answer1#сохранение переменной
        self.wrong_answer2=wrong_answer2#сохранение переменной
        self.wrong_answer3=wrong_answer3#сохранение переменной
        self.correct=0#установка начального значения 
        self.attempts=0#установка начального значения 
    def got_right(self):#попытки
        self.correct+=1#добавление правильного вопроса
        self.attempts+=1#добавление 1 балла за попытку
        print('Це правильна відовідь')#выводим текст правильный вопрос
    def got_wrong(self):#функция для неправильного ответа
        self.attempts+=1#добавление 1 балла за непправильный ответ
        print('Відповідь невірна')#вывод на экран текста ответ неправильный