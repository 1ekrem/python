from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.tradingview.com/"
driver.get(url)

#list of header items

headerItems = "li.tv-mainmenu__item"

#print(driver.find_element_by_css_selector(headerItems).text)

web_tabs = []
for item in driver.find_elements_by_css_selector(headerItems):
    web_tabs.append(item.text)
    
for i in web_tabs:
    print(i)

hidden_elements = 'ul.i-hidden'


driver.quit()