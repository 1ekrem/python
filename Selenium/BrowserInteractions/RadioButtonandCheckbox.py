from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RadioButtonTest(object):
    
    def test(self):

        driver= webdriver.Firefox()
        wait = time.sleep(2)

        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver.get(baseUrl)
        
        wait

        bmwRadio = driver.find_element(By.XPATH, "//input[contains(@type, 'radio')and contains(@name, 'cars') and contains(@id, 'bmw')]")
        bmwRadio.click()

        wait

        benzRadio = driver.find_element(By.ID, "benzradio")
        benzRadio.click()

        wait

        bmwCheck = driver.find_element(By.ID, "bmwcheck")
        bmwCheck.click()

        wait

        benzCheck = driver.find_element(By.ID, "benzcheck")
        benzCheck.click()

        if (benzCheck.is_selected() and bmwCheck.is_selected() 
            and (bmwRadio.is_selected() or benzRadio.is_selected())) is True:
            print("All selected")
        else:
            print("FAILED")

        driver.quit()


ff = RadioButtonTest()
ff.test()