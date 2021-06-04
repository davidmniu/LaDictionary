import sys
import os
import requests
import re
import platform

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QAbstractItemView, QLabel, QFrame

from ladic.dictionary import getData
from ladic.ui.window import Ui_MainWindow

from definitions import TEX_PATH, TEX_DIR, PDF_PATH

# quick function to display message boxes
def msgBox(self, text):
    box = QMessageBox(self)
    box.setText(text)
    box.exec()

# function to format word from searchEdit
def cleanWord(word):
    return word.strip().lower().capitalize()

def writeTeX(text, line):
    line -= 1
    inFile = open(TEX_PATH, 'r')
    outFile = open(TEX_DIR + "~dictionary.tex", 'w')
    content = inFile.readlines()
    outFile.writelines(content[:line])
    outFile.write(text)
    outFile.writelines(content[line:])
    outFile.close()
    inFile.close()
    os.replace(TEX_PATH, TEX_DIR + "~dictionary.tex")

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
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

        self.show()

    # function to populate proEdit and defView
    def updateData(self):
        word = cleanWord(self.searchEdit.text())
        try:
            data = getData(word)
        except TypeError:
            msgBox(self, "Error: word already in dictionary")
            return
        except ValueError:
            msgBox(self, "Error: incorrect spelling")
            return
        except requests.exceptions.ConnectionError:
            msgBox(self, "Error: can't connect to Dictionary.com (check your WiFi)")
            return
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

        word = cleanWord(self.searchEdit.text())
        letter = word[:1]
        pro = self.proEdit.text().strip()
        output = "\t\\entry{" + word + "}{" + pro + "}{" + self.defView.model().itemFromIndex(parent).text().strip() + "}{"
        for i in defList[0:-1]:
            output += i.split('.')[1].strip() + "\n\t$\\bullet$\n\t"
        output += defList[-1].split('.')[1].strip() + '}'

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
                writeTeX(output, count)
                # print("Enter at line " + str(count) + ":")
                # print(output)
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
                    writeTeX(output, count)
                    # print("Enter at line " + str(count))
                    # print(output)
                    break
                # word has not been placed
                else:
                    prevWord = currWord
        file.close()

        if False:
            os.system("pdflatex -output-directory "  + TEX_DIR + ' ' + TEX_PATH)

    # clear all
    def clear(self):
        self.defModel.clear()
        self.searchEdit.clear()
        self.proEdit.clear()

    def viewPDF(self):
        if platform.system() == "Windows":
            os.system("explorer.exe " + PDF_PATH)
        elif platform.system() == "Linux":
            os.system("okular " + PDF_PATH + " &")

# driver function which gets called in main.py
def run():
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec()
