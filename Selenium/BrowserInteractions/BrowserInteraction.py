from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class BrowserInteractions(object):
    
    def test(self):
        driver = webdriver.Firefox()

        driver.get("https://learn.letskodeit.com/p/practice")

        driver.maximize_window()

        title = driver.title 
        print("Title: ",title)

        BaseUrl = driver.current_url
        print("Current URL: ",BaseUrl)

        RadioButtonElement=driver.find_element(By.XPATH, "//input[@id='bmwradio']")
        RadioButtonElement.click()

        Page2Url = "https://www.google.com/"
        driver.get(Page2Url)

        Page2Title = driver.title
        print(Page2Title)

        Page2CurrentUrl = driver.current_url
        print(Page2CurrentUrl)

        if driver.current_url == Page2CurrentUrl:
            print("PASS - URLs mathced!", Page2CurrentUrl)
            driver.back()
            print(driver.current_url)
        
        if driver.current_url == BaseUrl:
            print("PASS - Returned back to Base URL", BaseUrl)
            driver.quit()

ff = BrowserInteractions()
ff.test()