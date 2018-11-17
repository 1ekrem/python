from selenium import webdriver
from selenium.webdriver.common.by import By
import logger
import time
import random

from ShopTester import ShopTester
from utils import stringify_links, filter_by_text
import util_excel as utex

# Create a webdriver instance
driver = webdriver.Chrome()
#driver.maximize_window()

baseURL = "http://magento2-demo.nexcess.net/"

driver.get(baseURL)

gear_tab = "[href='http://magento2-demo.nexcess.net/gear.html']"

driver.find_element(By.CSS_SELECTOR, gear_tab).click()
driver.find_element_by_link_text("Bags").click()
list_items = "[class= 'rating-result']"

print(driver.find_element_by_css_selector(list_items).get_attribute("class"))

for item in list_items:
    print(item)