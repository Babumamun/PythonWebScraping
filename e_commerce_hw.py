import selenium
import pandas as pd
from tqdm import tqdm
from selenium import webdriver as wb
webD=wb.Chrome('/Users/mac/Desktop/chromedriver')
webD.get('https://webscraper.io/test-sites/e-commerce/static')
clickObj=webD.find_element_by_xpath('//*[@id="side-menu"]/li[2]/a')
clickObj.click()
webD.find_element_by_xpath('//*[@id="side-menu"]/li[2]/ul/li[1]/a').click()
ll=webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div')
productInfoList=webD.find_elements_by_class_name('thumbnail')
listOflinks=[]
for el in productInfoList:
    ppp1=el.find_elements_by_tag_name('h4')[-1]
    pp2=ppp1.find_element_by_tag_name('a')
    listOflinks.append(pp2.get_property('href'))

listOflinks=[]
condition=True
while condition:
    productInfoList=webD.find_elements_by_class_name('thumbnail')
    for el in productInfoList:
        ppp1=el.find_elements_by_tag_name('h4')[-1]
        pp2=ppp1.find_element_by_tag_name('a')
        listOflinks.append(pp2.get_property('href'))
    try:
#         webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/ul/li[13]/a').click()
        kk= webD.find_elements_by_class_name('page-link')[-1]
        print (kk.get_attribute('aria-label'))
        if kk.get_attribute('aria-label')== 'Next »':
            kk.click()
        else:
            condition=False
    except:
        condition=False



alldetails=[]
for i in tqdm(listOflinks):
    webD.get(i)
    nameoftheproduct=webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[2]').text
    descriptionOfProduct=webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/p').text
    priceProduct=webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[1]').text
    reviewOftheProduct=webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[3]/p').text
    tempJ={'nameoftheproduct':nameoftheproduct,
      'priceProduct':priceProduct,
      'reviewOftheProduct':reviewOftheProduct,
      'descriptionOfProduct':descriptionOfProduct,
      'linkofProduct':i}
    alldetails.append(tempJ)

result=pd.DataFrame(alldetails)
print(result)
result.to_csv('/Users/mac/Desktop/result.csv')
