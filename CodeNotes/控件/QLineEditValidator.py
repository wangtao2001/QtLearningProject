'''
对QLineEdit输入内容进行限制（校验器）
使用正则表达式类
'''
import sys
from PyQt5.QtWidgets import QFormLayout,QLineEdit,QApplication,QWidget
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator#三种校验器：整形，浮点型，正则
from PyQt5.QtCore import QRegExp#正则表达式类

###################################
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.layout = QFormLayout(self)

        self.intLineEdit = QLineEdit()#创建三个输入框用以不同限制内容
        self.doubleLineEdit = QLineEdit()
        self.regexpLineEdit = QLineEdit()

        self.layout.addRow("整数类型",self.intLineEdit)#添加到布局
        self.layout.addRow("浮点数类型",self.doubleLineEdit)
        self.layout.addRow("数字和字母",self.regexpLineEdit)

        #设置校验器
        intValidator = QIntValidator(self)
        intValidator.setRange(0,99)
        
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setNotation(QDoubleValidator.ScientificNotation)#正常显示浮点数
        doubleValidator.setDecimals(2)#设置精度小数点后两位

        regexpValidator = QRegExpValidator(self)
        regexpValidator.setRegExp(QRegExp("[a-zA-Z0-9]+"))

        #绑定校验器
        self.intLineEdit.setValidator(intValidator)
        self.doubleLineEdit.setValidator(doubleValidator)
        self.regexpLineEdit.setValidator(regexpValidator)
#####################################

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())



