# In webpages we saw some popups or alerts we need to click okay or cancel them right
# We can handle them in the selenium using alerts, mostly alerts are of java or javaScript popup's which means that we can't be able to inspect them.
# We can only accept or reject them we can do that by switching to them. Like below
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Harsha")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
assert "Harsha" in alert_text
alert.accept()  # I can accept or dismiss

# There is another alert in the page which we can reject so I am using that to demonstrate dismiss operation.
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Harsha")
driver.find_element(By.ID, "confirmbtn").click()
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
assert "Harsha" in alert_text
alert.dismiss()
