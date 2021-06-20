"""
9.设置伙伴关系，模拟登录页面
使用Alt+字母可以快速聚焦到文本含有&字母的控件，设置伙伴关系后则聚焦到被绑定的控件上
"""
import sys
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QApplication, QGridLayout, QDialog


def _exit():
    app.exit()


class MainWindow(QDialog):  # 使用对话窗口
    def __init__(self):
        super().__init__()
        self.signinButton = QPushButton("登录&S")
        self.passwordLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        self.passwordLabel = QLabel("密码&P")
        self.nameLabel = QLabel("账号&N")  # 绑定热键Alt+N快速聚焦
        self.cancelButton = QPushButton("取消&C")
        self.layout = QGridLayout(self)  # 将布局直接加载到窗口上 不需要使用QWeight框架
        self.initUI()

    def initUI(self):
        self.setWindowTitle("登录")

        self.nameLabel.setBuddy(self.nameLineEdit)  # 设置伙伴关系 Alt+N聚焦到文本框
        self.passwordLabel.setBuddy(self.passwordLineEdit)

        self.layout.addWidget(self.nameLineEdit, 0, 1, 1, 2)
        self.layout.addWidget(self.nameLabel, 0, 0)
        self.layout.addWidget(self.passwordLineEdit, 1, 1, 1, 2)
        self.layout.addWidget(self.passwordLabel, 1, 0)
        self.layout.addWidget(self.signinButton, 2, 1)
        self.layout.addWidget(self.cancelButton, 2, 2)

        self.cancelButton.clicked.connect(_exit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
