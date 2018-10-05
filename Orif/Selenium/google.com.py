# google "python"
# extract all the URLs
    # Check the page structure.
    # Learn how it is organized then script

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.google.com") 

elem = driver.find_element_by_name("q") 
#Defensive programming you have to clear to make sure
elem.clear()
elem.send_keys("Python")
elem.send_keys(Keys.RETURN)

#Second page: results
driver.implicitly_wait(15)

first_div = driver.find_element_by_css_selector("div.bkWMgd:first-child")
links = first_div.find_elements_by_css_selector("a")

for link in links:
    print(link.get_attribute("href"))

# Final: job is done - close the bowser

# driver.close()


