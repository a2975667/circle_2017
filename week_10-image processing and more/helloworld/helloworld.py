# -*- coding: cp950 -*-
import helloworld_ui
import sys
import qtpy
from helloworld_ui import Ui_MainWindow
from qtpy import *
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        '''
        UI�s��function

        old API
        QtCore.QObject.connect(self.�s����UI�W�l,QtCore.SIGNAL("�s�ʰʧ@"),self.�s�ʪ�fun�W�l)

        new API
        self.�s����UI�W�l.clicked.connect(self.�s�ʪ�fun�W�r)
        '''
        #old API
        #QtCore.QObject.connect(self.Button1_name, QtCore.SIGNAL("clicked()"), self.label_change1) 

        #new API
        self.Button1_name.clicked.connect(self.label_change1)

        self.Button2_name.clicked.connect(self.label_change2)
    def label_change1(self): 
        self.label_name.setText('hello world')
    def label_change2(self): 
        self.label_name.setText('good job') 
 
if __name__ == '__main__':
    app = helloworld_ui.QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
