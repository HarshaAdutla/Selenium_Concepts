# Sometimes we see page is loading to show the content.
# There are two types of waits available in selenium to wait for some time.
# 1. Implicit Wait
# 2. Explicit Wait

# ********** Implicit Wait **********
# Implicit wait means it will wait for every element to load some mentioned time after that it will through an error.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.implicitly_wait(5)
# This wait will apply for every element for 5 seconds. This is not a good practice because there may be some case which we need to check for their
# instant operation, if we define this it will apply to those kind of tests as well. So we should use the other type of wait.


# ********** Implicit Wait **********
# This will only be applied only where we define it.

# In below, I have passed the driver and also the time. So when we use the wait it will wait the driver for 10 seconds for that particular element.

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located(By.CSS_SELECTOR, "<locator>"))

# So it will wait for the located element visibility for 10 seconds after that it will through an error.




