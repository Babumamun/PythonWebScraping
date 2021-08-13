from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver=webdriver.Chrome('/Users/mac/Desktop/chromedriver')
driver.get('https://www.bing.com/')
search_box=driver.find_element_by_xpath('//*[@id="sb_form_q"]')
search_box.send_keys("University")
button_submit=driver.find_element_by_xpath('//*[@id="sb_form"]/label')
button_submit.click()
#time
WebDriverWait(driver,10).until(expected_conditions.title_contains('University'))
html=driver.page_source #we wanna get the new page

#write=open("/Users/mac/Desktop/bing.html",'w',encoding='utf-8')
#write.write(html)

soup=BeautifulSoup(html,'html.parser')
title=soup.title.text
print(title)
h2=soup.find_all("h2")
for heading in h2:
    head_text=heading.text
    print(head_text)
p=soup.find_all("p")
for paragraph in p:
    tex_p=paragraph.text
    print(tex_p)

all_links=set()
a=soup.find_all('a')
for link in a:
    if (link.get('href')!='#'):
        all_links.add(link.get("href"))
        print(all_links)

#write.close()
driver.close()
