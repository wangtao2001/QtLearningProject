'''
添加、修改和删除树控件中的节点
布局嵌套
不可见的根节点
'''

from PyQt5.QtWidgets import QMainWindow,QApplication,QTreeWidget,QTreeWidgetItem,QHBoxLayout,\
    QPushButton,QWidget,QVBoxLayout
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(" ")
        self.resize(600,400)

        buttonLayout = QHBoxLayout()
        
        addButton = QPushButton("添加节点")
        updateButton = QPushButton("修改节点")
        deleteButton = QPushButton("删除节点")
        
        buttonLayout.addWidget(addButton)
        buttonLayout.addWidget(updateButton)
        buttonLayout.addWidget(deleteButton)
        
        #绑定槽函数
        addButton.clicked.connect(self.addNode)
        updateButton.clicked.connect(self.updateNode)
        deleteButton.clicked.connect(self.deleteNode)

        #树控件部分
        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(["属性","值"])
        self.tree.setColumnWidth(0,200)#

        self.treeRoot = QTreeWidgetItem(self.tree)
        
        self.treeRoot.setText(0,"文件")

        self.treeRootChild1 = QTreeWidgetItem(self.treeRoot)
        self.treeRootChild1.setText(0,"文件A")
        self.treeRootChild1.setText(1,"文件A数据")
        self.treeRootChild2 = QTreeWidgetItem(self.treeRoot)
        self.treeRootChild2.setText(0,"文件B")
        self.treeRootChild2.setText(1,"文件B数据")

        self.tree.expandAll()#展开所有节点

        #将按钮布局和树控件添加到主布局
        mainLayout = QVBoxLayout(self)
        mainLayout.addLayout(buttonLayout)
        mainLayout.addWidget(self.tree)
        self.setLayout(mainLayout)

    def addNode(self):
        #获取添加节点的父对象
        item = self.tree.currentItem()
        node = QTreeWidgetItem(item)#添加到刚刚获取的父节点上
        node.setText(0,"新属性")
        node.setText(1,"新值")
  
    def updateNode(self):
        item = self.tree.currentItem()
        item.setText(0,"修改属性")
        item.setText(1,"修改值")

    def deleteNode(self):
        root = self.tree.invisibleRootItem()#真正的根节点
        for item in self.tree.selectedItems():#当前被选择的根节点
            (item.parent() or root).removeChild(item)
    #通过循环的方式删除被选择节点以及他的子节点
    #根节点的父节点时不可见的，只能获取

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())