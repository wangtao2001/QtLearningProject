'''
选项卡控件
QTabWidget类
'''

import sys
from PyQt5.QtWidgets import QApplication,QTabWidget,QWidget,\
    QPushButton,QVBoxLayout

class MainWindow(QTabWidget):#继承的是QtabWidget类
    def __init__(self):
        super().__init__()

        self.setWindowTitle(" ")
        self.resize(600,400)

        self.tab1 = QWidget()#每一个页就是一个单独的页面
        self._setTab1UI()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1,"第一页")#添加页也就是窗口
        self.addTab(self.tab2,"第二页")
        self.addTab(self.tab3,"第三页")

    def _setTab1UI(self):#将每一个选项卡的定制单独封装
        layoutTab1 = QVBoxLayout(self.tab1)
        layoutTab1.addWidget(QPushButton("there"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
    