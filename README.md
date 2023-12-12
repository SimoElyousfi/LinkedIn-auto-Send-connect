# LinkedIn auto Send connect
Boot with Python to send invetations  in linkedin
This boots have 3 Functions (Search, Send, Next page) 

# I using
Python 3, undetected chromedriver, Selenium

# imports
import undetected_chromedriver as uc

from selenium.webdriver import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

import time


# Chrome Options
I using my GoogleChrome profile to hide  from login section

chrome_options = uc.ChromeOptions()

chrome_options.add_argument(r'--user-data-dir=C:\Users\moham\AppData\Local\Google\Chrome\User Data')

chrome_options.add_argument(r'--profile-directory=Profile 4')

# Create driver

driver = uc.Chrome(driver_executable_path="chromedriver.exe", use_subprocess=True, options=chrome_options)

driver.maximize_window()

driver.get(url)

time.sleep(3)

# Action

actions = ActionChains(driver)

