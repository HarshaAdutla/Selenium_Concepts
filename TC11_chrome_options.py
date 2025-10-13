# In above test cases somewhere I have already used chrome options.
# What is chrome Options?
# In first few scripts we something to maximize the browser window, we can do that by using chrome options.
# We used driver.maximize_window() - method this is a valid and this is the selenium method to maximize the browser window.
# this will be used after browser initialization meanas, we first initiate the browser then this will work, like browser will be opened and then it
# will get maximized. But using chrome options we can directly start the browser in the maximized window itself.
import time

from selenium import webdriver

# Normal Selenium flow
# driver = webdriver.Chrome()
# driver.maximize_window()

# Like this we can only define it after browser initiated.

# We need to import the chrome options first then we can define these methods even before initiating the browser.

# Chrome Options:

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# Now we need to pass this chrome options to the driver. Like below

# Like this we can define more operations.
# Headless:-
# When we run any test browser will be opened and test will be executed right, we do that in headless mode also. Means browser will be opened and
# executes the test but in the background. We can only see the output not the browser. This will put less pressure on the system CPU.
chrome_options.add_argument("--headless")  # I am commenting/uncommenting to see other chrome options.

# SSL Certifications:-
# Some webpages have ssl certificates, means we used to saw when we open any websites we get private network errors like this right, so we need to
# ignore all those certifications we can use the chrome options.
chrome_options.add_argument("--ignore-certification-errors")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
time.sleep(3)

# There are a lot of methods were there but these are the most used ones. In the below-mentioned URL all the chrome_options were there.
# https://www.selenium.dev/documentation/webdriver/browsers/chrome/
