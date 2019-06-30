from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()


URL = "https://freecrm.com/"
driver.get(URL)
time.sleep(3)
driver.find_element_by_xpath("//span[text()='Log In']").click()
time.sleep(3)
driver.find_element_by_css_selector('input[name="email"]').send_keys("burhannyc@aol.com")
driver.find_element_by_css_selector('input[name="password"]').send_keys("Selenium123")
driver.find_element_by_css_selector('.ui.fluid.large.blue').click()
time.sleep(3)

print(driver.find_element_by_css_selector('.user-display').text)
time.sleep(1)
driver.close()