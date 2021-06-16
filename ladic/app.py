import sys
import os
import subprocess
import platform
import re
import requests

# from PyQt6 import QtCore, QtGui, QtWidgets
# from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QAbstractItemView

from ladic.helper import getData, msgBox, cleanWord, validateWord, formatDefi, writeTeX
from ladic.ui.window import Ui_MainWindow

from paths import TEX_PATH, TEX_DIR, PDF_PATH, EXE_ROOT_DIR, ROOT_DIR

def validateIndices(self):
    indices = self.defView.selectionModel().selectedIndexes()
    if not indices:
        msgBox(self, "Error: must select at least one definition")
        return

    parent = QStandardItemModel.parent(self.defView.model(), indices[0])
    defList = [self.defView.model().itemFromIndex(indices[0]).text()]
    for i in indices[1:]:
        defList.append(self.defView.model().itemFromIndex(i).text())
        if  QStandardItemModel.parent(self.defView.model(), i) != parent:
            msgBox(self, "Error: cannot select definitions from multiple lexical categories")
            return
    return [parent, defList]

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon(os.path.join(ROOT_DIR, "ladic.ico")))
        self.setupUi(self)

        # set model for defView
        self.defModel = QStandardItemModel()
        self.defView.setModel(self.defModel)
        # allow multiple selection
        self.defView.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        # self.defView.setHeaderHidden(True)

        # connect buttons and enter key for search bar
        self.searchEdit.returnPressed.connect(self.updateData)
        self.clearButton.pressed.connect(self.clear)
        self.saveButton.pressed.connect(self.save)
        self.actionPDF.triggered.connect(self.viewPDF)
        self.actionAbout.triggered.connect(self.openAbout)

        self.show()


    # function to populate proEdit and defView
    def updateData(self):
        word = cleanWord(self.searchEdit.text())
        if not validateWord(self, word):
           return
       
        try:
            data = getData(word)
        except Exception as e:
            msgBox(self, "Error:" + str(e))
            return

        pro = data[0]
        defs = data[1]
        self.searchEdit.setText(word.lower())
        self.proEdit.setText(pro)
        self.defModel.clear()

        self.defModel.setHorizontalHeaderLabels(["Definitions"])
        parentItem = self.defModel.invisibleRootItem()
        count = 1
        for key in defs:
            category = QStandardItem(str(key))
            category.setSelectable(False)
            for i in defs[key]:
                element = QStandardItem(str(count) + ". " + str(i))
                element.setEditable(True)
                category.appendRow(element)
                count += 1
            parentItem.appendRow(category)
        self.defModel.layoutChanged.emit()
        self.defView.expandAll()

    # function to save definition in LaTeX file
    def save(self):
        word = cleanWord(self.searchEdit.text())
        if not validateIndices(self) or not validateWord(self, word):
            return
        else:
            parent = validateIndices(self)[0]
            defList = validateIndices(self)[1]

        word = cleanWord(self.searchEdit.text())
        letter = word[:1]
        pro = self.proEdit.text().strip()
        output = "\t\\entry{" + word + "}{" + pro + "}{" + self.defView.model().itemFromIndex(parent).text().strip() + "}{"
        for i in defList[0:-1]:
            output += formatDefi(self, i) + "\n\t$\\bullet$\n\t"
        output += formatDefi(self, defList[-1]) + '}'

        # linear search to find where data should be entered
        file = open(TEX_PATH, "r")
        count = 0
        outLine = 0
        prevWord = ""
        currWord = ""
        while True:
            count += 1
            line = file.readline()
         
            # if line is empty then EOF is reached
            if not line:
                if letter > currWord[:1]: # empty file or new letter
                    output = "\n\\section*{" + letter + "}\n\\begin{multicols}{2}\n" + output + "\n\\end{multicols}\n"
                else: # same letter
                    output = "\n" + output + "\n"
                count -= 1
                break

            # line is not empty, so continue formatting
            line = line.strip()

            if (line[1:6] == "entry"): # if line is an entry
                currWord = re.split(r"\\entry{|}", line, 3)[1]
                # if word is between two entries or beginning of nonempty dictionary
                if (word > prevWord and word < currWord):
                    # word is last of its letter
                    if (letter  < currWord[:1]):
                        # word is first of its letter, aka new letter
                        if (letter > prevWord[:1]):
                            output = "\n\\section*{" + letter + "}\n\\begin{multicols}{2}\n" + output + "\n\\end{multicols}"
                            count -= 3
                        # last of nonempty set of words beginning with same letter
                        else:
                            output = "\n" + output
                            count -= 4
                    # beginning / middle of sets of words beginning with same letter
                    else:
                        output += "\n"
                    output += "\n"
                    break
                # word has not been placed
                else:
                    prevWord = currWord
        file.close()
        writeTeX(output, count)
        subprocess.call("pdflatex -output-directory "  + TEX_DIR + ' ' + TEX_PATH, shell=True)

    # clear all
    def clear(self):
        self.defModel.clear()
        self.searchEdit.clear()
        self.proEdit.clear()

    def viewPDF(self):
        if platform.system() == "Windows":
            subprocess.call("start " + PDF_PATH, shell=True)
        elif platform.system() == "Darwin":
            subprocess.call("open " + PDF_PATH, shell=True)
        elif platform.system() == "Linux":
            subprocess.call("okular " + PDF_PATH + " &", shell=True)

    def openAbout(self):
        site = "https://github.com/davidmniu/LaDictionary"
        if platform.system() == "Windows":
            subprocess.call("start " + site, shell=True)
        elif platform.system() == "Darwin":
            subprocess.call("open " + site, shell=True)
        elif platform.system() == "Linux":
            subprocess.call("xdg-open " + site, shell=True)

# driver function which gets called in main.py
def run():
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec()
