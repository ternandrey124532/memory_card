from PyQt5.QtCore import Qt#функциональный модуль
from random import*#подключение рандома
from PyQt5.QtWidgets import*#За окно
from PyQt5.QtCore import QTimer#timer
from question_layout import*
w,h=600,600
window3=QWidget()
window3.resize(w,h)#установка размеров 
window3.setWindowTitle("question layout")#установка названия окна
window3.move(100,100)

    

le1=QLabel('Статистика:')
le2=QLabel('Правильні відповіді:')
le3=QLabel('Неправильні відповіді:')
linv=QVBoxLayout()
linv.addWidget()
linv.addWidget(le2)
linv.addWidget(le3)
linh=QHBoxLayout()
linh.addWidget(linv)
window3.setLayout(linh)
#def statistika()