# !/usr/bin/python
import sys
import re
from PyQt4.QtGui import *
from PyQt4.QtCore import *

layer = locals()
class TreeWidget(QMainWindow):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setWindowTitle('TreeWidget')
        self.tree = QTreeWidget()
        self.tree.setColumnCount(1)
        self.tree.setHeaderLabels(['contents'])
        items = self.get_data()

        for i in items:
            layer['layer%s' % (items[i][0]-1)] = items[i][0]-1
        for child in range(0,len(items)):
            if child == 0 :
                layer['layer%s'%items[child][0]] = QTreeWidgetItem(self.tree)
                layer['layer%s'%items[child][0]].setText(0,items[child][1])
            else:
                layer['layer%s'%items[child][0]] = QTreeWidgetItem(layer['layer%s'%(items[child][0]-1)])
                layer['layer%s'%items[child][0]].setText(0,items[child][1])
        self.tree.addTopLevelItem(layer1)
        self.setCentralWidget(self.tree)   

    def read_file(self): 
       BLOCK_SIZE = 2048
       with open('test.xml', 'rb') as f: 
           while True: 
               block = f.read(BLOCK_SIZE) 
               if block: 
                   yield block 
               else: 
                   return

    def get_data(self):
        strs = ''
        for i in self.read_file():
            strs += i.decode('utf-8')    
        result = re.sub('\t+<\t*|\t+/>\t*','',strs)
        item = {}
        i = 0
        for s in result.split('\r\n'):
            if s!='':
                reg=re.compile("\t")
                length=len(reg.findall(s))
                item[i] = [length,s.replace('\t','')]
                i+=1
        return item
      
app = QApplication(sys.argv)
tp = TreeWidget()
tp.show()
app.exec_()
