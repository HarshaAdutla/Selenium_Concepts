# We see sorting operations in the webpage right, now we will do one sorting validation.
# First I am sorting the table in the web and take it as a list I apply sort on list then it will become new sorted list now compare it with the
# original list if both are same then the sorting functionality is working fine else the sorting functionality is not working in the web.



from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")

# If any website have any restrictions like not safe, Your Connection is not Private . To eliminate those errors we use below argument in chrome
# options
chrome_options.add_argument("--ignore-certification-errors")

driver = webdriver.Chrome(options=chrome_options)
browser_sorted_veggies = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")  # This table option is available in the Greenkart website.
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()  # Now it is sorted in the web
veggie_web_elements = driver.find_elements(By.XPATH, "//tr/td[1]")

for item in veggie_web_elements:
    browser_sorted_veggies.append(item.text)
original_browser_sorted_list = browser_sorted_veggies.copy()

browser_sorted_veggies.sort()
assert browser_sorted_veggies == original_browser_sorted_list
