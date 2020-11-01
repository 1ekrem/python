from selenium import webdriver
import time

driverpath="./chromedriver.exe"
driver = webdriver.Chrome(executable_path=driverpath)


url="https://www.youtube.com/"
driver.get (url)

time.sleep(3)
print("test is done")

driver.quit()
print("web browser is closed.")