"""
27.绘制多样式直线
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("绘制多样式直线")
        self.resize(300, 200)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)  # 开始绘图
        pen = QPen(Qt.red, 3, Qt.SolidLine)  # 创建一个画笔：颜色、粗细、实线
        # pen.setStyle(Qt.DashLine)  设置虚线
        # Qt.DashDotDotLine 点划线 Qt.DotLine 点线...
        painter.setPen(pen)
        painter.drawLine(20, 40, 250, 40)
        painter.end()  # 结束绘图


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
