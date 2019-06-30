from selenium import webdriver

from CrmTester import CrmTest
from  utils import stringify_links, filter_by_text

# create a WebDriver instance
driver = webdriver.Chrome()
crm = CrmTest(driver)

# 1) load home page and retrieve section links
home_page = crm.load_home_page()
home_page.screenshot("C:/PythonClass/freecrm/screenshots/homepage.png")

