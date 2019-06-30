from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from LoginPage import LoginPage
from WebDriverContainer import WebDriverContainer

class CrmTest(WebDriverContainer):
    _home_page_url = "https://freecrm.com/"

    def __init__(self, driver):
        super().__init__(driver)
    
    def load_home_page(self):
        self._load_url(self._home_page_url)
        return LoginPage(self._driver)