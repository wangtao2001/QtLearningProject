"""
14.QRadioButton控件：单选按钮控件：同时只能有一个被选中
"""
import sys
from PyQt5.QtWidgets import QHBoxLayout, QApplication, QWidget, QRadioButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.button2 = QRadioButton("Tomorrow")
        self.button1 = QRadioButton("Today")
        self.layout = QHBoxLayout(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(" ")
        self.setGeometry(200, 200, 600, 400)

        self.button1.toggled.connect(self.buttonState)  # 状态变化的信号
        self.button2.toggled.connect(self.buttonState)

        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)

    def buttonState(self):
        if self.sender().isChecked():
            print("已选择" + self.sender().text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
