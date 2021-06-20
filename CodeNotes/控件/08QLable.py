"""
8.QLable控件：设置文本对齐、文本颜色、背景色、超链接、提示、显示图片
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget
from PyQt5.QtGui import QPalette, QPixmap  # 调色板设置背景色、显示图片
from PyQt5.QtCore import Qt


def linkHovered():  # 设置槽方法（当鼠标滑过时）
    print("你划过了鼠标")


def linkClicked():  # 设置槽方法（当鼠标单击时）
    print("你单击了鼠标")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainFrame = QWidget()  # 主框架
        self.label1 = QLabel()
        self.label2 = QLabel()
        self.label3 = QLabel()
        self.label4 = QLabel()
        self.initUI()

    def initUI(self):
        palette = QPalette()  # 创建一个调色板
        palette.setColor(QPalette.Window, Qt.blue)  # 为调色板设置颜色

        self.label1.setText("<font color=yellow>这是一个拥有背景颜色的文本标签</font>")  # 设置文本用HTML控制颜色
        self.label1.setAutoFillBackground(True)  # 允许背景填充
        self.label1.setPalette(palette)  # 给标签设置背景色
        self.label1.setAlignment(Qt.AlignCenter)  # 设置文本居中对齐

        self.label2.setText("<a href='#'>划过此标签时会显示信息</a>")

        self.label3.setAlignment(Qt.AlignCenter)  # 文本居中
        self.label3.setToolTip("这是一个图片标签")  # 设置提示文本
        self.label3.setPixmap(QPixmap("../../ResourceFile/Ico/python.jpg"))  # 设置图片

        self.label4.setText("<a href='www.python.org'>python官网</a>")
        self.label4.setAlignment(Qt.AlignRight)  # 右对齐
        self.label4.setToolTip("这是一个超链接")
        #self.label4.setOpenExternalLinks(True)  # 打开启动超链接的功能，会屏蔽其他事件（槽函数）

        vbox = QVBoxLayout()  # 垂直布局
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label3)
        vbox.addWidget(self.label4)

        self.label2.linkHovered.connect(linkHovered)  # 槽绑定
        self.label4.linkActivated.connect(linkClicked)

        self.setWindowTitle("QLable控件演示")
        self.mainFrame.setLayout(vbox)  # 将布局添加到框架上
        self.setCentralWidget(self.mainFrame)  # 将主框架充满整个屏幕


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
