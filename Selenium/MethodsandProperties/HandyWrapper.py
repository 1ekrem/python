from selenium.webdriver.common.by import By

class HandyWrapper(object):

    def __init__(self, driver):
        self.driver = driver

    def  getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath" :
            return By.XPATH
        else:
            print("Locator type is not supported")
        return False
    
    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element Found")
        except:
            print("Element not found")
        return element

    def isElementPresent(self, locator, byType):
        element = None
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                print("Element Found")
                return True
            else: return False
        except:
            print("Element not found")
            return False

    def elemetnPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                print("Element Found")
                return True
            else:
                print("Element Not Found, Yapacagin isi sikiyim!")
                return False
        except:
            print("Element not found")
            return False