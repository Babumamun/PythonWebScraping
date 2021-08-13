import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup
source=requests.get("https://openpyxl.readthedocs.io/en/stable/").text
soup=BeautifulSoup(source,"lxml")
body=soup.find("div",id="openpyxl-a-python-library-to-read-write-excel-2010-xlsx-xlsm-files")
header=body.h1.text
print(header)
#print(header)
tabel=body.table.text
#print(tabel)
introduction=body.find("div",id='introduction').text
#print(introduction)
security=body.find("div",id="security").text
#print(security)
mailing_list=body.find("div",id="mailing-list").text
#print(mailing_list)
documentation=body.find("div",id="documentation").text
#print(documentation)
support=body.find("div",id="support").text
#print(support)
how_to_contribute=body.find("div",id="how-to-contribute").text
#print(how_to_contribute)
installation=body.find("div",id="installation").text
#print(installation)
usage_examples=body.find("div",id="usage-examples").text
#print(usage_examples)
performance=body.find("div",id="performance").text
#print(performance)
other_topics=body.find("div",id="other-topics").text
#print(other_topics)
information_for_developers=body.find("div",id="information-for-developers").text
#print(information_for_developers)
api_documentation=body.find("div",id="api-documentation").text
#print(api_documentation)
op_File =open("/Users/mac/Desktop/my_text.txt", "a")
op_File.write(header+tabel+introduction+security+mailing_list+
              documentation+support+how_to_contribute+installation+
              usage_examples+performance+other_topics+
              information_for_developers+api_documentation)
print('data save Success!')

'''
op_File =open("/Users/mac/Desktop/new_text.txt", "a")
op_File.write(title+head_text+tex_p+str(all_links))
print('Data save Success!')
op_File.close()'''





