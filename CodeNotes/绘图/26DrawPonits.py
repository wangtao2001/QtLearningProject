"""
25.绘制像素点 -> 绘制正弦曲线
"""
from math import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("绘制正弦曲线")
        self.resize(300, 200)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)  # 开始绘图
        painter.setPen(Qt.red)

        for i in range(1000):  # 绘制1000个点
            x = 100 * (-1 + 2.0 * i/1000) + self.size().width()/2.0
            y = -50 * sin((x - self.size().width()/2.0) * pi/50) + self.size().height()/2.0
            painter.drawPoint(x, y)
        painter.end()  # 结束绘图


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
