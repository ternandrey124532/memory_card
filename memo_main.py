from PyQt5.QtCore import Qt#функциональный модуль
from random import*#подключение рандома
from PyQt5.QtWidgets import*#За окно
from PyQt5.QtCore import QTimer#timer
from memo_card1 import*#модуль 
from question_layout import*#подклчение линий из модуля
from statictika import*

time_unit=60000#1 minyta
timer=QTimer()#создание таймера
def sleep():#функция для остановки таймера
    window.hide()#окно зачиняється
    schet=boxm.text()#считывание текста 
    schet=int(schet)#переделывание в числовой формат 
    timer.setInterval(schet*time_unit)#создание интервала
    timer.start()#таймер запускается
    timer.timeout.connect(wake)
def wake():#функция для запуска таймера
    timer.stop()#таймер осстанавливается
    window.show()#окно показывается

w,h=600,500#ширина и высота окна
#tre=True
window=QWidget()#создание виджета
window.resize(w,h)#установка своих размеров окна
window.setWindowTitle("Memory Card") #установка названия на окно
window.move(100,100)

        


radio_l=[radio1,radio2,radio3,radio4]#создание списка с радиобаттонами
shuffle(radio_l)

def chek_result():#функция для проверки результата
    correct=radio_l[0].isChecked()#проверка правильного ответа
    if correct:
        rightw.setText('правильно')#меняем текст на правильно
        showr()#нажатие на кнопку ответить
    else:#или
        incorrect=radio_l[1].isChecked() or radio_l[2].isChecked() or radio_l[3].isChecked()
        if incorrect:
            rightw.setText('неправильно')#текст неправильно 
            showr()#нажатие на кнопку ответить
def click_OK():#функция для нажатия
    if vidp.text() == 'Відповісти':#считывание текста
        chek_result()#проверка результата
    elif vidp.text() == 'Наступне питання':
        start()
        showq()
        
    
qlist=[]#создание списка
def creatq():#создание вопроса
    a=qe1.text()#считывание текста 
    b=qe2.text()#считывание текста
    c=qe3.text()#считывание текста
    d=qe4.text()#считывание текста
    e=qe5.text()#считывание текста
    g=Question(a,b,c,d,e)#добавление вопросов в клас
    qlist.append(g)#добавление вопросов в список
def clear():#очистка вопросов
    qe1.clear()#очистка вопросов
    qe2.clear()#очистка вопросов
    qe3.clear()#очистка вопросов
    qe4.clear()#очистка вопросов
    qe5.clear()#очистка вопросов

def start():#кнопка запуск
    randq=choice(qlist)#рандом вопросов в списке
    radio_l[0].setText(randq.answer)#правильний вопрос
    radio_l[1].setText(randq.wrong_answer1)#неправильный вопрос
    radio_l[2].setText(randq.wrong_answer2)#неправильный вопрос
    radio_l[3].setText(randq.wrong_answer3)#неправильный вопрос
    vidpovid.setText(randq.answer)#правильный ответ
    vopros.setText(randq.question)#вопрос

    window2.hide()
    window.show()
    
    


window.setLayout(v3)#крепим главную вертикальну линию на окно
window2.setLayout(vrtg)#крепим главную горизонтальную линию на окно
vidp.clicked.connect(click_OK)#нажатие на ответить

qb1.clicked.connect(creatq)#создание вопросов
qb2.clicked.connect(clear)#очистка вопросов
qb3.clicked.connect(start)#запуск

timer.timeout.connect(wake)#таймер зарабатывает
otdih.clicked.connect(sleep)#таймер останавливается

window.show()#окно показывается
window2.show()#окно показывается
window.hide()#окно закрыть
app.exec_()#приложение закрыть
#app.exec_()#приложение закрыть