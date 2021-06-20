"""
18.QComboBox：计数器控件
获取所选数字等操作
"""
import sys
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QWidget, QSpinBox, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.sb = QSpinBox()
        self.label = QLabel("当前值")
        self.layout = QVBoxLayout(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(" ")
        self.setGeometry(200, 200, 400, 100)

        self.sb.setValue(18)  # 设置默认值
        self.sb.setRange(10, 30)  # 设置范围
        self.sb.setSingleStep(2)  # 设置步长

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.sb)

        self.sb.valueChanged.connect(self.valuechanged)

    def valuechanged(self):
        self.label.setText("当前值" + str(self.sender().value()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
