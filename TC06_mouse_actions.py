import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
time.sleep(3)
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
time.sleep(3)
# When we use actions we need to give .perform() at the end then only it works. Consider it as action needs to performed to complete the action.
# Her I went to mouse hover tab and clicked on reload button using the actions class.

# Similarly if we want to click right click(context click) we can do that by using same actions. Like below
action.context_click(driver.find_element(By.ID, "mousehover")).click().perform()
time.sleep(2)
