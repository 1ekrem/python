from selenium import webdriver
from selenium.webdriver.common.by import By
from AutomationFramework.pages.home.login_page import LoginPage
import unittest
import pytest

class LoginTests(unittest.TestCase):
    baseUrl = "https://learn.letskodeit.com/"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    lp = LoginPage(driver)

    # @pytest.mark.run(order=2)
    # def test_validLogin(self):
    #     self.lp.login("test@email.com","abcabc")
    #     result = self.lp.verifyLoginSuccessful()
    #     assert result == True
    #     self.driver.close()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.driver.get(self.baseUrl)
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True