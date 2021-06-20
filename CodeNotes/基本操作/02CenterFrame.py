"""
2.手动居中布局：屏幕坐标系-窗口坐标系
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget  # 主窗口、应用程序、显示器类


class MainWindow(QMainWindow):  # 创建自定义类，继承主窗口类
    def __init__(self):
        super().__init__()  # 一般的初始化方式

        self.setWindowTitle("This is Title")  # 标题
        self.resize(600, 400)  # 窗口大小
        self._center()

    def _center(self):  # 使屏幕居中
        screen = QDesktopWidget().screenGeometry()  # 屏幕坐标系
        size = self.geometry()  # 窗口坐标系
        self.move((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    firstWindow = MainWindow()
    firstWindow.show()
    sys.exit(app.exec_())
