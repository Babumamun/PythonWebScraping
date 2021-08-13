'''x = ['a', 'b', {'foo': 1, 'bar': {'x': 10, 'y': 20, 'z': 30},
'baz': 3}, 'c', 'd']
print(len(x))
print(x[2][3][2])'''
#import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
path="/Users/mac/Desktop/chromedriver"
driver=webdriver.Chrome(path)
#driver.get('https://techwithtim.net')
driver.get('https://www.bing.com/')
tittle=driver.title
print(tittle)
#time.sleep()
WebDriverWait(driver,10).until(expected_conditions)
#driver.quit()
