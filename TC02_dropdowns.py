# In web pages we will have two types of dropdowns
# 1. Static Dropdowns - These dropdowns are created using the <select> tag. And options are static in nature.
# 2. Dynamic Dropdowns - These dropdowns are created using the <div> tag. And options are dynamic in nature. These will change based on the user input.
import time
from tkinter.tix import Select

from selenium import webdriver

# ************* Browser Invocation *************

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# *************  Static Dropdowns *************
# To handle static dropdowns, we need to use the Select class in selenium.
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

static_dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
static_dropdown.select_by_value("option1")  # Select option by Value(if we have value attribute in the element)
time.sleep(2)
static_dropdown.select_by_visible_text("Option3")
time.sleep(2)
static_dropdown.select_by_index(2)  # Select option by Index
time.sleep(2)

# *************  Dynamic Dropdowns *************
driver.find_element(By.ID, "autocomplete").send_keys("ind")  # When I Enter this text options will be displayed in the dropdown.
time.sleep(2)
# Now I will capture all the options from the dropdown and store them in a list.
options = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item-wrapper")  # Here
for option in options:
    if option.text == "India":
        option.click()
        break
time.sleep(5)


# Get Attribute

# If we want to get any attribute value of any element, we can use get_attribute() method.
# Example: I have entered "ind" in the dynamic dropdown. Now I want to verify the value entered the dynamic dropdown.
# I will use get_attribute() method to get the value of the dynamic dropdown.
assert driver.find_element(By.ID, "autocomplete").get_attribute("value") == "India"


driver.close()