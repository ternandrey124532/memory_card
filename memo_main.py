from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
w,h=600,500
app=QApplication([])
window=QtWidget
window.resize(w,h)
window.setWindowTitle("Memory Card")
window.move(100,100)


window.show()
app.exec_()
