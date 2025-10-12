# In selenium, we have different types of locators to find elements on a web page.
# The most commonly used locators are:
# 1. ID
# 2. Name
# 3. Class Name
# 4. Tag Name
# 5. Link Text
# 6. Partial Link Text
# 7. CSS Selector
# 8. XPath


# We can invoke any browser using webdriver class.

# Here in this script I am using all the locators to demonstrate how to use them.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
time.sleep(3)
# Using ID locator for sending the username
driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")

# Using CSS_Selector locator for sending the password
driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("learning")

# Using XPATH locator for clicking the sign-in button
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()

# And we have two radio buttons for user type. We will use XPATH locator for this with index.
driver.find_element(By.XPATH, "//label[@class='customradio'][1]").click()

# Handling the same radio button with CSS_Selector and index.
# driver.find_element(By.CSS_SELECTOR, "label.customradio:nth-child(1)").click          -> Handling the same radio button with another locator.
driver.find_element(By.LINK_TEXT, "terms and conditions").click()  # Using Link Text locator for clicking the terms and conditions link.
time.sleep(5)

#  These are the most commonly used locators in selenium.


# We can gte title, and we can refresh the page using selenium.
print(driver.title)  # This will print the title of the page
driver.refresh()  # This will refresh the page
time.sleep(3)
driver.close()  # This will close the browser
"""
We can write locators on simple text also.
For example, if we have a button with text "Sign In", we can use the following locators to find the button.
1. XPATH: //button[text()='Sign In']
2. CSS Selector: button:contains('Sign In')   --> Note: This is not supported in all browsers.
3. XPATH: //button[contains(text(),'Sign In')]
"""

# In above, I have used the webdriver class to invoke the browser.
# We can also use the service class to invoke the browser.
# -->   Like this
"""
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Drivers/chromedriver.exe")
"""
# Inside the Service() we have to provide the path of the chromedriver.exe file.
# We need to download the chromedriver.exe file from the official website of selenium. And we need to check the version of the chrome browser and
# download the chromedriver.exe file accordingly.

# We can also use the webdriver manager to invoke the browser.
# -->   Like this
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)
"""

# Same way we can use the webdriver manager for other browsers also like firefox, edge etc.
#  -->   Like this
"""
*********** For Firefox ***********

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

Way 1: 
driver = webdriver.Firefox()    # For Firefox

Way 2:
from selenium.webdriver.chrome.service import Service

service_obj = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service_obj)

Way 3:
from selenium.webdriver.chrome.service import Service

Service_obj = Service("C:/Drivers/geckodriver")
driver = webdriver.Firefox(service=service_obj)

*********** For Edge ***********

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

Way 1:
driver = webdriver.Edge()

Way 2:
from selenium.webdriver.edge.service import Service

service_obj = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service_obj)

Way 3:
from selenium.webdriver.edge.service import Service

Service_obj = Service("C:/Drivers/msedgedriver")
driver = webdriver.Edge(service=service_obj)

*********** For Safari ***********

Way 1:
driver = webdriver.Safari()

Way 2:
from selenium.webdriver.safari.service import Service

service_obj = Service(SafariDriverManager().install())
driver = webdriver.Safari(service=service_obj)

Way 3:
from selenium.webdriver.safari.service import Service

Service_obj = Service("/usr/bin/safaridriver")
driver = webdriver.Safari(service=service_obj)
"""
