from selenium import webdriver
from selenium.webdriver.common.by import By

class ByDemo(object):

    def Test(self):

        baserUrl = "https://learn.letskodeit.com/p/practice"

        driver = webdriver.Firefox()
        driver.get(baserUrl)

        elementById = driver.find_element(By.ID, "benzradio")
        
        if elementById is not None:
            print("We found and element by ID")

        elementByXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        
        if elementByXpath is not None:
            print("We found and element by Xpath")
        
        elementByLinkText = driver.find_element(By.LINK_TEXT, "Login")

        if elementByLinkText is not None:
            print("We found and element by LinkText")

        if (elementById, elementByLinkText, elementByXpath) is not None:
            driver.close()

d = ByDemo()
d.Test()