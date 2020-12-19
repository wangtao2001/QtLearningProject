# -*- coding: utf-8 -*-
'''
初步体验加载组件和使用信号槽
'''
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget#主窗口、应用程序、显示器
from PyQt5.QtWidgets import QHBoxLayout,QWidget,QPushButton#水平布局、控件、按钮

#####################
class MainWindow(QMainWindow):#创建主窗口类
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("This is Title")#标题
        self.resize(600,400)#大小
        
        self.button1 = QPushButton("关闭窗口")#设置按钮对象
        self.button1.clicked.connect(self.onButtonPushed)#将click与槽绑定

        self.layout = QHBoxLayout()#水平布局对象
        self.layout.addWidget(self.button1)#将按钮添加到水平布局
        
        self.mainFrame = QWidget()#主框架
        self.mainFrame.setLayout(self.layout)#将布局添加到框架上

        self.setCentralWidget(self.mainFrame)#将主框架充满整个屏幕
    
    def onButtonPushed(self):#槽,即事件发生后执行的函数,退出app
        print(self.sender().text()+" 发生，程序退出")
        app.exit()
###################

if __name__ == '__main__':
    app = QApplication(sys.argv)

    firstWindow = MainWindow()
    firstWindow.show()
    sys.exit(app.exec_())
