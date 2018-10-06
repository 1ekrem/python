from selenium import webdriver


def testMethod(enterYourSite):
    #Initiate the driver
    driver = webdriver.Firefox(executable_path="C:/Users/DELL/Desktop/Selenium WebDriver/FireFoxDriver/geckodriver.exe")
    driver.get(enterYourSite)

testMethod("https://stockcharts.com/")