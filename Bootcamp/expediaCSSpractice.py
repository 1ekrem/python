from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)

driver.get("https://www.expedia.com/")
flight = driver.find_element(By.LINK_TEXT, "Flights")
flight.click()

one_way = driver.find_element(By.CSS_SELECTOR, "#flight-type-one-way-label-flp")
one_way.click()

flying_from =  driver.find_element(By.CSS_SELECTOR, "#flight-origin-flp")
flying_from.clear()
flying_from.send_keys("Miami")