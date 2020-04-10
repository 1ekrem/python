from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

baseUrl = "https://system.netsuite.com/app/login/secure/enterpriselogin.nl?whence="

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get(baseUrl)

driver.find_element_by_name('email').sendkeys("test1@pcsww.com")