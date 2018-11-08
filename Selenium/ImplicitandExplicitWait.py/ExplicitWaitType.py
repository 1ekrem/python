from traceback import print_stack
from Selenium.MethodsandProperties import HandyWrapper
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time

class ExplicitWaitType(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrapper()

    def waitForElement(self, locator, locatorType = 'id', 
                        timeout = 10, pollFrequency = 0.5):
        element = None
        try:
            byType= self.hw.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout)+
                            " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency =1,
                                ignored_exceptions=[NoSuchElementException,
                                                    ElementNotVisibleException,
                                                    ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                                    )))
            
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element