'''
QCheckBox控件：复选按钮控件
复选框的三种状态
'''
import sys
from PyQt5.QtWidgets import QHBoxLayout,QApplication,QWidget,QCheckBox
from PyQt5.QtCore import Qt

#################################
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(" ")
        self.setGeometry(200,200,600,400)

        self.layout = QHBoxLayout(self)
        self.button1 = QCheckBox("Today")
        self.button1.setChecked(True)#设置为选中状态
        self.button2 = QCheckBox("Tomorrow")#默认为未选中状态
        self.button3 = QCheckBox("Yesterday")
        self.button3.setTristate(True)
        self.button3.setCheckState(Qt.PartiallyChecked)

        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)                                             
        self.layout.addWidget(self.button3)       
##################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())