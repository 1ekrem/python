from selenium import webdriver
import os

class FindByLinkText():
    
    def test(self):
        
        driver = webdriver.Firefox(executable_path="C:/Users/DELL/Desktop/Selenium WebDriver/FireFoxDriver/geckodriver.exe")

        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver.get(baseUrl)

        elementbyClassName = driver.find_element_by_class_name("inputs")
        elementbyClassName.send_keys("Testing the Element")


        if elementbyClassName is not None:
            print("We found an element by Class Name")

        elementByTagName = driver.find_element_by_tag_name("h1")
        text= elementByTagName.text

        if elementByTagName is not None:
            print("We found an element by Tag Name: "+ text)

ff = FindByLinkText()
ff.test()