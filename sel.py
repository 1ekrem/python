from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from selenium.common import exceptions

url = 'https://www.roomster.com/'
driver = webdriver.Chrome()
driver.get(url)

selectEntirePlace = "entire place"
xselectEntirePlace = "//span[@data-id="'button-HaveApartment'"]"
selectEntirePlace2= driver.find_element_by_xpath(xselectEntirePlace).get_attribute('data-id')

# text2=driver.find_element_by_xpath(xselectEntirePlace).text

# if text2 == selectEntirePlace:
#     print("PASS")

driver.find_element_by_xpath(xselectEntirePlace).get_attribute('data-id')

