"""
16.QComboBox：下拉列表控件
添加列表项和获取所选的列表项
"""
import sys
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QWidget, QComboBox, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.label = QLabel("请选择语言")
        self.cb = QComboBox()
        self.initUI()
        self.printAllItems()

    def initUI(self):
        self.setWindowTitle(" ")
        self.setGeometry(200, 200, 400, 100)

        self.cb.addItems(["Python", "C++", "Java", "C#"])  # 添加列表项

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.cb)

        self.cb.currentIndexChanged.connect(self.itemChanged)  # 当选择项变化时

    def itemChanged(self, i):  # i是向前被选择项的索引，自动传入 connect自动传入
        self.label.setText(self.sender().currentText())  # 当前被选中的文本，也可以使用itemText(i)
        print(f"Selecting item{i}:{self.sender().itemText(i)}")

    def printAllItems(self):  # 输出复选框的所有列表项
        for count in range(self.cb.count()):  # 列表项个数
            print("Item" + str(count) + "= " + self.cb.itemText(count))
    # 有两种知道当前选择项的方法
    # self.sender().currentText()
    # self.sender().itemText(i) i会自动传入槽函数


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
