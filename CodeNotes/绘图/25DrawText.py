"""
25.绘制文本，使用paintEvent事件方法
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QFont
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("绘制文本")
        self.resize(300, 200)
        self.text = "Hello World"

    def paintEvent(self, event):
        """
        事件方法，方法名称必须固定
        在窗口大小变化时，就会自动调用这个方法
        这里相当于重写，借用这个事件来启用绘图
        """
        painter = QPainter(self)
        painter.begin(self)  # 开始绘图
        painter.setPen(Qt.blue)  # 设置颜色
        painter.setFont(QFont('SimSun', 25))  # 设置字体
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)
        # 绘图区域：整个窗口、居中对齐、文本内容
        painter.end()  # 结束绘图


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
