from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import platform
import sys
import subprocess

def split_cmd(cmd):
    return cmd.split(" ")

def check_architecture():
    arch = platform.machine()
    if 'arm' in arch.lower():
        return "ARM"
    elif 'amd' in arch.lower() or "x86_64" in arch.lower():
        return "AMD"
    else:
        return "Unknown"

def check_system():
    system = platform.system()
    if system == 'Windows':
        return "Windows"
    elif system == 'Linux':
        return "Linux"
    else:
        return "Unknown"

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--auto-open-devtools-for-tabs")

# Path to your Chrome WebDriver executable
if check_architecture() == "ARM":
    webdriver_path = 'chromedriver-mac-arm64/chromedriver'
    chrome_options.binary_location = f"chrome-mac-arm64/chrome"
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
# Switch to the Sources tab
elements_tab = driver.find_element(By.CSS_SELECTOR, '[aria-label="Elements"]')
elements_tab.click()
driver.quit()
