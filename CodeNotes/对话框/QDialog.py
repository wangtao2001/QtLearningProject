'''
基本对话框，所有对话框的基类
对话框的聚焦模式
'''
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QDialog
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(" ")
        self.resize(300,200)

        self.button = QPushButton(self)
        self.button.setText("弹出对话框")
        self.move(50,50)
        self.button.clicked.connect(self.showDialog)
    
    def showDialog(self):
        self.dialog = QDialog()
        self.dialog.button = QPushButton(self.dialog)
        self.dialog.button.setText("确定")
        self.dialog.button.clicked.connect(self.dialog.close)
        self.dialog.setWindowModality(Qt.ApplicationModal)#对话框聚焦模式当前对话框展示时无法聚焦到其他窗口上
        self.dialog.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    firstWindow = MainWindow()
    firstWindow.show()
    sys.exit(app.exec_())