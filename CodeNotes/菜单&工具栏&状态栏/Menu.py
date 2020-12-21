'''
创建和使用菜单
创建动作
动作触发槽
'''
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QAction
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" ")
        self.resize(400,400)
        self.initMenu()
    
    def initMenu(self):
        self.menu = self.menuBar()#菜单栏对象
        
        file = self.menu.addMenu("文件(&F)")#顶层菜单返回一个 菜单对象       
        new = file.addAction("新建")#添加动作也就是子菜单
        new.setShortcut("Ctrl+N")#添加快捷键
        save = QAction("保存",self)#另一种方式
        save.setShortcut("Ctrl+S")
        file.addAction(save)
        _exit = QAction("退出",self)
        _exit.setShortcut("Ctrl+E")
        file.addAction(_exit)

        new.triggered.connect(self.printText)#动作被触发时绑定槽会出入一个布尔量
        save.triggered.connect(self.printText)
        _exit.triggered.connect(self._exitAction)

    def printText(self,bool):
        print(self.sender().text())

    def _exitAction(self,bool):
        app.exit()#退出   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    firstWindow = MainWindow()
    firstWindow.show()
    sys.exit(app.exec_())