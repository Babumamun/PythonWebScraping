import requests
from bs4 import BeautifulSoup

address = ["https://openpyxl.readthedocs.io/en/stable/development.html",
           "https://openpyxl.readthedocs.io/en/stable/development.html#coding-style"]

aList = []

for item in address:
    h1 = requests.get(item)
    if h1.status_code != 200:
        print("the website is not exist or error")
    else:
        h1_soup = BeautifulSoup(h1.text)
        h2_soup = h1_soup.find("div", {"itemprop": "articleBody"})
        h3_soup = h2_soup.find_all("div", {"class": "section"})

        for items in h3_soup:

            titletag = items.find_all("h1")
            if titletag != []:
                print(titletag[0].get_text())
                aList.append(titletag[0].string)

            tagitem = items.find_all("h2")
            if tagitem != []:
                print(tagitem[0].get_text())
                aList.append(tagitem[0].string)

            pList = []
            pageitem = items.find_all("p")
            for pitem in pageitem:
                pList.append(pitem.string)
            aList.append(pList)

print(aList)
wfile = open("openpyxldoc.txt", "w", encoding=h1.encoding)
for item in aList:
    if item != None:
        if isinstance(item, list):
            for child_item in item:
                if child_item != None:
                    wfile.write(child_item + "\n")
        else:
            wfile.write(item + "\n")
wfile.close()





