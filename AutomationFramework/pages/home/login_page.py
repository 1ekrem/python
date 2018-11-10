from selenium import webdriver
from selenium.webdriver.common.by import By
from AutomationFramework.base.selenium_driver import SeleniumDriver
from AutomationFramework.utilities.custom_logger import customLogger
import logging

class LoginPage(SeleniumDriver):
    
    log = customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _login_link = "Login"
    _emai_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")
    
    def enterEmail(self, email):
        self.sendKeys(email, self._emai_field)
    
    def enterPassword(self, password):
        self.sendKeys(password,self._password_field)
    
    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//span[@class='navbar-current-user' and contains(text(),'Test User')]", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(), 'Invalid email or password.')]", locatorType="xpath")
        return result

