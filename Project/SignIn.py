# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QLabel,QPushButton,QLineEdit,QApplication,QGridLayout,QDialog,QHBoxLayout
from PyQt5.QtGui import QFont,QRegExpValidator,QIntValidator
from PyQt5.QtCore import QRegExp,Qt

#############################
class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("登录")
        self.setGeometry(600,300,450,150)

        font = QFont("微软雅黑",10)
        self.nameLabel = QLabel("账号&N")#热键
        self.nameLabel.setFont(font)
        self.passwordLabel = QLabel("密码&P")
        self.passwordLabel.setFont(font)
        self.nameLineEdit = QLineEdit()
        self.nameLineEdit.setFont(font)
        self.passwordLineEdit = QLineEdit()
        self.passwordLineEdit.setFont(font)
        self.signinButton = QPushButton("登录&S")
        self.signinButton.setFont(font)
        self.cancelButton = QPushButton("取消&C")
        self.cancelButton.setFont(font)

        self.nameLabel.setBuddy(self.nameLineEdit)#设置伙伴关系
        self.passwordLabel.setBuddy(self.passwordLineEdit)

        self.nameLineEdit.setEchoMode(QLineEdit.Normal)#回显模式
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.nameLineEdit.setPlaceholderText("账号")#限制输入
        self.nameLineEdit.setValidator(QIntValidator(0,99999999))
        self.passwordLineEdit.setPlaceholderText("密码(区分大小写)")
        self.passwordLineEdit.setValidator(QRegExpValidator(QRegExp("[a-zA-Z0-9]+")))

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.nameLineEdit,0,1,1,2)
        self.layout.addWidget(self.nameLabel,0,0)
        self.layout.addWidget(self.passwordLineEdit,1,1,1,2)
        self.layout.addWidget(self.passwordLabel,1,0)
        self.layout.addWidget(self.signinButton,2,0)
        self.layout.addWidget(self.cancelButton,2,2)

        self.cancelButton.clicked.connect(self.exit)
        self.nameLineEdit.editingFinished.connect(self.nameEditingFinished)#保存账号
        self.passwordLineEdit.editingFinished.connect(self.passwordEditingFinished)#保存密码
        self.signinButton.clicked.connect(self.signin)#比对账号密码
 
    _name = None
    _password = None
    def nameEditingFinished(self):
        self._name = self.sender().text()
    def passwordEditingFinished(self):
        self._password = self.sender().text()
    def exit(self):
        app.exit()
    def signin(self):#点击登录时
        if user.get(self._name,-1) == self._password:
            tipWindow.setText("登陆成功")
            tipWindow.correct()#将新窗口点击与退出程序绑定
            tipWindow.show()
        else:
            tipWindow.setText("账号或密码错误")
            tipWindow.error()#将新窗口点击与退出提示窗口绑定
            tipWindow.show()
            self.passwordLineEdit.clear()#清空密码输入

class TipWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" ")
        self.setGeometry(700,400,450,150)

        font = QFont("微软雅黑",10)
        self.label = QLabel()
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.button = QPushButton("确定")
        self.button.setFont(font)
        
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.label,0,0,1,3)
        self.layout.addWidget(self.button,1,1,1,1)

    def setText(self,text):
        self.label.setText(text)
    def windowexit(self):
        tipWindow.close()
    def appexit(self):
        app.exit()

    def correct(self):
        self.button.clicked.connect(self.appexit)
    def error(self):
        self.button.clicked.connect(self.windowexit)
##############################

if __name__ == "__main__":
    user = {'2020':'aaaa'}

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    tipWindow = TipWindow()
    mainWindow.show()
    sys.exit(app.exec_())