# LinkedIn auto Send connect
Mini boot with Python to send invetations  in linkedin

i using python 3, undetected chromedriver, Selenium

**imports**
import undetected_chromedriver as uc
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


I using my GoogleChrome profile to hide  from login section
**Options**
# Options
chrome_options = uc.ChromeOptions()
chrome_options.add_argument(r'--user-data-dir=C:\Users\moham\AppData\Local\Google\Chrome\User Data')
chrome_options.add_argument(r'--profile-directory=Profile 4')

