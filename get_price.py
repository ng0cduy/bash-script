from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from deep_translator import GoogleTranslator
from selenium.webdriver.chrome.options import Options
import platform
import sys
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

print("Operating System:", check_system())

# Path to your Chrome WebDriver executable
if check_architecture() == "ARM":
    webdriver_path = 'chromedriver-mac-arm64/chromedriver'
else:
    webdriver_path = 'chromedriver-linux64/chromedriver'
    # chrome_binary='/mnt/c/Program\ Files/Google/Chrome/Application/chrome.exe'

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = f"chrome-linux64/chrome"

# URL of the webpage you want to scrape
url = 'https://jp.mercari.com/en/item/m51252320310'

# Initialize Chrome WebDriver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service,options=chrome_options)
driver.implicitly_wait(10)
# Navigate to the webpage
driver.get(url)
price_xpath='/html/body/div[1]/div/div[3]/main/article/div[2]/section[1]/section[1]/div/div[1]/div/span[2]'
name_xpath='/html/body/div[1]/div/div[3]/main/article/div[2]/section[1]/div/div/div/h1'
condition_xpath='/html/body/div[1]/div/div[3]/main/article/div[2]/section[3]/div[2]/div[3]/div[2]/span'
like_xpath='/html/body/div[1]/div/div[3]/main/article/div[2]/section[1]/section[2]/div/div[1]/div[1]/div/div[1]/button/span'
user_xpath='/html/body/div[1]/div/div[3]/main/article/div[2]/section[5]/div[2]/a'
# Find the element containing the price (replace 'xpath_expression' with the actual XPath of the element)
price_element = driver.find_element(by=By.XPATH,value=price_xpath)
name_element = driver.find_element(by=By.XPATH,value=name_xpath)
condition_element = driver.find_element(by=By.XPATH,value=condition_xpath)
like_element = driver.find_element(by=By.XPATH,value=like_xpath)
user_xpath = driver.find_element(by=By.XPATH,value=user_xpath)
translator = GoogleTranslator(source='ja', target='en')

# Extract the price value
price = int(price_element.text.replace(',',''))
japanese_name = name_element.text
english_name = translator.translate(japanese_name)
condition_in_ja=condition_element.text
condition_in_en=translator.translate(condition_in_ja)
like=like_element.text
user_xpath=user_xpath.get_attribute("href")
print(f"{url},{english_name},{price},{like},{user_xpath}")


# Close the WebDriver
driver.quit()
