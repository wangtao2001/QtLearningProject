import ctypes
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from DialogUtils import FirstWindow, SelectNumWindow
from MainWindow import MainWindow

if __name__ == "__main__":
    # 解决windows系统下任务栏不显示图标的问题
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    # 创建窗口
    app = QApplication(sys.argv)
    # 设置图标
    app.setWindowIcon(QIcon('E:\PycharmProjects\Selector\ResourceFile\icon\select.ico'))
    # 初始化窗口
    mainWindow = MainWindow()
    numWindow = SelectNumWindow(mainWindow)
    tip = FirstWindow(numWindow, mainWindow)
    tip.show()
    sys.exit(app.exec_())
