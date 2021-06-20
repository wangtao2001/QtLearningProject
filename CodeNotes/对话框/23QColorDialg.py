"""
23.颜色对话框类型:用于改变文字颜色、背景色
"""
from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPalette  # 调色板
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel()
        self.button2 = QPushButton("选择背景颜色")
        self.button = QPushButton("选择文字颜色")
        self.layout = QVBoxLayout(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(" ")
        self.resize(400, 600)

        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.selectTextColor)
        self.layout.addWidget(self.button2)
        self.button2.clicked.connect(self.selectBGColor)
        self.label.setText("Hello World 你好 世界")
        self.layout.addWidget(self.label)

    def selectTextColor(self):
        color = QColorDialog.getColor()
        palette = QPalette()  # 创建一个调色板
        palette.setColor(QPalette.WindowText, color)  # 为调色板设置颜色
        # 注意这里是作用于WindowText
        self.label.setPalette(palette)

    def selectBGColor(self):
        color = QColorDialog.getColor()
        palette = QPalette()  # 创建一个调色板
        palette.setColor(QPalette.Window, color)  # 为调色板设置颜色
        self.label.setAutoFillBackground(True)
        self.label.setPalette(palette)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    firstWindow = MainWindow()
    firstWindow.show()
    sys.exit(app.exec_())
