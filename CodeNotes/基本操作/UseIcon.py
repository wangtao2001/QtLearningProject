# -*- coding: utf-8 -*-
'''
设置图标以及状态栏：图标的两种方式
'''
######################
import ctypes#解决windows系统下任务栏不显示图标的问题
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
#####################

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget#主窗口、应用程序、显示器
from PyQt5.QtGui import QIcon

#####################
class MainWindow(QMainWindow):#创建主窗口类
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("This is Title")#标题
        self.resize(600,400)#大小
                
        self.statusbar = self.statusBar()#新建状态栏对象
        self.statusbar.showMessage("Hello World")#状态栏显示消息

        #self.setWindowIcon(QIcon(path))
        #也可以使用窗口方法设置图标只是在MAC OS下不会显示
        #即使再通过Application()的方法设置MAC OS 下标题栏图标也不会显示，所以此方法少用
###################

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("D:\Python\GUI\QtDesigner\ico\computer.ico"))
    
    firstWindow = MainWindow()
    firstWindow.show()
    sys.exit(app.exec_())