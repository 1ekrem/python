from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ImplicitlyWaitDemo(object):
    
    def test(self):
        
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)

        baseURL = "https://learn.letskodeit.com/"
        driver.get(baseURL)

        loginButton = driver.find_element(By.XPATH, "//a[@class='navbar-link fedora-navbar-link']")
        loginButton.click()

        emailField = driver.find_element(By.XPATH, "//input[@id ='user_email']")
        emailField.send_keys("test@email.com", Keys.TAB, "abcabc")

ff = ImplicitlyWaitDemo()
ff.test()

