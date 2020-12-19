# -*- coding: utf-8 -*-
'''
设置控件的提示信息和字体
将UI初始化单独封装
'''
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip,QHBoxLayout,QPushButton,QWidget#控件提示信息
from PyQt5.QtGui import QFont#字体设置

#####################
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()#将UI初始化单独封装一个方法

    def initUI(self):
        QToolTip.setFont(QFont("SansSerif",12))#为提示信息设置字体
        self.setToolTip('今天<b>星期五</b>')#为窗口设置提示消息，支持富文本
        
        self.setGeometry(300,300,400,300)
        self.setWindowTitle("This is Title")

        self.pushButton = QPushButton("消息")
        self.pushButton.setToolTip("现在是晚上八点")#为按钮设置提示消息

        self.layout = QHBoxLayout()#水平布局对象
        self.layout.addWidget(self.pushButton)#将按钮添加到水平布局       
        self.mainFrame = QWidget()#主框架
        self.mainFrame.setLayout(self.layout)#将布局添加到框架上
        self.setCentralWidget(self.mainFrame)#将主框架充满整个屏幕
#####################

if __name__ == '__main__':
    app = QApplication(sys.argv)

    firstWindow = MainWindow()
    firstWindow.show()
    sys.exit(app.exec_())