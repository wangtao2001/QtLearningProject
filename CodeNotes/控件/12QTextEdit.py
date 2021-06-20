"""
12.QTextEdit控件：显示文本、获取所输入文本
"""
import sys
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QWidget, QTextEdit, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.button_out_html = QPushButton("获得HTML")
        self.button_out_plaintext = QPushButton("获得文本")
        self.button_html = QPushButton("显示HTML")
        self.button_plaintext = QPushButton("显示文本")
        self.textEdit = QTextEdit()
        self.layout = QVBoxLayout(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(" ")
        self.setGeometry(200, 200, 441, 619)

        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(self.button_plaintext)
        self.layout.addWidget(self.button_html)
        self.layout.addWidget(self.button_out_plaintext)
        self.layout.addWidget(self.button_out_html)

        self.button_plaintext.clicked.connect(self.plaintext)
        self.button_html.clicked.connect(self.html)
        self.button_out_plaintext.clicked.connect(self.out_plaintext)
        self.button_out_html.clicked.connect(self.out_html)

    def plaintext(self):
        self.textEdit.setPlainText("Hello,World!")  # 设置文本

    def html(self):
        self.textEdit.setHtml("<font color='blue' size=5>Hello,World!</font>")

    def out_plaintext(self):
        print(self.textEdit.toPlainText())  # 当前输入的文本

    def out_html(self):
        print(self.textEdit.toHtml())  # 获得输入的HTML文本（完整文本）


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
