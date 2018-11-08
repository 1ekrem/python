from selenium import webdriver
from selenium.webdriver.common.by import By
from AutomationFramework.pages.home.login_page import LoginPage
import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseUrl = "https://learn.letskodeit.com/"
        driver = webdriver.Firefox()
        #driver.maximize_window()
        driver.implicitly_wait(15)
        driver.get(baseUrl)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")

        coursesLink = "https://learn.letskodeit.com/courses"
        driver.get(coursesLink)

        userIcon = driver.find_element_by_xpath(".//*[@id='navbar']//span[text()='Test User']")
        if userIcon is not None:
            print("--Login Successful")
        else:
            print("--Login Failed")
        
        driver.close()

# ff = LoginTests()
# ff.test_validLogin()