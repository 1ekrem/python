from selenium import webdriver
import os

class FindByLinkText():
    
    def test(self):
        
        driver = webdriver.Firefox(executable_path="C:/Users/DELL/Desktop/Selenium WebDriver/FireFoxDriver/geckodriver.exe")

        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver.get(baseUrl)

        elementByLinkText = driver.find_element_by_link_text("Login")

        if elementByLinkText is not None:
            print("We found an element by Link Text")
        
        elementByPartialLinkText = driver.find_element_by_partial_link_text("Sign")

        if elementByPartialLinkText is not None:
            print("We found an element by Partial Link Text")

        elementByRadioButton = driver.find_element_by_id("benzradio")
        elementByRadioButton.click()
        radiobuttonCheck = elementByRadioButton.is_selected()

        if radiobuttonCheck is True:
            print("Radio Button is clicked")
        else:
            print("Can't find!")

ff = FindByLinkText()
ff.test()