from selenium import webdriver
from selenium.webdriver.common.by import By
from AutomationFramework.pages.home.login_page import LoginPage
import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseUrl = "https://learn.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(15)
        driver.get(baseUrl)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")

        # coursesLink = "https://learn.letskodeit.com/courses"
        # driver.get(coursesLink)

        testresult = lp.verifyLoginSuccessful()

        assert testresult == False

        driver.close()