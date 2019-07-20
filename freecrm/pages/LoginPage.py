from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from WebDriverContainer import WebDriverContainer

class LoginPageModel(WebDriverContainer):
    __login_Button_selector = (By.XPATH, "//span[text()='Log In']")

    #Initiate the driver
    def __init__(self, driver):
        super().__init__(driver)
    
    @property
    def button_link(self):
        loginButton = self._try_find_element(self.__login_Button_selector, 20)

        return loginButton
    
class LoginPage(WebDriverContainer):
    def __init__(self, driver):
        super().__init__(driver)
        self.__login__ = LoginPageModel(driver)
    
    @property
    def button_link(self):
        return self.__login__.button_link
    