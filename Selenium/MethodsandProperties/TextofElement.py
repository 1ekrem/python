from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TextElement(object):
    
    def Test(self):

        driver = webdriver.Firefox()
        
        driver.maximize_window()
        
        baseUrl = "https://learn.letskodeit.com/p/practice"
        
        driver.get(baseUrl)

        openTabElement = driver.find_element(By.ID, "opentab")
        elementText = openTabElement.text
        print("Text on element is: "+ elementText)
        time.sleep(2)
        driver.quit()

ff = TextElement()
ff.Test()


