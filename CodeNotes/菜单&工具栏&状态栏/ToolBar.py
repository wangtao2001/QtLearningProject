'''
创建和使用工具栏：动作的集合，理解为菜单动作的快捷方式
'''

import sys,math
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(" ")
        self.resize(300,200)

        self.toolFile = self.addToolBar("File")#像窗口添加工具栏对象,不同工具栏会以分割线分隔
        self.toolFile.setToolButtonStyle(Qt.ToolButtonIconOnly)#设置图标与文字的关系这里是只显示图标

        self.newAction = QAction(QIcon(r"ResourceFile\Ico\new.png"),"new",self)#在有图标的情况下文字会以提示的方式出现
        self.openAction = QAction(QIcon(r"ResourceFile\Ico\open.png"),"open",self)

        self.toolFile.addAction(self.newAction)#为工具栏添加动作
        self.toolFile.addAction(self.openAction)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    firstWindow = MainWindow()
    firstWindow.show()
    sys.exit(app.exec_())
