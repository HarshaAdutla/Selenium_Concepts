import time

from attr.converters import default_if_none
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# We use keyboard to enter something and when go ahead we press Enter key in out keyboard right we can handle all those with selenium also.


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
# To use the keyboard keys we need to import keys package from the selenium

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Harsha" + Keys.ENTER)  # After entering the text it will press the enter key.
time.sleep(2)
# In this page when we press ENTER key will get the success message so we will be checking the error message to verify whether the ENTER is pressed
# or not.
message = driver.find_element(By.CSS_SELECTOR, ".alert-success").text
assert "successfully" in message

# We can press almost all the keys like Control keys(windows/linux), command keys(Mac), modifier keys, functional keys, shift and alt.

# We can refer this website for other keys also.


# ********************* All Keys Notes *********************
"""
Keys Notes:- 

from selenium.webdriver.common.keys import Keys

# Modifier Keys
Keys.SHIFT
Keys.CONTROL
Keys.ALT
Keys.META  # Command key on Mac, Windows key on Windows

# Function Keys
Keys.F1
Keys.F2
Keys.F3
Keys.F4
Keys.F5
Keys.F6
Keys.F7
Keys.F8
Keys.F9
Keys.F10
Keys.F11
Keys.F12

# Navigation Keys
Keys.ARROW_DOWN
Keys.ARROW_LEFT
Keys.ARROW_RIGHT
Keys.ARROW_UP
Keys.HOME
Keys.END
Keys.PAGE_DOWN
Keys.PAGE_UP

# Action Keys
Keys.ENTER
Keys.RETURN
Keys.TAB
Keys.BACK_SPACE
Keys.BACKSPACE  # Same as BACK_SPACE
Keys.DELETE
Keys.SPACE
Keys.ESCAPE
Keys.INSERT

# Special Characters
Keys.SEMICOLON
Keys.EQUALS

# Number Pad Keys
Keys.NUMPAD0
Keys.NUMPAD1
Keys.NUMPAD2
Keys.NUMPAD3
Keys.NUMPAD4
Keys.NUMPAD5
Keys.NUMPAD6
Keys.NUMPAD7
Keys.NUMPAD8
Keys.NUMPAD9
Keys.MULTIPLY  # *
Keys.ADD       # +
Keys.SEPARATOR
Keys.SUBTRACT  # -
Keys.DECIMAL   # .
Keys.DIVIDE    # /

# Other Keys
Keys.PAUSE
Keys.CANCEL
Keys.HELP
Keys.CLEAR
Keys.COMMAND  # Mac Command key
Keys.LEFT_SHIFT
Keys.LEFT_CONTROL
Keys.LEFT_ALT
Keys.NULL


Common Usage Examples:-
from selenium.webdriver.common.keys import Keys

# Enter text and submit
search_box.send_keys("Search text" + Keys.ENTER)

# Clear field using Ctrl+A and Delete
search_box.send_keys(Keys.CONTROL + "a")
search_box.send_keys(Keys.DELETE)

# Select all (Mac)
search_box.send_keys(Keys.COMMAND + "a")

# Copy and Paste
search_box.send_keys(Keys.CONTROL + "c")  # Copy
another_box.send_keys(Keys.CONTROL + "v")  # Paste

# Navigate
element.send_keys(Keys.TAB)  # Move to next field
element.send_keys(Keys.ARROW_DOWN)  # Move down in dropdown

# Escape/Close
element.send_keys(Keys.ESCAPE)

# Multiple keys at once
element.send_keys(Keys.SHIFT + Keys.TAB)  # Shift+Tab

# Chain keys
element.send_keys(Keys.CONTROL + "a", Keys.DELETE, "New text", Keys.ENTER)


Basic Usage Of Functional Keys:
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Method 1: Using send_keys directly
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.F5)  # Refresh page

# Method 2: Using ActionChains (more reliable)
actions = ActionChains(driver)
actions.send_keys(Keys.F11).perform()  # Fullscreen

All Function Keys Examples:-

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# F1 - Usually opens Help
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.F1)

# F2 - Rename (in file systems)
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.F2)

# F3 - Search
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.F3)

# F4 - Address bar in browsers
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.F4)

# F5 - Refresh page (most common)
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.F5)

# F6 - Move cursor to address bar
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.F6)

# F7 - Spell check
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.F7)

# F8 - Usually used in Windows startup
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.F8)

# F9 - Varies by application
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.F9)

# F10 - Activate menu bar
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.F10)

# F11 - Fullscreen mode
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.F11)

# F12 - Open Developer Tools
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.F12)

Using ActionChains (Recommended Method):-
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)

# F5 - Refresh
actions.send_keys(Keys.F5).perform()

# F11 - Toggle fullscreen
actions.send_keys(Keys.F11).perform()

# F12 - Open DevTools
actions.send_keys(Keys.F12).perform()



Practical Examples
Example 1: Refresh Page Using F5


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Navigate to a page
driver.get("https://www.example.com")
time.sleep(2)

# Refresh using F5
actions = ActionChains(driver)
actions.send_keys(Keys.F5).perform()
print("Page refreshed using F5")

Example 2: Open Developer Tools with F12
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Open DevTools
actions = ActionChains(driver)
actions.send_keys(Keys.F12).perform()
time.sleep(2)

# Close DevTools
actions.send_keys(Keys.F12).perform()


Example 3: Toggle Fullscreen with F11
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Enter fullscreen
actions = ActionChains(driver)
actions.send_keys(Keys.F11).perform()
time.sleep(3)

# Exit fullscreen
actions.send_keys(Keys.F11).perform()



Function Keys with Modifiers:-
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)

# Ctrl + F5 (Hard refresh)
actions.key_down(Keys.CONTROL).send_keys(Keys.F5).key_up(Keys.CONTROL).perform()

# Shift + F10 (Context menu)
actions.key_down(Keys.SHIFT).send_keys(Keys.F10).key_up(Keys.SHIFT).perform()

# Alt + F4 (Close window)
actions.key_down(Keys.ALT).send_keys(Keys.F4).key_up(Keys.ALT).perform()


Complete Working Example:-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Setup driver
driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(2)

# Create ActionChains instance
actions = ActionChains(driver)

# Use F11 to enter fullscreen
print("Entering fullscreen...")
actions.send_keys(Keys.F11).perform()
time.sleep(3)

# Exit fullscreen
print("Exiting fullscreen...")
actions.send_keys(Keys.F11).perform()
time.sleep(2)

# Refresh page with F5
print("Refreshing page...")
actions.send_keys(Keys.F5).perform()
time.sleep(2)

# Hard refresh with Ctrl+F5
print("Hard refresh...")
actions.key_down(Keys.CONTROL).send_keys(Keys.F5).key_up(Keys.CONTROL).perform()
time.sleep(2)

driver.quit()


Important Notes:-
Send to body element: Function keys usually work best when sent to the body element or using ActionChains
Browser compatibility: Some function keys might behave differently across browsers
ActionChains is more reliable: For function keys, using ActionChains is generally more reliable than send_keys()
F12 DevTools: Opening DevTools with F12 might affect your automation script
Platform differences: Some function keys behave differently on Windows, Mac, and Linux


Common Issues and Solutions:-
# Issue: Function key not working
# Solution 1: Use ActionChains
actions = ActionChains(driver)
actions.send_keys(Keys.F5).perform()

# Solution 2: Send to body element
body = driver.find_element(By.TAG_NAME, 'body')
body.send_keys(Keys.F5)

# Solution 3: Add a small delay
time.sleep(0.5)
actions.send_keys(Keys.F5).perform()



Here's a comprehensive guide on how to use modifier keys in Selenium:
What are Modifier Keys?
Modifier keys are:

CONTROL (Ctrl) - Windows/Linux
COMMAND (Cmd/⌘) - Mac
SHIFT
ALT (Option on Mac)
META (Windows key/Command key)

Method 1: Simple Concatenation (Quick Method):-
from selenium.webdriver.common.keys import Keys

# Ctrl + A (Select all)
element.send_keys(Keys.CONTROL + "a")

# Ctrl + C (Copy)
element.send_keys(Keys.CONTROL + "c")

# Ctrl + V (Paste)
element.send_keys(Keys.CONTROL + "v")

# Ctrl + X (Cut)
element.send_keys(Keys.CONTROL + "x")

# Shift + Tab (Navigate backward)
element.send_keys(Keys.SHIFT + Keys.TAB)

# Alt + F4 (Close window - be careful!)
element.send_keys(Keys.ALT + Keys.F4)

Method 2: ActionChains with key_down/key_up (Recommended):-
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)

# Ctrl + A (Select all)
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# Ctrl + C (Copy)
actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# Ctrl + V (Paste)
actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

# Multiple modifiers: Ctrl + Shift + T (Reopen closed tab)
actions.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys("t").key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()


Common Keyboard Shortcuts
Text Editing:-

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

element = driver.find_element(By.ID, "text-field")
actions = ActionChains(driver)

# Select All
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# Copy
actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# Cut
actions.key_down(Keys.CONTROL).send_keys("x").key_up(Keys.CONTROL).perform()

# Paste
actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

# Undo
actions.key_down(Keys.CONTROL).send_keys("z").key_up(Keys.CONTROL).perform()

# Redo
actions.key_down(Keys.CONTROL).send_keys("y").key_up(Keys.CONTROL).perform()

# Bold text
actions.key_down(Keys.CONTROL).send_keys("b").key_up(Keys.CONTROL).perform()

# Italic text
actions.key_down(Keys.CONTROL).send_keys("i").key_up(Keys.CONTROL).perform()

# Find
actions.key_down(Keys.CONTROL).send_keys("f").key_up(Keys.CONTROL).perform()

Browser Navigation:-
# New Tab
actions.key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()

# Close Tab
actions.key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()

# Reopen Closed Tab
actions.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys("t").key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()

# Switch to Next Tab
actions.key_down(Keys.CONTROL).send_keys(Keys.TAB).key_up(Keys.CONTROL).perform()

# Switch to Previous Tab
actions.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()

# Refresh Page
actions.key_down(Keys.CONTROL).send_keys("r").key_up(Keys.CONTROL).perform()

# Hard Refresh
actions.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys("r").key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()

# Open DevTools
actions.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys("i").key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()

# View Page Source
actions.key_down(Keys.CONTROL).send_keys("u").key_up(Keys.CONTROL).perform()

# Zoom In
actions.key_down(Keys.CONTROL).send_keys(Keys.ADD).key_up(Keys.CONTROL).perform()

# Zoom Out
actions.key_down(Keys.CONTROL).send_keys(Keys.SUBTRACT).key_up(Keys.CONTROL).perform()

# Reset Zoom
actions.key_down(Keys.CONTROL).send_keys("0").key_up(Keys.CONTROL).perform()


Practical Examples
Example 1: Clear and Type New Text:-
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

element = driver.find_element(By.ID, "search-box")
actions = ActionChains(driver)

# Select all text
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# Delete it
element.send_keys(Keys.DELETE)

# Type new text
element.send_keys("New search query")

Example 2: Copy from One Field to Another:-
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)

# Select text from first field
source = driver.find_element(By.ID, "source-field")
source.click()
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# Copy
actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# Click on target field
target = driver.find_element(By.ID, "target-field")
target.click()

# Paste
actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()


Example 3: Multi-Select with Ctrl+Click:-
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)

# Hold Ctrl and click multiple items
item1 = driver.find_element(By.ID, "item1")
item2 = driver.find_element(By.ID, "item2")
item3 = driver.find_element(By.ID, "item3")

actions.key_down(Keys.CONTROL).click(item1).click(item2).click(item3).key_up(Keys.CONTROL).perform()

Example 4: Shift+Click to Select Range:-
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)

# Click first item
first_item = driver.find_element(By.XPATH, "//li[1]")
first_item.click()

# Hold Shift and click last item to select range
last_item = driver.find_element(By.XPATH, "//li[10]")
actions.key_down(Keys.SHIFT).click(last_item).key_up(Keys.SHIFT).perform()


Cross-Platform Compatibility (Mac vs Windows):-
import platform
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Detect platform and use appropriate modifier key
if platform.system() == 'Darwin':  # Mac
    modifier = Keys.COMMAND
else:  # Windows/Linux
    modifier = Keys.CONTROL

actions = ActionChains(driver)
element = driver.find_element(By.ID, "text-field")

# Select all (works on both platforms)
actions.key_down(modifier).send_keys("a").key_up(modifier).perform()

# Copy (works on both platforms)
actions.key_down(modifier).send_keys("c").key_up(modifier).perform()

Complete Working Example:-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Setup
driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(2)

actions = ActionChains(driver)
search_box = driver.find_element(By.NAME, "q")

# Type some text
search_box.send_keys("Selenium WebDriver")
time.sleep(1)

# Select all text using Ctrl+A
print("Selecting all text...")
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
time.sleep(1)

# Copy text using Ctrl+C
print("Copying text...")
actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
time.sleep(1)

# Delete text
search_box.send_keys(Keys.DELETE)
time.sleep(1)

# Paste text using Ctrl+V
print("Pasting text...")
actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(1)

# Press Enter
search_box.send_keys(Keys.ENTER)
time.sleep(3)

driver.quit()


Advanced: Multiple Modifiers:-
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)

# Ctrl + Shift + Delete (Clear browsing data)
actions.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys(Keys.DELETE).key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()

# Ctrl + Alt + Delete (Task Manager on Windows)
actions.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys(Keys.DELETE).key_up(Keys.ALT).key_up(Keys.CONTROL).perform()

# Ctrl + Shift + N (Incognito window)
actions.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys("n").key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()



Best Practices:-
# ✅ GOOD: Using ActionChains with proper key release
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# ✅ GOOD: Simple concatenation for basic shortcuts
element.send_keys(Keys.CONTROL + "a")

# ❌ BAD: Not releasing modifier keys
actions.key_down(Keys.CONTROL).send_keys("a").perform()  # Control stays pressed!

# ✅ GOOD: Always release modifier keys in reverse order
actions.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys("t").key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()

Common Modifier Key Combinations:-
# Text operations
Keys.CONTROL + "a"  # Select All
Keys.CONTROL + "c"  # Copy
Keys.CONTROL + "v"  # Paste
Keys.CONTROL + "x"  # Cut
Keys.CONTROL + "z"  # Undo
Keys.CONTROL + "y"  # Redo
Keys.CONTROL + "f"  # Find

# Browser operations
Keys.CONTROL + "t"  # New Tab
Keys.CONTROL + "w"  # Close Tab
Keys.CONTROL + "n"  # New Window
Keys.CONTROL + Keys.SHIFT + "t"  # Reopen Tab
Keys.CONTROL + Keys.SHIFT + "n"  # Incognito Window
Keys.CONTROL + "r"  # Refresh
Keys.CONTROL + Keys.SHIFT + "r"  # Hard Refresh
Keys.CONTROL + "+"  # Zoom In
Keys.CONTROL + "-"  # Zoom Out
Keys.CONTROL + "0"  # Reset Zoom

# Navigation
Keys.ALT + Keys.ARROW_LEFT  # Back
Keys.ALT + Keys.ARROW_RIGHT  # Forward
Keys.CONTROL + Keys.TAB  # Next Tab
Keys.CONTROL + Keys.SHIFT + Keys.TAB  # Previous Tab



"""
