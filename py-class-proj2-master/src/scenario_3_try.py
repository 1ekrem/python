from selenium import webdriver
from selenium.webdriver.common.by import By
import logger
import time
import random
from selenium.common import exceptions

from ShopTester import ShopTester
from utils import stringify_links, filter_by_text
import util_excel as utex
import ShopItemPage 

# Create a webdriver instance
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

sleep = time.sleep(3)

baseURL = "http://magento2-demo.nexcess.net/"
driver.get(baseURL)

gear_tab = "[href='http://magento2-demo.nexcess.net/gear.html']"
driver.find_element(By.CSS_SELECTOR, gear_tab).click()
driver.find_element_by_link_text("Watches").click()

# Find the highest rated item in the section and select the item. 
items = driver.find_elements(By.CSS_SELECTOR, "[class = 'item product product-item']")
items_rating = []
for item in items:
        item_name = item.find_element_by_css_selector("[class = 'product-item-link']")
        print(item_name.text)
        item_rating = item.find_element_by_css_selector("[class = 'rating-result']").get_attribute("title")
        items_rating.append(item_rating)
        print(item_rating)
print(items_rating)
print(min(items_rating))
if item_rating == min(items_rating):
        print("Found the highest rated item :", min(items_rating), "-", item_name.text)
        highest_rated_item_locator = driver.find_element(By.LINK_TEXT, item_name.text)
        highest_rated_item_locator.click()
        print("Highest rated item is selected!")