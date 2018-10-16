from selenium import webdriver
from selenium.webdriver.common.by import By
from HandyWrapper import HandyWrapper
import time

class ElementPresenceCheck(object):
    
    def Test(self):
        
        driver = webdriver.Firefox()
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver.maximize_window
        driver.implicitly_wait(10)
        hw = HandyWrapper(driver)
        driver.get(baseUrl)

        elementResult = hw.isElementPresent("name", By.ID)
        print(str(elementResult))
        
        elementResult2 = hw.elemetnPresenceCheck("//input[@id='name1']",By.XPATH)
        print(str(elementResult2))
    
        driver.quit()

ff = ElementPresenceCheck()
ff.Test()