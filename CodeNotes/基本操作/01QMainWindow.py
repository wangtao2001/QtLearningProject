"""
测试主窗口QMainWindow类
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class FirstMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWindow, self).__init__(parent)  # 不常用的初始化的方式

        # 设置主窗口标题
        self.setWindowTitle('第一个主窗口应用')

        # 设置窗口尺寸
        self.resize(400, 300)

        # 状态栏
        self.status = self.statusBar()
        self.status.showMessage("只显示5秒", 5000)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建应用程序
    app.setWindowIcon(QIcon('../../ResourceFile/Ico/computer.ico'))  # 为应用添加图标
    main = FirstMainWindow()  # 自定义主窗口
    main.show()  # 显示窗口
    sys.exit(app.exec_())  # 主事件循环
