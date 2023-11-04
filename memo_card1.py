from PyQt5.QtCore import Qt#функциональный модуль
from PyQt5.QtWidgets import*#За окно
app=QApplication([])#создание приложения
vidp=QPushButton('Відповісти')#кнопка отвеат
men=QPushButton('Статистика')#кнопка меню
otdih=QPushButton('Відпочити')#кнопка отдыха
boxm=QSpinBox()#таймер окошко
boxm.setValue(30)#начальное колличество секунд

box1=QGroupBox('Варіанти відповідей')#создание бокса1
vopros=QLabel('')#создание текста вопроса
gp=QButtonGroup()#группа баттонов
#knopki
radio1=QRadioButton()#создание радиобаттона
radio2=QRadioButton()#создание радиобаттона
radio3=QRadioButton()#создание радиобаттона
radio4=QRadioButton()#создание радиобаттона

gp.addButton(radio1)#добавление кнопки радиобаттона
gp.addButton(radio2)#добавление кнопки радиобаттона
gp.addButton(radio3)#добавление кнопки радиобаттона
gp.addButton(radio4)#добавление кнопки радиобаттона
#вертикальные
v1=QVBoxLayout()#создание вертикальных линий
v2=QVBoxLayout()#создание вертикальных линий
v3=QVBoxLayout()#главная вертикальная линия
v4=QVBoxLayout()#создание вертикальных линий
#виджеты кнопок
v1.addWidget(radio1)#добавление виджета на 1 линию
v1.addWidget(radio2)#добавление виджета на 1 линию
v2.addWidget(radio3)#добавление виджета на 2 линию
v2.addWidget(radio4)#добавление виджета на 2 линию
#прикрепили радиобаттони к боксу1
horizontal=QHBoxLayout()#горизонтальная линия
horizontal.addLayout(v1)#добавление 1 линии
horizontal.addLayout(v2)#добавление 2 линии
box1.setLayout(horizontal)#добавление в бокс1 горизонтальную линию которая содержит в себе 2 вертикальх

#горизонтальная
g1=QHBoxLayout()#создание горизонтальной линии
g2=QHBoxLayout()#создание горизонтальной линии
g3=QHBoxLayout()#создание горизонтальной линии
g4=QHBoxLayout()#создание горизонтальной линии

g1.addWidget(men)#добавление виджета меню на 1 горизонтальную линию
g1.addWidget(otdih)#добавление виджет отдых на 1 линию
g1.addWidget(boxm)

g2.addWidget(vopros)#добавления виджета вопроса

g3.addWidget(box1)#добаавления на 3 линию виджет бокс1

g4.addWidget(vidp)#добавление на 4 линию ответа

#box2
box2=QGroupBox('результат')#создание 2 бокса
rightw=QLabel()#праивльно не правильно
vidpovid=QLabel()#apple
vres=QVBoxLayout()#вертикальная линия
vres.addWidget(rightw,alignment=(Qt.AlignTop | Qt.AlignLeft))
vres.addWidget(vidpovid,alignment=Qt.AlignCenter,stretch=2)
box2.setLayout(vres)#добавление бокс2 на вертикальную линию
g3.addWidget(box2)#добавление на горизотальную линию бокса2
box2.hide()#бокс2 не показівается


v3.addLayout(g1)#добавление на главную линию горизонтальную
v3.addLayout(g2)#добавление на главную линию горизонтальную
v3.addLayout(g3)#добавление на главную линию горизонтальную
v3.addLayout(g4)#добавление на главную линию горизонтальную



def showr():#нажал відповісти
    box1.hide()#!!!!!!!!!!!
    box2.show()#бокс2 показівается
    vidp.setText('Наступне питання')#установка текста следуюий вопрос
def showq():#функция показ вопроса
    vidp.setText('Відповісти')#ставим текст ответить
    box1.show()#бокс1 показывается
    box2.hide()#бокс2 спрятался
    gp.setExclusive(False)#снятие огранчиений что б скинуть выбор
    radio1.setChecked(False)#снятие ограничений с радиобаттона 1
    radio2.setChecked(False)#снятие ограничений с радиобаттона 2
    radio3.setChecked(False)#снятие ограничений с радиобаттона 3
    radio4.setChecked(False)#снятие ограничений с радиобаттона 4
    gp.setExclusive(True)#вернуть ограничения