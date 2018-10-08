from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ElementState(object):

    def isEnabled(self):
        baseUrl = "https://www.google.com/"

        driver = webdriver.Firefox()

        driver.get(baseUrl)
        driver.implicitly_wait(3)

        e1 = driver.find_element_by_xpath("//input[@title='Search']")
        e1.send_keys("Hello World", Keys.ENTER)

ff = ElementState()
ff.isEnabled()