from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GetAttributeofElement(object):
    
    def Test(self):
        
        driver = webdriver.Firefox()
        baseUrl = "https://learn.letskodeit.com/p/practice"
        wait = time.sleep(3)
        driver.get(baseUrl)

        element = driver.find_element(By.ID, "name")
        result = element.get_attribute("class")

        print("Value of attribute is: " + result)
        wait
        driver.quit()

ff = GetAttributeofElement()
ff.Test()