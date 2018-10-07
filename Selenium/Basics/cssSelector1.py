from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class FinViz(object):

    def generateChart(self):

        driver = webdriver.Firefox()
        
        baseUrl = 'https://finviz.com/'
        driver.get(baseUrl)

        searchBarElement = driver.find_element_by_css_selector('input[placeholder = "Search ticker, company or profile"]')
        searchBarElement.send_keys("TSLA", Keys.ENTER)



charts=FinViz()
charts.generateChart()
