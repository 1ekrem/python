from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *

driver = webdriver.Firefox()
driver.get("https://google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("python")

search_box.find_element(By.NAME, "btnK").click()
#search_box.send_keys(Keys.ENTER)

# wait = WebDriverWait(driver,
#                      10,
#                      poll_frequency=1,
#                      ignored_exceptions=[NoSuchElementException,
#                                          ElementNotVisibleException,
#                                          ElementNotSelectableException])

# first_div = wait.until(
#     expected_conditions.presence_of_element_located(
#         (By.CSS_SELECTOR, "div.bkWMgd:first-child")
#     )
# )

# links = first_div.find_elements(By.CSS_SELECTOR, "a")
# for link in links:
#     if link.text:
#         print(link.text, link.get_attribute("href"))

#driver.close()