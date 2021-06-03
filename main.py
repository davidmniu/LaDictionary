import sys
import requests

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QAbstractItemView, QLabel

# from gui import Ui_MainWindow
# from dict import getData
# from ladic import getData
from ladic.dict import getData
from ladic.ui.window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        '''
        self.proModel = QStringListModel()
        self.proView.
        '''

        self.defModel = QStandardItemModel()
        self.defView.setModel(self.defModel)
        self.defView.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.defView.setHeaderHidden(True)

        # self.defView.selectionChanged.connect(self.hideOthers)
        #self.defView.setWordWrap(True)
        #print(self.defView.wordWrap())

        self.searchEdit.returnPressed.connect(self.updateData)
        self.clearButton.pressed.connect(self.clear)
        self.saveButton.pressed.connect(self.save)

        self.show()

    def updateData(self):
        try:
            data = getData(self.searchEdit.text())
        except ValueError:
            box = QMessageBox(self)
            box.setText("Error: incorrect spelling")
            box.exec()
            return
        except requests.exceptions.ConnectionError:
            box = QMessageBox(self)
            box.setText("Error: can't connect to Dictionary.com (check your WiFi)")
            box.exec()
            return
        except Exception as e:
            box = QMessageBox(self)
            box.setText("Error:" + str(e))
            box.exec()
            return

        pro = data[0]
        defs = data[1]
        self.proEdit.setText(pro)
        self.defModel.clear()

        parentItem = self.defModel.invisibleRootItem()
        for key in defs:
            category = QStandardItem(str(key))
            category.setSelectable(False)
            for i in defs[key]:
                element = QStandardItem(str(i))
                element.setEditable(True)
                category.appendRow(element)
            parentItem.appendRow(category)
        self.defModel.layoutChanged.emit()
        self.defView.expandAll()

    def hideOthers(self):
        pass

    def save(self):
        word = searchEdit.text().simplified()
        pro = proEdit.text().simplified()


    def clear(self):
        self.defModel.clear()
        self.searchEdit.clear()
        
app = QApplication(sys.argv)
w = MainWindow()
app.exec()

'''
# Code for message box
box = QMessageBox(self)
box.setText(self.searchEdit.text())
box.exec()
print(getData(self.searchEdit.text()))
'''
