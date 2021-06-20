"""
4.探讨三种输出窗口大小与位置的不同方式
使用面向过程方式 将控件直接放入主窗口上
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication  # 窗口、应用程序、显示器
from PyQt5.QtWidgets import QPushButton  # 按钮

app = QApplication(sys.argv)
widget = QWidget()  # 使用widget类型窗口


def onButtonPushed():  # 槽
    print("1")
    print(f"widget.x()={widget.x()}")
    print(f"widget.y()={widget.y()}")
    print(f"widget.width()={widget.width()}")
    print(f"widget.height()={widget.height()}")
    print("2")
    print(f"widget.geometry().x()={widget.geometry().x()}")
    print(f"widget.geometry().y()={widget.geometry().y()}")
    print(f"widget.geometry().width()={widget.geometry().width()}")
    print(f"widget.geometry().height()={widget.geometry().height()}")
    print("3")
    print(f"widget.frameGeometry().x()={widget.frameGeometry().x()}")
    print(f"widget.frameGeometry().y()={widget.frameGeometry().y()}")
    print(f"widget.frameGeometry().width()={widget.frameGeometry().width()}")
    print(f"widget.frameGeometry().height()={widget.frameGeometry().height()}")


############################
# 在MAC OS下 .x() 与.width() 都相同，即窗口的横坐标与宽度是确定的
# .resize(width,height)设置的其实是工作区的宽高而不包括标题栏，标题栏是操作系统根据分辨率指定的
# .y()和.frameGeometry().y() 与.height和.geometry().height() 表示的的是工作区的左上角纵坐标与到底部的宽度
# .geometry.y() 表示整个窗口的纵坐标
# .frameGeometry().height() 表示整个窗口的高度
# 在Windows下整个窗口外围有一个边框，会有一到两个像素的差别
############################


btn = QPushButton(widget)  # 将按钮加载到主窗口上
btn.setText("输出此窗口的大小与位置")  # 设置按钮文本
btn.clicked.connect(onButtonPushed)  # 将点击与槽关联
btn.move(25, 35)  # 设置按钮位置

widget.resize(400, 300)  # 窗口大小
widget.move(200, 300)  # 窗口位置
widget.setWindowTitle("This is Title")  # 标题

widget.show()
sys.exit(app.exec_())
