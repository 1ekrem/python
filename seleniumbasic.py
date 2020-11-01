from selenium import webdriver as wb
import time

url = "https://www.google.com"

wb.Chrome(executable_path="C://PythonClass/chromedriver.exe").get(url)
time.sleep(5)