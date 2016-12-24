# !/usr/bin/python

import sys

from PyQt4.QtGui import *

from PyQt4.QtCore import *

class TreeWidget(QMainWindow):

    def __init__(self,parent=None):

        QWidget.__init__(self,parent)

        self.setWindowTitle('TreeWidget')

        self.tree = QTreeWidget()

        self.tree.setColumnCount(2)

        self.tree.setHeaderLabels(['Key','Value'])

        root= QTreeWidgetItem(self.tree)

        root.setText(0,'root')

        child1 = QTreeWidgetItem(root)

        child1.setText(0,'child1')

        child1.setText(1,'name1')

        child2 = QTreeWidgetItem(root)

        child2.setText(0,'child2')

        child2.setText(1,'name2')

        child3 = QTreeWidgetItem(root)

        child3.setText(0,'child3')

        child4 = QTreeWidgetItem(child3)

        child4.setText(0,'child4')

        child4.setText(1,'name4')

        self.tree.addTopLevelItem(root)

        self.setCentralWidget(self.tree)             

app = QApplication(sys.argv)

tp = TreeWidget()

tp.show()

app.exec_()
