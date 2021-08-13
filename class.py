import requests
from bs4 import BeautifulSoup
'''r1=requests.get("https://www.google.com/")
print(r1)
help(r1)'''
'''r2=requests.get("https://realpython.com/lru-cache-python/.html")
write1=open("/Users/mac/Desktop/mamun1","w",encoding="utf-8")
write1.write(r2.text)
write1.close()'''
'''r=requests.get("https://web.facebook.com/?_rdc=1&_rdr.html","wb")
write1=open("/Users/mac/Desktop/my_fb","w",encoding="utf-8")
write1.write(r.text)
write1.close()
print("done")'''
html=requests.get("https://realpython.com/beautiful-soup-web-scraper-python/")
soup=BeautifulSoup(html.text)
print(soup)
data=soup.find_all("")

