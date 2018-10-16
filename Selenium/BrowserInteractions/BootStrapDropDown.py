from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DropdownElements(object):
    
    def test1(self):

        driver = webdriver.Firefox()
        driver.maximize_window()

        baseURL = "https://www.jquery-az.com/boots/demo.php?ex=63.0_2"
        driver.get(baseURL)

        driver.implicitly_wait(10)
        wait = time.sleep(3)

        #Click on the dropdown button by a customized XPath
        driver.find_element(By.XPATH, "//button[contains(@class, 'multiselect')]").click()
        wait

        #Find your dropdown list by a customized XPath and store them in to a List.
        List = driver.find_elements(By.XPATH, "//ul[contains(@class, 'multiselect-container')]//li//a//label") 

        size = len(List)
        print(size)

        #Print and Select a particular name
        for list_item in List:
            print(list_item.text)

            if list_item.text.__contains__("Python"):
                list_item.click()
                break
        
        #Make sure you don't select the already selected options
        # for list_items in List:
        #     if list_items.is_selected() is False:
        #         list_items.click()

ff = DropdownElements()
ff.test1()