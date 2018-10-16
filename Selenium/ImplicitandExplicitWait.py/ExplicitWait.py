from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time

class ExplicitlyWaitDemo(object):
    
    def TestExplicit(self):
        
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        
        baseURL = "https://www.expedia.com/"
        driver.get(baseURL)

        flighTab = driver.find_element(By.XPATH, "//button[@id='tab-flight-tab-hp']")
        flighTab.click()

        departureBar = driver.find_element_by_xpath("//input[@id='flight-origin-hp-flight']")
        departureBar.send_keys("SFO")
        
        destinationBar = driver.find_element(By.ID, "flight-destination-hp-flight")
        destinationBar.send_keys("JFK")

        departureCalender = driver.find_element(By.ID, 'flight-departing-hp-flight')
        departureCalender.send_keys("10/18/2018")

        returnCalender = driver.find_element(By.ID, 'flight-returning-hp-flight')
        returnCalender.clear()
        time.sleep(3)
        returnCalender.send_keys("10/21/2018")
        
        searchButton = driver.find_element(By.XPATH, "//form[@id='gcw-flights-form-hp-flight']//button[@type='submit']")
        searchButton.click()

        wait = WebDriverWait(driver, 10, poll_frequency =1,
                            ignored_exceptions=[NoSuchElementException,
                                                ElementNotVisibleException,
                                                ElementNotSelectableException])

        _airlineCheckBox = driver.find_element_by_id("airlineRowContainer_AS")
        element = wait.until(EC.element_to_be_clickable(_airlineCheckBox))
        element.click()

        # time.sleep(2)
        # driver.quit()

ff = ExplicitlyWaitDemo()
ff.TestExplicit()
