# -*- coding: utf-8 -*-
'''
设置伙伴关系，模拟登录页面
'''
import sys
from PyQt5.QtWidgets import QLabel,QPushButton,QLineEdit,QApplication,QGridLayout,QDialog

#############################
class MainWindow(QDialog):#使用对话窗口
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("登录")

        self.nameLabel = QLabel("账号&N")#绑定热键Alt+N快速聚焦
        self.passwordLabel = QLabel("密码&P")
        self.nameLineEdit = QLineEdit()
        self.passwordLineEdit = QLineEdit()
        self.signinButton = QPushButton("登录&S")
        self.cancelButton = QPushButton("取消&C")

        self.nameLabel.setBuddy(self.nameLineEdit)#设置伙伴关系
        self.passwordLabel.setBuddy(self.passwordLineEdit)

        self.layout = QGridLayout(self)#将布局直接加载到窗口上
        self.layout.addWidget(self.nameLineEdit,0,1,1,2)
        self.layout.addWidget(self.nameLabel,0,0)
        self.layout.addWidget(self.passwordLineEdit,1,1,1,2)
        self.layout.addWidget(self.passwordLabel,1,0)
        self.layout.addWidget(self.signinButton,2,1)
        self.layout.addWidget(self.cancelButton,2,2)

        self.cancelButton.clicked.connect(self.exit)
    
    def exit(self):
        app.exit()
##############################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())