# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dictionaryGUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searchbar = QtWidgets.QTextEdit(self.centralwidget)
        self.searchbar.setGeometry(QtCore.QRect(80, 40, 331, 31))
        self.searchbar.setObjectName("searchbar")
        self.proLabel = QtWidgets.QLabel(self.centralwidget)
        self.proLabel.setGeometry(QtCore.QRect(80, 100, 91, 16))
        self.proLabel.setObjectName("proLabel")
        self.proEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.proEdit.setGeometry(QtCore.QRect(170, 90, 331, 31))
        self.proEdit.setObjectName("proEdit")
        self.defLabel = QtWidgets.QLabel(self.centralwidget)
        self.defLabel.setGeometry(QtCore.QRect(80, 140, 91, 16))
        self.defLabel.setObjectName("defLabel")
        self.defTree = QtWidgets.QTreeWidget(self.centralwidget)
        self.defTree.setGeometry(QtCore.QRect(80, 160, 256, 192))
        self.defTree.setObjectName("defTree")
        self.defTree.headerItem().setText(0, "1")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(90, 410, 93, 28))
        self.saveButton.setObjectName("saveButton")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(220, 410, 93, 28))
        self.clearButton.setObjectName("clearButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.proLabel.setText(_translate("MainWindow", "Pronunciation:"))
        self.defLabel.setText(_translate("MainWindow", "Definitions:"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
