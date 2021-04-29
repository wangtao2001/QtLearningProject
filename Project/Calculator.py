# -*- coding: utf-8 -*-
import ctypes
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QDesktopWidget,QPushButton,QLabel,QGridLayout
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt,QSize,QRect
from math import sin,cos,tan,pi,e

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_window()
        self.set_icon()
        self.init_frame()
        self.init_layout()
        self.init_widget()
        self.add_widget()
        self.binding()
        self.setCentralWidget(self.frame)
    
    def init_window(self):#初始化窗口
        self.setWindowTitle("Calculater")
        #self._center()
        self.setGeometry(1321,50,517,954)
            
    def _center(self):#居中方法
        self.screen = QDesktopWidget().screenGeometry()
        self.size = self.geometry()
        self.move((self.screen.width()-self.size.width())//2,(self.screen.height()-self.size.height())//2)

    def set_icon(self):#设置图标
        self.setWindowIcon(QIcon("D:\Python\GUI\QtDesigner\ico\computer.ico"))     

    def init_widget(self):#创建控件
        font = QFont("等线",20)      
        self.button_one = QPushButton()
        self.button_one.setText("1")
        self.button_one.setFont(font)
        self.button_two = QPushButton()
        self.button_two.setText("2")
        self.button_two.setFont(font)
        self.button_three = QPushButton()
        self.button_three.setText("3")
        self.button_three.setFont(font)
        self.button_four = QPushButton()
        self.button_four.setText("4")
        self.button_four.setFont(font)
        self.button_five = QPushButton()
        self.button_five.setText("5")
        self.button_five.setFont(font)
        self.button_six = QPushButton()
        self.button_six.setText("6")
        self.button_six.setFont(font)
        self.button_seven = QPushButton()
        self.button_seven.setText("7")
        self.button_seven.setFont(font)
        self.button_eight = QPushButton()
        self.button_eight.setText("8")
        self.button_eight.setFont(font)
        self.button_nine = QPushButton()
        self.button_nine.setText("9")
        self.button_nine.setFont(font)
        self.button_zero = QPushButton()
        self.button_zero.setText("0")
        self.button_zero.setFont(font)
        self.button_add = QPushButton()
        self.button_add.setText("+")
        self.button_add.setFont(font)
        self.button_sub = QPushButton()
        self.button_sub.setText("-")
        self.button_sub.setFont(font)
        self.button_multi = QPushButton()
        self.button_multi.setText("*")
        self.button_multi.setFont(font)
        self.button_div = QPushButton()
        self.button_div.setText("/")
        self.button_div.setFont(font)
        self.button_eq = QPushButton()
        self.button_eq.setText("=")
        self.button_eq.setFont(font)
        self.button_clear = QPushButton()
        self.button_clear.setText("C")
        self.button_clear.setFont(font)
        self.button_point = QPushButton()
        self.button_point.setText(".")
        self.button_point.setFont(font)
        self.button_left_bracket = QPushButton()
        self.button_left_bracket.setText("(")
        self.button_left_bracket.setFont(font)
        self.button_right_bracket = QPushButton()
        self.button_right_bracket.setText(")")
        self.button_right_bracket.setFont(font)
        self.button_back = QPushButton()
        self.button_back.setText("Back")
        self.button_back.setFont(font)
        self.button_sin = QPushButton()
        self.button_sin.setText("sin")
        self.button_sin.setFont(font)
        self.button_cos = QPushButton()
        self.button_cos.setText("cos")
        self.button_cos.setFont(font)
        self.button_tan = QPushButton()
        self.button_tan.setText("tan")
        self.button_tan.setFont(font)
        self.button_pi = QPushButton()
        self.button_pi.setText("π")
        self.button_pi.setFont(font)
        self.button_e = QPushButton()
        self.button_e.setText("e")
        self.button_e.setFont(font)
        
        font = QFont("等线",30)
        self.label = QLabel()
        self.label.setFont(font)
    
    def init_layout(self):#创建栅格布局
        self.layout = QGridLayout(self.frame)
    
    def init_frame(self):#加载主框架
        self.frame = QWidget()

    def add_widget(self):#将控件、布局加载到框架上
        self.layout.addWidget(self.button_one,4,0,1,1)
        self.layout.addWidget(self.button_two,4,1,1,1)
        self.layout.addWidget(self.button_three,4,2,1,1)
        self.layout.addWidget(self.button_four,3,0,1,1)
        self.layout.addWidget(self.button_five,3,1,1,1)
        self.layout.addWidget(self.button_six,3,2,1,1)
        self.layout.addWidget(self.button_seven,2,0,1,1)
        self.layout.addWidget(self.button_eight,2,1,1,1)
        self.layout.addWidget(self.button_nine,2,2,1,1)
        self.layout.addWidget(self.button_zero,5,1,1,1)
        self.layout.addWidget(self.button_eq,5,2,1,1)
        self.layout.addWidget(self.button_add,5,3,1,1)
        self.layout.addWidget(self.button_sub,4,3,1,1)
        self.layout.addWidget(self.button_multi,3,3,1,1)
        self.layout.addWidget(self.button_div,2,3,1,1)
        self.layout.addWidget(self.button_clear,1,3,1,1)
        self.layout.addWidget(self.button_point,5,0,1,1)
        self.layout.addWidget(self.button_left_bracket,1,0,1,1)
        self.layout.addWidget(self.button_right_bracket,1,1,1,1)
        self.layout.addWidget(self.button_back,1,2,1,1)
        self.layout.addWidget(self.button_sin,1,4,1,1)
        self.layout.addWidget(self.button_cos,2,4,1,1)
        self.layout.addWidget(self.button_tan,3,4,1,1)
        self.layout.addWidget(self.button_pi,4,4,1,1)
        self.layout.addWidget(self.button_e,5,4,1,1)

        self.layout.addWidget(self.label,0,0,1,3)

    def binding(self):#绑定信号槽
        self.button_one.clicked.connect(self.label_text)
        self.button_two.clicked.connect(self.label_text)
        self.button_three.clicked.connect(self.label_text)
        self.button_four.clicked.connect(self.label_text)
        self.button_five.clicked.connect(self.label_text)
        self.button_six.clicked.connect(self.label_text)
        self.button_seven.clicked.connect(self.label_text)
        self.button_eight.clicked.connect(self.label_text)
        self.button_nine.clicked.connect(self.label_text)
        self.button_zero.clicked.connect(self.label_text)
        self.button_eq.clicked.connect(self.label_text)
        self.button_add.clicked.connect(self.label_text)
        self.button_sub.clicked.connect(self.label_text)
        self.button_multi.clicked.connect(self.label_text)
        self.button_div.clicked.connect(self.label_text)
        self.button_point.clicked.connect(self.label_text)
        self.button_left_bracket.clicked.connect(self.label_text)
        self.button_right_bracket.clicked.connect(self.label_text)
        self.button_sin.clicked.connect(self.label_text)
        self.button_cos.clicked.connect(self.label_text)
        self.button_tan.clicked.connect(self.label_text)
        self.button_pi.clicked.connect(self.label_text)
        self.button_e.clicked.connect(self.label_text)
        self.button_back.clicked.connect(self.label_back)
        self.button_clear.clicked.connect(self.label_clear)
    
    _outsqueue = []
    _calsqueue = []
    def label_text(self):#按下按钮时在屏幕显示
        text = self.sender().text()
        if text in ['sin','cos','tan']:#补括号
            self._outsqueue.append(text+"(")
            self._calsqueue.append(text+"(")
            self.label.setText("".join(self._outsqueue))
        elif text=='π':#表示不相同
            self._outsqueue.append(text)
            self._calsqueue.append('pi')
            self.label.setText("".join(self._outsqueue))
        elif text != '=':
            self._outsqueue.append(text)
            self._calsqueue.append(text)
            self.label.setText("".join(self._outsqueue))
        else:#其他
            try:
                answer = eval("".join(self._calsqueue))
                if answer%1 == 0 :
                    self.label.setText("%d" % answer)
                else:
                    self.label.setText("%10f" % answer)
                self._outsqueue.append(str(answer))
                self._calsqueue.append(str(answer))
            except:
                self.label.setText("出错")
            finally:
                self._calsqueue = []
                self._outsqueue = []
    def label_clear(self):#清空屏幕
        self._outsqueue = []
        self._calsqueue = []
        self.label.setText("")
    def label_back(self):#退格
        self._outsqueue = self._outsqueue[:-1]
        self._calsqueue = self._calsqueue[:-1]
        self.label.setText("".join(self._outsqueue))

    
if __name__ == "__main__":
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())