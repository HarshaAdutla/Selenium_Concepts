# In webpages when we click on some links or something it opens in another window right.
# But in selenium when we open any browser the driver works in that window only, if we want to automate in the newly opened window we need to
# switch to the new window.
# We can do this by using switch functionality.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()
# Now the new window will be opened but our driver will stay in the old window we call it the parent window.
# To switch the driver from parent window to child window we use window handles method.

windows_opened = driver.window_handles  # This will collect all the windows opened in the list.
driver.switch_to.window(windows_opened[1])  # We need to pass the window name here.
print(driver.find_element(By.TAG_NAME, "h3").text)
time.sleep(2)

# After performing operations in the child window when we use driver.close() this will close the child window but not the parent window.
# We need to get that driver back to the parent window to continue the test, we can do that like below

driver.switch_to.window(windows_opened[0])
time.sleep(3)
print(driver.find_element(By.TAG_NAME, "h3").text)

# We can put the assertions also like below.
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text


