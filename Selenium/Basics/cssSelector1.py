from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class FinViz(object):

    def generateChart(self):

        driver = webdriver.Firefox()
        
        baseUrl = 'https://letskodeit.teachable.com/'
        driver.get(baseUrl)

        searchBarElement = driver.find_element_by_xpath("//a[@class='btn-primary btn-hg text-center']")
        searchBarElement.click()



charts=FinViz()
charts.generateChart()
