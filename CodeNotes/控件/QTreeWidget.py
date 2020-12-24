'''
实现树控件：
创建树控件
添加根节点与子节点
为节点添加响应事件
'''

from PyQt5.QtWidgets import QMainWindow,QApplication,QTreeWidget,QTreeWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(" ")
        self.resize(600,400)

        self.tree = QTreeWidget()#创建树控件框架
        self.tree.setColumnCount(2)#设置列数
        self.tree.setHeaderLabels(["key","value"])#指定列标签
        self.tree.setColumnWidth(0,200)#设置第0列宽度为200

        self.treeRoot = QTreeWidgetItem(self.tree)#将节点放入树中
        
        self.treeRoot.setText(0,"文件")#在第0列添加文本
        self.treeRoot.setIcon(0,QIcon(r"ResourceFile\Ico\open.png"))

        self.treeRootChild1 = QTreeWidgetItem(self.treeRoot)#为根节点添加子节点
        self.treeRootChild1.setText(0,"文件A")#任然需要指定列数
        self.treeRootChild1.setText(1,"文件A数据")
        self.treeRootChild1.setCheckState(0,Qt.Checked)#设置复选框
        self.treeRootChild2 = QTreeWidgetItem(self.treeRoot)
        self.treeRootChild2.setText(0,"文件B")

        self.setCentralWidget(self.tree)#将树控件充满整个屏幕
        self.tree.expandAll()#设置默认展开所有节点
        self.tree.clicked.connect(self.onTreeClicked)#为树绑定槽函数

    def onTreeClicked(self,_):
        item = self.tree.currentItem()#获得被单击的节点
        print(f"key={item.text(0)} value={item.text(1)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())