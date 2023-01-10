import time
from selenium import webdriver
import pywinmacro as p

driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://google.com")


time.sleep(5)
driver.close()