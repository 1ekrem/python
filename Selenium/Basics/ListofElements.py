from selenium import webdriver
from selenium.webdriver.common.by import By

class ListOfElements(object):
    def testElements(self):
        
        driver = webdriver.Firefox()
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver.get(baseUrl)

        elementListByClass = driver.find_elements_by_class_name("inputs")
        length1 = len(elementListByClass)

        if elementListByClass is not None:
            print("Class Name -> Size of the elements: "+ str(length1))

        elementListByTagName = driver.find_elements(By.TAG_NAME, "a")
        length2 = len(elementListByTagName)

        if elementListByTagName is not None:
            print("Tag Name -> Size of the elements: "+str(length2))

        if (elementListByClass, elementListByTagName) is not None:
            driver.close()

runTest= ListOfElements()
runTest.testElements()



