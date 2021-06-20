"""
24.文件对话框类型：实现打开文件
两种打开方法（注意第二种）
"""
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QPushButton, QLabel, QTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.textEdit = QTextEdit()
        self.button2 = QPushButton("加载文本")
        self.imageLabel = QLabel()
        self.button1 = QPushButton("加载图片")
        self.layout = QVBoxLayout(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(" ")
        self.resize(400, 300)

        self.layout.addWidget(self.button1)
        self.button1.clicked.connect(self.loadImage)  # 加载图片
        self.layout.addWidget(self.imageLabel)

        self.layout.addWidget(self.button2)
        self.button2.clicked.connect(self.loadText)  # 加载文本
        self.layout.addWidget(self.textEdit)

    def loadImage(self):
        path = "."  # 路径就是当前路径
        fname, _ = QFileDialog.getOpenFileName(self, "打开文件", path, "图像文件(*.jpg ,*.png)")  # 参数为对话框标题，初始路径，打开文件提示
        # 打开单个文件
        # 第二个参数不需要就使用_做临时变量 是status 即是否点击了取消
        self.imageLabel.setPixmap(QPixmap(fname))

    # 静态打开文件方法
    def loadText(self):
        dialog = QFileDialog()  # 对话框对象
        dialog.setFileMode(QFileDialog.AnyFile)  # 设置打开文件类型 这里是所有文件
        dialog.setFilter(QDir.Files)  # 打开的是文件
        if dialog.exec():  # 打开文件
            filenames = dialog.selectedFiles()  # 返回被选择的文件（可以打开多个）
            f = open(filenames[0], 'r', encoding='utf-8')  # 选择第一个文件
            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    firstWindow = MainWindow()
    firstWindow.show()
    sys.exit(app.exec_())
