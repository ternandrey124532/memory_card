from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
vidp=QPushButton('Відповісти')
men=QPushButton('Меню')
otdih=QPushButton('Відпочити')
boxm=QSpinBox()
boxm.setValue(30)
groupb=QGroupBox('Варіанти відповідей')
gp=QButtonGroup()
#knopki
ct=QRadioButton()
aplle=QRadioButton()
appl=QRadioButton()
build=QRadioButton()

gp.addButton(ct)
gp.addButton(apple)
gp.addButton(appl)
gp.addButton(build)

v1=QVBoxLayout()
v2=QVBoxLayout()
v3=QVBoxLayout()
v4=QVBoxLayout()

v1.addWidget(ct)
v1.addWidget(aplle)
v2.addWidget(appl)
v2.addWidget(build)

g1=QHBoxLayout()
g1.addLayout(men)
g1.addLayout(otdih)

g2=QHBoxLayout()
g2.addLayout(v1)
g2.addLayout(v2)

g3=QHBoxLayout()
g3.add(vidp)
