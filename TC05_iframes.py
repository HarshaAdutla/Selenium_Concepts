# Frames looks like they are part of the html page but no frames are a layer on top of the html.
# Ex: Consider html as a wall and frame will be the paint. We can have another html as frame.
# Same like we switched to windows and alerts we need to switch to frames also.
# How to identify a frame?
# If any element has a taf as frame or iframe then that element is a frame. It is not part of the html but a layer on it. And developers should
# inform the team if they use any frames.

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://the-internet.herokuapp.com/iframe")
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='tox-icon']").click()
time.sleep(2)
driver.switch_to.frame("mce_0_ifr")
time.sleep(2)
text_from_frame = driver.find_element(By.CSS_SELECTOR, "#tinymce").text
print(text_from_frame)
time.sleep(2)
# After execution, we need to switch back to the original page from the frame. Like Below
driver.switch_to.default_content()      # This will bring the driver to main page.
header_text = driver.find_element(By.TAG_NAME, "h3").text
print(header_text)