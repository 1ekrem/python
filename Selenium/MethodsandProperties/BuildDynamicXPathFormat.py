from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class BuildDynamicXpathFormat(object):
    
    def Test(self):

        driver = webdriver.Firefox()
        baseUrl = "https://learn.letskodeit.com"
        driver.maximize_window
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        #Login
        driver.find_element(By.LINK_TEXT, "Login").click()
        email = driver.find_element(By.ID, "user_email")
        email.send_keys("test@email.com")
        password = driver.find_element(By.ID, "user_password")
        password.send_keys("abcabc")
        driver.find_element(By.XPATH, "//input[@name = 'commit']").click()

        #Search a course
        searchBar = driver.find_element(By.XPATH, "//input[@id='search-courses']")
        #searchBar.click()
        searchBar.send_keys("Python", Keys.ENTER)

        #Select a course
        # XPath
        #_course = "//div[contains(@class, 'course-listing-title') and contains(text(), 'Selenium WebDriver With Python 3.x')]"
        # DYNAMIC XPATH
        _course = "//div[contains(@class, 'course-listing-title') and contains(text(), '{0}')]"
        _courseName = "Selenium WebDriver With Python 3.x"
        _courseLocator = _course.format(_courseName)

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()

        _courseFinalPage=driver.find_element(By.XPATH, "//h1[@class='course-title']")
        _couseFinalTitle = _courseFinalPage.text
        print(_couseFinalTitle)

        if _couseFinalTitle == _courseName:
            print("Elements found! You can successfuly sign up the course!")
        else:
            print("Course name did not match the searched course! Please try again!")

        driver.quit()


ff = BuildDynamicXpathFormat()
ff.Test()