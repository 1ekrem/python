from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import difflib
from openpyxl import load_workbook
from selenium.common.exceptions import *

driver = webdriver.Chrome()
driver.maximize_window()

URL = "https://freecrm.com/"
driver.get(URL)
time.sleep(3)
driver.find_element_by_xpath("//span[text()='Log In']").click()
time.sleep(3)

try:
    driver.find_element_by_css_selector('input[name="mail"]').send_keys("burhannyc@aol.com")
except NoSuchElementException:
    print("Fail to identify email section")

driver.quit()