from selenium import webdriver
import os

class FindByIdName():
    
    def test(self):
        
        driver = webdriver.Firefox(executable_path="C:/Users/DELL/Desktop/Selenium WebDriver/FireFoxDriver/geckodriver.exe")

        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver.get(baseUrl)

        elementByXpath = driver.find_elements_by_xpath("//input[@id='name']")

        if elementByXpath is not None:
            print("We found an element by Xpath")
        
        elementByCSS = driver.find_elements_by_css_selector("#displayed-text")

        if elementByCSS is not None:
            print("We found an element by CSS")


ff = FindByIdName()
ff.test()