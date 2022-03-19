
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QGridLayout, QMainWindow, QSpinBox
from PyQt5 import QtCore

from TreadUtils import *


class FirstWindow(QDialog):
    """
    提示是否为第一次使用的窗口，参数window为选择后展示的窗口
    """

    def __init__(self, windowYes: QDialog, windowNo: QMainWindow):
        super().__init__()
        self.windowYes = windowYes
        self.windowNo = windowNo
        self.setWindowTitle("请选择")
        self.setGeometry(700, 400, 350, 150)

        font = QFont("宋体", 13)
        self.label = QLabel("是否为第一次使用本程序？")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.button_yes = QPushButton("是")
        self.button_yes.setFont(font)
        self.button_no = QPushButton("否")
        self.button_no.setDefault(1)  # 默认选中
        self.button_no.setFont(font)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.label, 0, 0, 2, 2)
        self.layout.addWidget(self.button_yes, 3, 0, 1, 1)
        self.layout.addWidget(self.button_no, 3, 1, 1, 1)

        # 绑定单击方法
        self.button_yes.clicked.connect(self.set_status)
        self.button_no.clicked.connect(self.set_status)

    def set_status(self):
        """
        槽函数，设置接下来展示的窗口
        :return:
        """
        text = self.sender().text()
        if text == "是":
            self.windowYes.show()
        else:
            self.windowNo.show()
        self.close()


class SelectNumWindow(QDialog):
    """
    第一次使用，提示用户选择题号的范围
    """

    def __init__(self, mainWindow: QMainWindow):
        super().__init__()
        self.setWindowTitle("请选择")
        self.setGeometry(700, 400, 350, 150)
        self.mainWindow = mainWindow

        font = QFont("宋体", 13)
        self.box = QSpinBox()
        self.box.setValue(10)  # 设置默认值
        self.box.setRange(1, 100)  # 设置范围
        self.box.setSingleStep(1)  # 设置步长
        self.box.setFont(font)
        self.label = QLabel("请选择题目总数")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.button = QPushButton("确认")
        self.button.setFont(font)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.label, 0, 0, 1, 3)
        self.layout.addWidget(self.box, 1, 0, 1, 3)
        self.layout.addWidget(self.button, 2, 1, 1, 1)

        self.button.clicked.connect(self.execute)

    def execute(self):
        # 写文件这里需要使用多线程
        thread = WriteThread([i for i in range(1, self.box.value()+1)])
        thread.finishSignal.connect(self.callback)  # 执行完毕后执行回调函数
        thread.run()

    def callback(self):
        self.close()
        self.mainWindow.show()
