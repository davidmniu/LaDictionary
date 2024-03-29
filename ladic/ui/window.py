# Form implementation generated from reading ui file 'designer/window.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(583, 736)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.searchFrame = QtWidgets.QFrame(self.centralwidget)
        self.searchFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.searchFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.searchFrame.setObjectName("searchFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.searchFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.searchLabel = QtWidgets.QLabel(self.searchFrame)
        self.searchLabel.setObjectName("searchLabel")
        self.horizontalLayout_3.addWidget(self.searchLabel)
        self.searchEdit = QtWidgets.QLineEdit(self.searchFrame)
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout_3.addWidget(self.searchEdit)
        self.verticalLayout.addWidget(self.searchFrame)
        self.proFrame = QtWidgets.QFrame(self.centralwidget)
        self.proFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.proFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.proFrame.setObjectName("proFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.proFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.proLabel = QtWidgets.QLabel(self.proFrame)
        self.proLabel.setObjectName("proLabel")
        self.horizontalLayout_2.addWidget(self.proLabel)
        self.proEdit = QtWidgets.QLineEdit(self.proFrame)
        self.proEdit.setObjectName("proEdit")
        self.horizontalLayout_2.addWidget(self.proEdit)
        self.verticalLayout.addWidget(self.proFrame)
        self.defView = QtWidgets.QTreeView(self.centralwidget)
        self.defView.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.defView.setObjectName("defView")
        self.verticalLayout.addWidget(self.defView)
        self.buttonFrame = QtWidgets.QFrame(self.centralwidget)
        self.buttonFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.buttonFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.buttonFrame.setObjectName("buttonFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttonFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clearButton = QtWidgets.QPushButton(self.buttonFrame)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.saveButton = QtWidgets.QPushButton(self.buttonFrame)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.verticalLayout.addWidget(self.buttonFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 583, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPDF = QtGui.QAction(MainWindow)
        self.actionPDF.setObjectName("actionPDF")
        self.actionMove = QtGui.QAction(MainWindow)
        self.actionMove.setObjectName("actionMove")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionPDF)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LaDictionary"))
        self.searchLabel.setText(_translate("MainWindow", "Search:"))
        self.proLabel.setText(_translate("MainWindow", "Pronunciation:"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionPDF.setText(_translate("MainWindow", "Open PDF"))
        self.actionMove.setText(_translate("MainWindow", "Move"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
