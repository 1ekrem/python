from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class CalenderOption(object):
    
    def test(self):
        
        driver = webdriver.Firefox()
        driver.maximize_window()