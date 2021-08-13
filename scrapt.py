import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup
source=requests.get("https://openpyxl.readthedocs.io/en/stable/index.html").content
soup=BeautifulSoup(source,'lxml')
body=soup.find("div",id="openpyxl-a-python-library-to-read-write-excel-2010-xlsx-xlsm-files")
header=soup.body.find("h1").text
table=soup.body.find(class_='docutils field-list').text
introduction=soup.body.find(id="introduction").text
security=soup.body.find(id="security").text
#print(header)
#print(table)
#print(introduction)
#print(security)
'''csv_file=open("/Users/mac/Desktop/result.csv",'w')                '''
'''csv_writer=csv.writer(csv_file)                                   '''
'''csv_writer.writerow(['header','table','introduction','security']) '''
'''csv_writer.writerow([header,table,introduction,security])         '''
'''csv_file.close()                                                  '''
'''                                                                  '''
'''content_of_this_page=pd.DataFrame({"header":header,             '''
'''                                  "table":table,                '''
'''                                  "introduction":introduction,  '''
'''                                  "security":security,          '''
'''                                  })                            '''
'''content_of_this_page.to_csv("/Users/mac/Desktop/result.csv")    '''


#print(indroducation)
#paragrap=soup.find_all('p').text
#print(paragrap)
#aritcal=soup.find_all("h1")
#print(aritcal)
#print(small)
#table=soup.find(class_='docutils field-list').text
#print(table)


#print(m)
#print(soup)
#m="wy-nav-content"