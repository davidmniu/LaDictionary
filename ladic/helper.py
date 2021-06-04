import os
import sys
from bs4 import BeautifulSoup
import requests
import re
import string
import platform

from PyQt6.QtWidgets import QMessageBox

from definitions import TEX_PATH, TEX_DIR

def getData(word):
    word = cleanWord(word)
    site = requests.get("https://www.dictionary.com/browse/" + word)

    # cook the soup!
    soup = BeautifulSoup(site.text, "html.parser")

    # Data for proEdit 
    pron = soup.select('span[class*="pron-spell-content"]')[0]
    for bold in pron.find_all("span", attrs={"class":"bold"}):
        bold.insert(0, "'")
    pron = pron.text[2:-2]

    # Data for defView
    defs = soup.find("div", attrs={'class':'css-1avshm7 e16867sm0'})
    defDict = {}
    for i in defs.find_all("section", attrs={'class':'css-pnw38j e1hk9ate4'}):
        # types of words
        wordType = i.select('span[class*="e1hk9ate2"]')[0].text.capitalize().translate(str.maketrans('', '', string.punctuation))
        defDict[wordType] = []
        # definitions
        for j in i.select('div[class*="e1q3nk1v2"]'):
            defDict[wordType].append(re.split(r":|\.", j.text, 3)[0])

    return [pron, defDict]

# quick function to display message boxes
def msgBox(self, text):
    box = QMessageBox(self)
    box.setText(text)
    box.exec()

# function to format word from searchEdit
def cleanWord(word):
    return word.strip().lower().capitalize()

def validateWord(self, word):
    # check that word is not already in dictionary
    #with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/latex/dictionary.tex", "r") as file:
    with open(TEX_PATH) as file:
        for line in file:
            if word in line:
                msgBox(self, "Error: word already in dictionary")
                return

    # get pronunciation, various definitions + types of words
    word = word.replace(" ", "-")
    try:
        site = requests.get("https://www.dictionary.com/browse/" + word)
    except requests.exceptions.ConnectionError:
        msgBox(self, "Error: can't connect to Dictionary.com (check your WiFi)")
        return

    # check that word is correctly spelled
    if "misspelling" in site.url or "noresult" in site.url:
        msgBox(self, "Error: incorrect spelling")
        return

    return True

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
    os.replace(TEX_DIR + "~dictionary.tex", TEX_PATH)

def makePDF():
    system = platform.system()
    if system == "Windows":
        pass
    else if system == "Linux" or system == "Darwin":
        os.system("pdflatex -output-directory "  + TEX_DIR + ' ' + TEX_PATH)
