import os
from bs4 import BeautifulSoup
import requests
import re
import textwrap

def printDef(defList, index):
    print(tab + str(index + 1) + ". ", end="") 
    print(*textwrap.TextWrapper(width=70).wrap(defList[index+1]), 
        sep=("\n" + tab + str((len(str(index+1)) + 2)*' ')))

# Get input
word = input("Enter vocabulary word (or press [enter] to exit): ").lower()
while word != '':
    word = word.capitalize()

    # check if word is in dictionary
    found = False
    with open("dictionary.tex", "r") as file:
        for line in file:
            if word in line:
                found = True
                print("'" + word + "' is already in dictionary")
                break

    if found == True:
        word = input("Enter vocabulary word (or press [enter] to exit): ").lower()
        continue

    # initialize output string
    output = "\t\\entry{" + word + "}{}{}{"

    # get pronunciation, various definitions + types of words
    word = word.replace(" ", "-")
    url = requests.get("https://www.dictionary.com/browse/" + word)
    soup = BeautifulSoup(url.text, "html.parser")
    # pronunciation

    defs = soup.find("div", attrs={'class':'css-1avshm7 e16867sm0'})
    count = 1
    tab = 4*' '

    defList = []
    for i in defs.find_all("section", attrs={'class':'css-pnw38j e1hk9ate4'}):
        # types of words
        print(i.select('span[class*="e1hk9ate2"]')[0].text.capitalize())
        # definitions
        for j in i.select('div[class*="e1q3nk1v2"]'):
            print(tab + str(count) + ". ", end="") 
            defList.append(re.split(r":|\.", j.text, 3)[0])
            print(*textwrap.TextWrapper(width=70).wrap(defList[count-1]), 
                    sep=("\n" + tab + str((len(str(count)) + 2)*' ')))
            count += 1

    # select user input
    num = 0
    choices = []
    string = input("Enter desired definition indices, comma separated (or press [enter] to skip): ")
    #while string != "":
    try:
        if string != "":
            choices = [int (x) for x in string.strip().split(',')]
        # TODO: error handling
    except:
        print("Invalid input!")
    
    # create output string
    choices.sort()
    for i in choices:
        #printDef(defList, i)
        output += "\t" + defList[i-1]
        if (i < len(choices)):
            output += "\n\t$\\bullet$\n"
    output += "}"
    print(output)
    
    # linear search to find where data should be entered
    file = open("dictionary.tex", "r")
    count = 0
    outLine = 0
    prevWord = ""
    currWord = ""
    while True:
        count += 1
        line = file.readline()
     
        # if line is empty
        # end of file is reached
        if not line:
            print("Enter at line " + str(count - 1))
            break

        line = line.strip()
        if (line[1:6] == "entry"):
            currWord = re.split(r"\\entry{|}", line, 3)[1]
            if (word > prevWord and word < currWord):
                if (word[:1] < currWord[:1]):
                    output.prepend("\n")
                    outLine = count - 4
                else:
                    outLine = count
                print("Enter at line " + str(outLine))
                break
            else:
                prevWord = currWord
    file.close()

    # modify file
    if False:
        with open("dictionary.tex", "r") as file:
            contents = file.readlines()

        contents.insert(outLine, output)

        with open("dictionary.tex", "w") as file:
            contents = "".join(contents)
            file.write(contents)

    # execute pdflatex
    if False:
        os.system("pdflatex dictionary.tex")
    word = input("Enter vocabulary word (or press [enter] to exit): ").lower()
