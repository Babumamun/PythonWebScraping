import requests
from bs4 import BeautifulSoup

def getHtml(keyword,begin):
    addr = f'https://cn.bing.com/search?q={keyword}'
    print(addr)
    html = requests.get(addr)
    return html

html = getHtml("selenium",11)
with open("test.html","w",encoding = "utf-8")  as wf:
    wf.write(html.text)
