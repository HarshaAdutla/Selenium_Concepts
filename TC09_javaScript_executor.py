# There are some things which selenium didn't have which we can do using javaScript.
# Like we can't scroll using selenium so we will use javaScrip to do that.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")

# If any website have any restrictions like not safe, Your Connection is not Private . To eliminate those errors we use below argument in chrome
# options
chrome_options.add_argument("--ignore-certification-errors")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # This will scroll to the bottom of the page.
time.sleep(1)
driver.execute_script("window.scrollTo(0, 0);")  # This will scroll to the top of the page.
time.sleep(2)
driver.execute_script("window.scrollTo(0, 550);")
time.sleep(2)
