'''
QPushButton控件：显示图标和点开关功能，不可用
使用lambda绑定槽函数
'''

import sys
from PyQt5.QtWidgets import QVBoxLayout,QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon

###################################
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.setWindowTitle(" ")
        self.setGeometry(200,200,200,200)

        self.button = QPushButton("World")#可以在这里添加热键
        #self.setEnabled(False)#按钮不可用
        self.button.setIcon(QIcon("D:\VSCode-Python-Lib\GUI\Pyqt5_WriteByQtdesigner\ico\\button.png"))
        self.button.setCheckable(True)#将按钮变为开关功能
        self.button.toggle()#同上一起使用
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.ischecked)
        self.button.clicked.connect(lambda : self.print_text(self.button))
    #可以使用sender()获得发出信号的控件，也可以直接向槽函数传入控件
    #那么绑定槽函数时就需要传入控件
    #直接connect()是不能传参的，则使用lambda函数，本身是一个函数，功能就是调用传参过的槽函数
    
    #两种不同获取信号组件的方式
    def print_text(self,btn):
        print("Hello "+btn.text())
    def ischecked(self):
        if self.sender().isChecked():
            print("按钮被选中")
        else:
            print("按钮没有选中") 
##################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())


