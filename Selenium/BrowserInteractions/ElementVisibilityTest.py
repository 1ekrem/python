from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ElementVisibilityTest(object):
    def test(self):

        driver= webdriver.Firefox()

        driver.maximize_window()
        driver.delete_all_cookies()

        driver.set_page_load_timeout(40)
        driver.implicitly_wait(10)
        
        baseUrl = "https://www.freecrm.com/register/"

        driver.get(baseUrl)

        #Displayed Test
        SubmitButton = driver.find_element(By.ID, "submitButton")
        
        SubmitButtonVisible = SubmitButton.is_displayed()

        if SubmitButtonVisible is True:
            print("PASS - Submit button is visible")
        
        #Enabled Test
        SubmitButtonEnable = SubmitButton.is_enabled()

        if SubmitButtonEnable is True:
            print("PASS - Submit button is enabled")
        else:
            print("FAIL - Submit button is disabled")
        
        #Click CheckBox
        checkBox = driver.find_element(By.NAME, "agreeTerms")
        checkBox.click()

        RecheckSubmitButtonEnabled = SubmitButton.is_enabled()

        if RecheckSubmitButtonEnabled is True:
            print("PASS - Submit button is enabled")
        else:
            print("FAIL - Submit button is disabled")

        #isDisplayed() method is applicable to checkboxes, dropdowns, radiobuttons
        checkBoxSelected = checkBox.is_selected()

        if checkBoxSelected is True:
            print("PASS - Checkbox is clicked")
        else:
            print("FAIL - Checkbox is NOT clicked")

ff = ElementVisibilityTest()
ff.test()