import os
import sys
from bs4 import BeautifulSoup
import requests
import re
import textwrap

def getData(word):
    word = word.lower().capitalize() 
    with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/latex/dictionary.tex", "r") as file:
        for line in file:
            if word in line:
                # print("'" + word + "' is already in dictionary")
                return None

    # get pronunciation, various definitions + types of words
    word = word.replace(" ", "-")
    site = requests.get("https://www.dictionary.com/browse/" + word)

    if "misspelling?term" in site.url:
        raise ValueError

    soup = BeautifulSoup(site.text, "html.parser")
    # pronunciation
    pron = soup.select('span[class*="pron-spell-content"]')[0]
    for bold in pron.find_all("span", attrs={"class":"bold"}):
        bold.insert(0, "'")
    pron = pron.text[2:-2]

    defs = soup.find("div", attrs={'class':'css-1avshm7 e16867sm0'})
    tab = 4*' '

    defDict = {}
    for i in defs.find_all("section", attrs={'class':'css-pnw38j e1hk9ate4'}):
        # types of words
        wordType = i.select('span[class*="e1hk9ate2"]')[0].text.capitalize()
        defDict[wordType] = []
        # definitions
        for j in i.select('div[class*="e1q3nk1v2"]'):
            defDict[wordType].append(re.split(r":|\.", j.text, 3)[0])

    return [pron, defDict]
