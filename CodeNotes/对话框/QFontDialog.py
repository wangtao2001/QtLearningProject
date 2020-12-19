'''
字体对话框类型:用于改变字体、字号并返回
'''
from PyQt5.QtWidgets import QApplication,QWidget,QFontDialog,QVBoxLayout,QPushButton,QLabel
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(" ")
        self.layout = QVBoxLayout(self)
        self.resize(400,600)

        self.button = QPushButton("选择字体")
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.selectFont)
        self.label = QLabel()
        self.label.setText("Hello World 你好 世界")
        self.layout.addWidget(self.label)

    def selectFont(self):
        font,state = QFontDialog.getFont()
        #如果按下OK那么state值返回为1,下同
        if state:
            self.label.setFont(font)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    firstWindow = MainWindow()
    firstWindow.show()
    sys.exit(app.exec_())
