"""
21.输入对话框类型:用于获取文本、列表项、整数
"""
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QInputDialog, QFormLayout, QPushButton, QLineEdit
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.lineEdit3 = QLineEdit()
        self.button3 = QPushButton("获取整数数字")
        self.lineEdit2 = QLineEdit()
        self.button2 = QPushButton("获取字符串文本")
        self.lineEdit1 = QLineEdit()
        self.button1 = QPushButton("获取列表项")
        self.layout = QFormLayout(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(" ")
        self.resize(600, 400)

        self.button1.clicked.connect(self.getItem)
        self.layout.addRow(self.button1, self.lineEdit1)

        self.button2.clicked.connect(self.getText)
        self.layout.addRow(self.button2, self.lineEdit2)

        self.button3.clicked.connect(self.getInt)
        self.layout.addRow(self.button3, self.lineEdit3)

    def getItem(self):
        items = ["列表项1", "列表项2", "列表项3", "列表项4"]
        item, state = QInputDialog.getItem(self, "选择输入框", "XX列表", items)
        # 如果按下OK那么state值返回为1,下同
        if state:
            self.lineEdit1.setText(item)

    def getText(self):
        text, state = QInputDialog.getText(self, "文本输入框", "请输入文本")
        if state:
            self.lineEdit2.setText(text)

    def getInt(self):
        num, state = QInputDialog.getInt(self, "整数输入框", "请输入整数")
        if state:
            self.lineEdit3.setText(str(num))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    firstWindow = MainWindow()
    firstWindow.show()
    sys.exit(app.exec_())
