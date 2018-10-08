from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class HiddenElementTest(object):
    
    def Test(self):

        driver = webdriver.Firefox()
        wait = time.sleep(3)
        driver.maximize_window()
        baseURL= "https://learn.letskodeit.com/p/practice"

        driver.get(baseURL)

        TextBoxElement = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        visibleTextBox = TextBoxElement.is_displayed()

        if visibleTextBox is True:
            print("TextBox is visible!")
        else:
            print("TextBox is NOT visible!")
        
        wait

        hideButton = driver.find_element(By.XPATH, "//input[@id='hide-textbox']")
        hideButton.click()

        visibleTextBox = TextBoxElement.is_displayed()

        wait

        if visibleTextBox is True:
            print("TextBox is visible!")
        else:
            print("TextBox is NOT visible!")

        wait

        showButton = driver.find_element(By.XPATH, "//input[@id='show-textbox']")
        showButton.click()

        visibleTextBox = TextBoxElement.is_displayed()

        wait

        if visibleTextBox is True:
            print("TextBox is visible!")
        else:
            print("TextBox is NOT visible!")

        driver.close()

ff = HiddenElementTest()
ff.Test()