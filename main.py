import undetected_chromedriver as uc
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

data = []
url = "https://linkedin.com/"

# Options
chrome_options = uc.ChromeOptions()
chrome_options.add_argument(r'--user-data-dir=C:\Users\moham\AppData\Local\Google\Chrome\User Data')
chrome_options.add_argument(r'--profile-directory=Profile 4')

# Drive
driver = uc.Chrome(driver_executable_path="chromedriver.exe", use_subprocess=True, options=chrome_options)
driver.maximize_window()
driver.get(url)
time.sleep(3)

# Action
actions = ActionChains(driver)


# -Search.-------------------------------------------------------
def search_():
    keyword = input("Enter Keyword to Search: ")
    s = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
    s.clear()
    s.send_keys(keyword)
    time.sleep(1)
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(3)
    driver.find_element(By.XPATH, '//button[text()="People"]').click()
    # print("Search Done!")


# -Send Connect-------------------------------------------------------
def send_():
    # Get list People
    result_list = driver.find_elements(By.CLASS_NAME, "reusable-search__entity-result-list")
    result_list = result_list[0]
    # time.sleep(1)

    # Fetch list People
    for row in result_list.find_elements(By.TAG_NAME, "li"):
        # Get name
        a_row = row.find_elements(By.TAG_NAME, "a")[1]
        name = a_row.find_elements(By.TAG_NAME, "span")[1].text
        data.append(name)

        # Send Connect
        button = row.find_element(By.TAG_NAME, "button")
        if button.text == "Connect":
            # actions.click(button).perform()
            time.sleep(1)
            #
            # actions.send_keys(Keys.TAB)
            # actions.send_keys(Keys.TAB)
            # actions.send_keys(Keys.TAB)
            # # time.sleep(1)
            #
            # actions.send_keys(Keys.ENTER).perform()
            print(name)


# -Next-------------------------------------------------------
def next_():
    # Scroll to bottom page
    html = driver.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.END)
    time.sleep(0.5)

    # Click next
    button = driver.find_element(By.CSS_SELECTOR, "button.artdeco-pagination__button.artdeco-pagination__button--next")
    actions.click(button).perform()
    time.sleep(2)


search = True
while __name__ == "__main__":
    try:
        if search:
            # recursos humanos
            search_()
            search = False

        send_()
        next_()
    except Exception as e:
        pass
