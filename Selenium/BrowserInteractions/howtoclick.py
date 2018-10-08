from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class HowToClick(object):
    
    def Test(self):

        driver = webdriver.Firefox()
        baseUrl = "https://learn.letskodeit.com/"

        driver.get(baseUrl)
        driver.implicitly_wait(10)

        login_link = driver.find_element(By.XPATH, "//a[@class='navbar-link fedora-navbar-link']")
        login_link.click()

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test@gmail.com")

        passwordField = driver.find_element(By.ID, "user_password")
        passwordField.send_keys("123456789")

        time.sleep(3)

        #Clear
        emailField.clear()

        time.sleep(3)

        emailField.send_keys("TestingAgain@gmail.com")

        driver.quit()



ff = HowToClick()
ff.Test()
