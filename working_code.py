from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome("/Users/mac/Desktop/chromedriver")

driver.get("https://cn.bing.com/")

#Enter searching string(keyword)
search_box = driver.find_element_by_xpath('//*[@id="sb_form_q"]')
search_box.send_keys("University")

#click searching button
submit = driver.find_element_by_xpath('//*[@id="sb_form_go"]')
submit.click()
time.sleep(5)

#wait the webpage open
WebDriverWait(driver, 10).until(expected_conditions.title_contains('University'))
print("ok")

page = driver.find_element_by_class_name("sb_pagF")

#get hrefs in a list
mypages = page.find_elements_by_xpath('li/a')

web_address_list =[]
for p in mypages:
    href = p.get_attribute('href')
    if href:
        web_address_list.append(href)

k = 0
for h in web_address_list[:-1]:
    print(h)
    driver.get(h)
    time.sleep(5)
    html_source = driver.page_source
    filename = f"first_file{k}.html"
    with open(filename,"w",encoding = 'utf-8') as wf:
        wf.write(html_source)
    k = k+1

    soup = BeautifulSoup(html_source)