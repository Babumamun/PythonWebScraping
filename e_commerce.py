import selenium
from selenium import webdriver as wb
webD=wb.Chrome('/Users/mac/Desktop/chromedriver')
webD.get('https://webscraper.io/test-sites/e-commerce/static')
clickObj=webD.find_element_by_xpath('//*[@id="side-menu"]/li[2]/a')
clickObj.click()
webD.find_element_by_xpath('//*[@id="side-menu"]/li[2]/ul/li[1]/a').click()
ll=webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div')
print(ll)
productInfoList=webD.find_elements_by_class_name('thumbnail')
listOflinks=[]
for el in productInfoList:
    ppp1=el.find_elements_by_tag_name('h4')[-1]
    pp2=ppp1.find_element_by_tag_name('a')
    listOflinks.append(pp2.get_property('href'))

#webD.find_elements_by_class_name('page-link')[-1].text
'''listOflinks=[]
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
'''
hrefLinkList = []
condition = True
while condition:
    allInfo = webD.find_elements_by_xpath('//*[@class="thumbnail"]')

    for eEle in allInfo:
        hrefLink = eEle.find_elements_by_css_selector('h4')[-1].find_element_by_tag_name('a').get_property('href')
        hrefLinkList.append(hrefLink)
    try:
        webD.find_elements_by_xpath('//*[@class="page-link"]')[-1].click()
    except:
        condition = False
#print(listOflinks)
from tqdm import tqdm
overallinfo=[]
for i in tqdm(hrefLinkList):
    webD.get(i)
    nameOftheProduct=webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[2]').text
    priceoftheProduct=webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[1]').text
    descOfProduct=webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/p').text
    revOfProduct=webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[3]/p').text
    ("/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[3]/p")
    tempJ={'nameOftheProduct':nameOftheProduct,
          'priceoftheProduct':priceoftheProduct,
          'descOfProduct':descOfProduct,
          ' revOfProduct': revOfProduct,
          'hyperlink':i}
    overallinfo.append(tempJ)


#print(overallinfo)
'''op_File =open("/Users/mac/Desktop/e_commerce.txt", "a")
op_File.write(nameOftheProduct+priceoftheProduct+descOfProduct+i)
print('data save Success!')'''
import pandas as pd
result=pd.DataFrame(overallinfo)
result.to_csv('mamun.csv')
print('done!')


