from selenium import webdriver
import os

class ChDriver(object):

    def chromedrive(self):  
        
        driverLocation = "C:/Users/DELL/Desktop/Python Scripts/Drivers/chromedriver/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)

        driver.get("https://www.google.com")
        

