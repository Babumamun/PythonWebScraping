import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from string import ascii_lowercase
i=1
def make_soup(url):
    thepage= urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

soup = make_soup("https://www.airbnb.co.uk/s/Ljubljana--Slovenia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&query=Ljubljana%2C%20Slovenia&place_id=ChIJ0YaYlvUxZUcRIOw_ghz4AAQ&checkin=2020-11-01&checkout=2020-11-08&source=structured_search_input_header&search_type=autocomplete_click")
for img in soup.findAll('img'):
    temp=img.get('src')
    if temp[:1]=="/":
        image = "https://www.airbnb.co.uk/s/Ljubljana--Slovenia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&query=Ljubljana%2C%20Slovenia&place_id=ChIJ0YaYlvUxZUcRIOw_ghz4AAQ&checkin=2020-11-01&checkout=2020-11-08&source=structured_search_input_header&search_type=autocomplete_click" + temp
    else:
        image = temp

    print(image)

    nametemp = img.get('alt')
    if len(nametemp)==0:
        filename=str(i)
        i=i+1
    else:
        filename=nametemp


    imagefile = open(filename + ".jpeg", 'wb')
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()
