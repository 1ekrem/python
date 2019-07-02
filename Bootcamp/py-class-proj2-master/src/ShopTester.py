"""
The main purpose of this module is that navigation. 
It loads URLs, loads other sections and opens items page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from HomePage import HomePage
from ShopItemPage import ShopItemPage
from ShopSearchPage import ShopSearchPage
from ShopSectionPage import ShopSectionPage
from ShopSubSectionPage import ShopSubSectionPage
from WebDriverContainer import WebDriverContainer


class ShopTester(WebDriverContainer):
    _home_page_url = "http://magento2-demo.nexcess.net"
    _search_textbox_selector = (By.NAME, "q")

    def __init__(self, driver):
        super().__init__(driver)

    def load_home_page(self):
        self._load_url(self._home_page_url)
        return HomePage(self._driver)

    def load_section_page(self, section_link):
        section_link.click()
        return ShopSectionPage(self._driver)

    def load_subsection_page(self, subsection_link):
        subsection_link.click()
        return ShopSubSectionPage(self._driver)

    def load_item_page(self, item_link):
        item_link.click()
        return ShopItemPage(self._driver)

    def search_item(self, value: str):
        search_textbox = self._try_find_element(
            self._search_textbox_selector, 20)
        search_textbox.clear()
        search_textbox.send_keys(value)
        search_textbox.send_keys(Keys.ENTER)

        return ShopSearchPage(self._driver)
    
    def find_highest_rated_item(self):
        item_rated = []
        available_item = self._try_find_elements("[class = 'item product product-item']", 20)
        for item in available_item:
            item_rating = item.__item_rating_locator
            item_rated.append(item_rating)
            highest_rated_item = max(item_rated).get_attribute("class")
            print(highest_rated_item)
        
        return highest_rated_item
