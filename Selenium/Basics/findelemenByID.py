from selenium import webdriver
import os

class FindByIdName():
    
    def test(self):
        
        driverLocation = "C:/Users/DELL/Desktop/Python Scripts/Drivers/chromedriver/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)

        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver.get(baseUrl)

        elementById=driver.find_elements_by_id("bmwradio")
        
        if elementById is not None: # None is null in Python
            print("We found the element by id")

        elementByName = driver.find_element_by_name("show-hide")

        if elementByName is not None:
            print("We found the element by name")


ff = FindByIdName()
ff.test()