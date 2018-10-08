from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList(object):
    
    def testListofElements(self):
        
        driver = webdriver.Firefox()

        baseUrl = "https://learn.letskodeit.com/p/practice"

        wait = time.sleep(3)

        driver.get(baseUrl)

        driver.maximize_window()

        radioButtonsList = driver.find_elements(
            By.XPATH, "//input[contains(@type, 'radio')and contains(@name, 'cars')]")

        size = len(radioButtonsList)
        print("Size of the list: " + str(size))

        for radioButton in radioButtonsList:
            isSelected = radioButton.is_selected()

            if isSelected is not True:
                radioButton.click()
                print("radiobutton is clicked: ", radioButton.is_selected())
                wait
        
        driver.close()


ff = WorkingWithElementsList()
ff.testListofElements()