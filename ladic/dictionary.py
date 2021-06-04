import os
import sys
from bs4 import BeautifulSoup
import requests
import re
import string

from definitions import TEX_PATH

def getData(word):
    word = word.strip().lower().capitalize() 

    # check that word is not already in dictionary
    #with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/latex/dictionary.tex", "r") as file:
    with open(TEX_PATH) as file:
        for line in file:
            if word in line:
                raise TypeError

    # get pronunciation, various definitions + types of words
    word = word.replace(" ", "-")
    site = requests.get("https://www.dictionary.com/browse/" + word)

    # check that word is correctly spelled
    if "misspelling" in site.url or "noresult" in site.url:
        raise ValueError

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
