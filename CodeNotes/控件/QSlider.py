'''
QSlider：滑块控件
获取所选数字等操作
'''
import sys
from PyQt5.QtWidgets import QVBoxLayout,QApplication,QWidget,QSlider,QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
#################################
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(" ")
        self.setGeometry(200,200,600,300)

        self.layout = QVBoxLayout(self)
        self.label = QLabel("当前值")
        self.label_hello = QLabel("Hello World")
        self.slider = QSlider(Qt.Horizontal)#水平方向
        #设置最小值与最大值初始化必要操作
        self.slider.setMinimum(10)
        self.slider.setMaximum(30)
        self.slider.setValue(16)#初始值
        self.slider.setSingleStep(2)#步长
        
        self.slider.setTickInterval(6)#设置刻度间隔
        self.slider.setTickPosition(QSlider.TicksBelow)#设置刻度位置

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.label_hello)
        self.layout.addWidget(self.slider)

        self.slider.valueChanged.connect(self.valuechanged)

    def valuechanged(self):
        size = self.sender().value()
        self.label.setText("当前值"+str(size))
        self.label_hello.setFont(QFont("黑体",size))#随着滑块滑动字号改变
##################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())