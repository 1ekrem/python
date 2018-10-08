from selenium import webdriver
from selenium.webdriver.common.by import By


class BrowserInteractions(object):
    
    def Test(self):

        baseUrl = "https://learn.letskodeit.com/p/practice"

        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)

        title = driver.title
        print(title)

        currentUrl = driver.current_url
        print(currentUrl)

        driver.refresh()
        driver.get(driver.current_url)

        SecondUrl = ("https://www.google.com/")
        driver.get(SecondUrl)
        print(SecondUrl.title)

        driver.back()
        print(driver.current_url)
        
        driver.forward()
        print(driver.current_url)
        
        driver.back()
        print(driver.current_url)
        
        pageSource = driver.page_source
        print(pageSource)

        driver.quit()

ff = BrowserInteractions()
ff.Test()
