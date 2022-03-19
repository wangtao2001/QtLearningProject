import random
import sys

from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QMessageBox
from DialogUtils import *
from TreadUtils import *


class MainWindow(QMainWindow):
    """
    程序主窗口
    """
    def __init__(self):
        super().__init__()
        # 初始化字体
        self.weight_font = QFont("宋体", 15)
        self.label_font = QFont("宋体", 20)
        # 初始化所有控件
        self.button = None
        self.label = None
        # 执行初始化函数
        self.init_window()
        self.init_weight()
        # 主框架
        self.frame = QWidget()
        # 创建栅格布局
        self.layout = QGridLayout(self.frame)
        # 加载框架
        self.add_weight()
        self.setCentralWidget(self.frame)
        # 判断程序状态
        self.status = 0
        # 选择的数
        self.select_num = 0
        # 实时题目数组
        self.nums = None

    def init_window(self):
        """
        初始化窗口
        :return:
        """
        self.setWindowTitle("随机选题")
        # 位置与宽高
        self.resize(400, 400)
        self.setCenter()

    def setCenter(self):
        """
        设置屏幕居中
        :return:
        """
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2)

    def init_weight(self):
        """
        初始化所有控件
        :return:
        """
        self.button = QPushButton()
        self.button.setText("开始选择")
        self.button.clicked.connect(self.execute)
        self.setFont(self.weight_font)
        self.label = QLabel()
        self.label.setFont(self.label_font)
        # self.label.setAlignment(QtCore.Qt.AlignCenter)

    def add_weight(self):
        """
        #将控件、布局加载到框架上
        :return:
        """
        self.layout.addWidget(self.label, 0, 0, 4, 5)
        self.layout.addWidget(self.button, 5, 2, 1, 1)

    def execute(self):
        """
        程序主要处理函数
        :return:
        """
        text = self.sender().text()
        if text == "开始选择":
            self.status = 0
            self.button.setText("停止")
            raed_thread = ReadThread()
            raed_thread.finishSignal.connect(self.callback)
            try:
                raed_thread.run()
            except NoFileException:
                QMessageBox.critical(self, "错误", "请先选择题目总数", QMessageBox.Yes)
                sys.exit()
        elif text == "停止":
            self.status = 1
            self.button.setText("完成")
            self.label.setText("您选择的题目为：" + str(self.select_num))
            self.nums.remove(self.select_num)
            QApplication.processEvents()
            write_thread = WriteThread(self.nums)  # 移除掉已经选择数，重新写回去
            write_thread.run()
        else:
            self.label.setText("")
            self.button.setText("开始选择")
            QApplication.processEvents()

    def callback(self, nums):
        """
        快速更新label显示文字
        :param nums: 题目数组
        :return:
        """
        self.nums = nums
        if len(nums) == 0:
            QMessageBox.critical(self, "错误", "请重新选择题目总数", QMessageBox.Yes)
            sys.exit()
        while not self.status:
            self.select_num = random.choice(self.nums)
            self.label.setText("您选择的题目为：" + str(self.select_num))
            QApplication.processEvents()  # 刷新页面
