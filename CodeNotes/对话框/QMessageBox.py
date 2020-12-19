'''
五种消息对话框类型：
1.关于对话框
2.错误对话框
3.警告对话框
4.提问对话框
5.消息对话框
不同的对话框的图标和按钮控件（可以自定义按钮）可能不同
'''

from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QDialog,QVBoxLayout,QWidget,QMessageBox
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(" ")
        self.setGeometry(400,200,460,800)

        self.button1 = QPushButton("显示关于对话框")
        self.button1.clicked.connect(self.showDialog)
        self.button2 = QPushButton("显示消息对话框")
        self.button2.clicked.connect(self.showDialog)
        self.button3 = QPushButton("显示警告对话框")
        self.button3.clicked.connect(self.showDialog)
        self.button4 = QPushButton("显示错误对话框")
        self.button4.clicked.connect(self.showDialog)
        self.button5 = QPushButton("显示提问对话框")
        self.button5.clicked.connect(self.showDialog)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)
        self.layout.addWidget(self.button5)

    def showDialog(self):
        text = self.sender().text()
        if text == '显示关于对话框':
            QMessageBox.about(self,"关于","这是一个关于对话框")
        #返回值是不同按钮的ID值
        elif text == '显示消息对话框':
            reply = QMessageBox.information(self,"消息","这是一个消息对话框",QMessageBox.Yes|QMessageBox.No)#同时设置不同按钮类型
        elif text == '显示警告对话框':
            reply = QMessageBox.warning(self,"警告","这是一个警告对话框",QMessageBox.Yes|QMessageBox.No)
        elif text == '显示错误对话框':
            reply = QMessageBox.critical(self,"错误","这是一个错误对话框",QMessageBox.Yes|QMessageBox.No)
        elif text == '显示提问对话框':
            reply = QMessageBox.question(self,"提问","这是一个提问对话框",QMessageBox.Yes|QMessageBox.No)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    firstWindow = MainWindow()
    firstWindow.show()
    sys.exit(app.exec_())