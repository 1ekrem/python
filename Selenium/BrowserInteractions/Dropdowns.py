from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class DropdownElements(object):
    
    def test1(self):

        driver = webdriver.Firefox()
        driver.maximize_window()

        baseURL = "https://learn.letskodeit.com/p/practice"
        driver.get(baseURL)

        driver.implicitly_wait(10)
        wait = time.sleep(3)

        element = driver.find_element(By.ID, "carselect")

        sel = Select(element)

        #Select By Value
        sel.select_by_value("benz")
        print("Select Benz by Value")
        wait

        #Select By Index
        sel.select_by_index("2")
        print("Select Honda by Index")
        wait

        #Select BMW by visible text
        sel.select_by_visible_text("BMW")
        print("Select BMW by Visible Text")
        wait
        
        #Select Honda by Index but with Integer
        sel.select_by_index(2)
        print("Select Honda by Index with Int")
        wait

        driver.close()


ff = DropdownElements()
ff.test1()