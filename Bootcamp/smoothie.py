from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
baseURL = "https://tasty.co/recipe/cucumber-apple-mint-smoothie"

driver.get(baseURL)

listed_item = driver.find_element_by_class_name("xs-mb1 xs-mt0")

print(listed_item.text)