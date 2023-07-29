from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
#from selenium.webdriver import 
import time

driverpath="./chromedriver.exe"
driver = webdriver.Chrome(executable_path=driverpath)

username = 'erikersay@gmail.com'
pwd = '2058007e'


url="https://www.barchart.com/login"
driver.get (url)
#driver.maximize_window()

## LOGIN
driver.find_element_by_name('email').send_keys(username)
driver.find_element_by_name('password').send_keys(pwd)
driver.find_element_by_name('password').send_keys(Keys.ENTER)
time.sleep(5)

# Navigate to Most Active Options 

most_active = 'https://www.barchart.com/options/most-active/stocks?viewName=main'
driver.get(most_active)
time.sleep(2)

most_active_download_button = driver.find_element_by_class_name('toolbar-button download')
most_active_download_button.click()

driver.quit()