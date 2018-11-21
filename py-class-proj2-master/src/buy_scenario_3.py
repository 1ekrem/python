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

baseURL = "http://magento2-demo.nexcess.net/"

driver.get(baseURL)

gear_tab = "[href='http://magento2-demo.nexcess.net/gear.html']"

driver.find_element(By.CSS_SELECTOR, gear_tab).click()
driver.find_element_by_link_text("Watches").click()

# Find the highest rated item in the section and select the item. 
items = driver.find_elements(By.CSS_SELECTOR, "[class = 'item product product-item']")
items_rating = []
for item in items:
    try:
        item_name = item.find_element_by_css_selector("[class = 'product-item-link']")
        print(item_name.text)
        item_rating = item.find_element_by_css_selector("[class = 'rating-result']").get_attribute("title")
        print(item_rating)
        items_rating.append(item_rating)
        highest_rated_item = max(items_rating) 
        if item_rating == highest_rated_item:
            print("Found the highest rated item :", highest_rated_item, "-", item_name.text)
            highest_rated_item_locator = driver.find_element(By.CSS_SELECTOR, "[class = 'product-item-info']")
            highest_rated_item_locator.click()
            print("Highest rated item is selected!")
    except exceptions.StaleElementReferenceException:
        pass

# Type Quantity
quantity_locator = driver.find_element_by_id("qty")
quantity_locator.clear()
random_nr = random.randint(1,5)
quantity_locator.send_keys(random_nr)
print("Quantity is added")

# Click Add to Cart
add_to_cart_locator = driver.find_element_by_id("product-addtocart-button")
add_to_cart_locator.click()
print("Item(s) are sent to the Shopping Cart")

# Click Checkout Box
__checkout_box_selector = (By.CSS_SELECTOR, "a.action.showcart")
checkout_box_locator = driver.find_element(__checkout_box_selector)
checkout_box_locator.click()

# Click Go to Checkout    
__go_to_checkout_selector = (By.CSS_SELECTOR, "button#top-cart-btn-checkout")
go_to_checkout_locator = driver.find_element(__go_to_checkout_selector)
go_to_checkout_locator.click()




    
        

