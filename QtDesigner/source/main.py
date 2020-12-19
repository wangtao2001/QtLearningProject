# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import calculator as uifile
import ctypes

if __name__ == '__main__':
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

    app = QApplication(sys.argv)  #创建应用，获得命令行参数
    MainWindow = QMainWindow()    #创建窗口
    MainWindow.move(100,100)      #设置初始窗口位置  

    ui = uifile.Ui_MainWindow()
    ui.setupUi(MainWindow)


    MainWindow.show()            #显示窗口
    sys.exit(app.exec_())        #进入程序的主循环

