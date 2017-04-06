# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helloworld_ui.ui'
#
# Created: Sun Aug 09 01:08:34 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(651, 415)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_name = QtGui.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(30, 60, 511, 141))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Devanagari"))
        font.setPointSize(72)
        self.label_name.setFont(font)
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.Button1_name = QtGui.QPushButton(self.centralwidget)
        self.Button1_name.setGeometry(QtCore.QRect(50, 290, 111, 71))
        self.Button1_name.setObjectName(_fromUtf8("Button1_name"))
        self.Button2_name = QtGui.QPushButton(self.centralwidget)
        self.Button2_name.setGeometry(QtCore.QRect(220, 290, 111, 71))
        self.Button2_name.setObjectName(_fromUtf8("Button2_name"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_name.setText(_translate("MainWindow", "TextLabel", None))
        self.Button1_name.setText(_translate("MainWindow", "helloworld", None))
        self.Button2_name.setText(_translate("MainWindow", "good job", None))

