"""
28.绘制多边形，并进行颜色填充
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPolygon, QBrush
from PyQt5.QtCore import QPoint, Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("绘制多边形")
        self.resize(300, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)  # 开始绘图
        brush = QBrush(Qt.SolidPattern)
        painter.setBrush(brush)

        point1 = QPoint(140, 380)
        point2 = QPoint(270, 420)
        point3 = QPoint(290, 512)
        point4 = QPoint(290, 588)
        point5 = QPoint(200, 533)
        polygon = QPolygon([point1, point2, point3, point4, point5])

        painter.drawPolygon(polygon)
        painter.end()  # 结束绘图


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
