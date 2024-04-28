from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import lib
import time

## Setup chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--auto-open-devtools-for-tabs")

# Path to your Chrome WebDriver executable
if lib.check_architecture() == "ARM":
    webdriver_path = 'chromedriver-mac-arm64/chromedriver'
    chrome_options.binary_location = f"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
else:
    webdriver_path = 'chromedriver-linux64/chromedriver'
    chrome_options.binary_location = f"chrome-linux64/chrome"
# Path to your chromedriver executable

# Start Chrome with DevTools opened
# chrome_options.add_experimental_option("debuggerAddress")

# Initialize the WebDriver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the desired webpage
driver.implicitly_wait(10)
driver.get("https://jp.mercari.com/en/shops/product/4hS6JVowJ3tfhfXpkkxzyB")
driver.implicitly_wait(10)
# Switch to the DevTools
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.F12)
driver.switch_to.window(driver.window_handles[-1])
# driver.execute_script("DevToolsAPI.enterInspectElementMode()")
elements=driver.find_elements(By.CSS_SELECTOR,'[aria-label="Sources"]')
print(elements)
# time.sleep(2)
# elements = driver.find_elements_by_css_selector('.file')
# for element in elements:
#     print(element.text)

# elements = driver.find_elements(By.CSS_SELECTOR,".sources")
# print(elements)
# for element in elements:
#     print(element.text)
#     print()
# driver.quit()
