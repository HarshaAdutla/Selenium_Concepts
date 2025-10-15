# I am commenting this entire script because it is production and also high traffic site.



"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
time.sleep(1)
driver.find_element(By.ID, "username").send_keys("harsha.adutla@gmail.com")
driver.find_element(By.ID, "password").send_keys("Secure#harsha0507")
driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Logging in to LinkedIn
time.sleep(8)
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.visibility_of_element_located((By.ID, "global-nav")))
search_box = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
search_box.send_keys("QA Engineer" + Keys.ENTER)  # Global Search
time.sleep(3)
driver.find_element(By.LINK_TEXT, "See all job results").click()  # See all job CTA
time.sleep(3)
driver.find_element(By.ID, "searchFilter_timePostedRange").click()  # Filters opened
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='Past 24 hours']").click()  # 24 hours filter selected
driver.find_element(By.XPATH, "//fieldset[@class='reusable-search-filters-trigger-dropdown__container']/div[2]/button[2]").click()  # Apply filter
time.sleep(3)
all_jobs = driver.find_elements(By.XPATH, "//*[contains(@class, 'semantic-search-results-list')]/li")

print(len(all_jobs))
# for job in all_jobs:
#     job_title= job.find_element(By.XPATH, ".//div/a/div/div/div[2]/div/div/span/strong").text
#     print(job_title)
time.sleep(5)

driver.quit()


"""