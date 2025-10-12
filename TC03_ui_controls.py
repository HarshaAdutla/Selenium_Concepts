import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# *************  Radio Buttons *************

radio_buttons = driver.find_elements(By.NAME, "radioButton")
print(len(radio_buttons))
for radio_button in radio_buttons:
    if radio_button.get_attribute("value") == "radio2":
        radio_button.click()
        assert radio_button.is_selected()
        break
# time.sleep(5)

# Radio buttons mostly don't change the position so we can directly use index if we want to.
# Like this:-
radio_button2 = driver.find_element(By.XPATH, "//input[@class='radioButton'][1]")
radio_button2.click()
# time.sleep(2)
assert radio_button2.is_selected()

# *************  Check Boxes *************

# In the very same website we have some checkboxes as well so we will be working on those.
# Sometimes checkbox values may change their places like option 1 will be displayed at the second place and option 2 in the first place like this.
# I have multiple checkboxes so I am taking all the items and iterating through them and selecting the required checkbox.


all_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in all_checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()  # To Select whether it is selected or not
        break
# time.sleep(4)


# # *************  is_displayed *************

# Sometimes we need to check whether something is displayed ot not. So we can use the is_displayed method

assert driver.find_element(By.ID, "displayed-text").is_displayed()  # This will return true or True.
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()  # Now this will return False.
