from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from deep_translator import GoogleTranslator
from selenium.webdriver.chrome.options import Options
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


# Path to your Chrome WebDriver executable
if check_architecture() == "ARM":
    webdriver_path = 'chromedriver-mac-arm64/chromedriver'
    chrome_options.binary_location = f"chrome-mac-arm64/chrome"
else:
    webdriver_path = 'chromedriver-linux64/chromedriver'
    chrome_options.binary_location = f"chrome-linux64/chrome"


# Initialize Chrome WebDriver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service,options=chrome_options)
products_list = []
with open("input.txt",'r') as urls_file:
    urls=urls_file.readlines()
for url in urls:
    url=url.strip()
    driver.implicitly_wait(10)

    # Navigate to the webpage
    driver.get(url)
    price_xpath='/html/body/div[1]/div/div[3]/main/article/div[2]/section[1]/section[1]/div/div[1]/div/span[2]'
    price_xpath_shop='/html/body/div[1]/div[1]/div[2]/main/article/div[2]/section[1]/section[1]/div/div/span[2]'
    name_xpath='/html/body/div[1]/div/div[3]/main/article/div[2]/section[1]/div/div/div/h1'
    name_xpath_shop='/html/body/div[1]/div[1]/div[2]/main/article/div[2]/section[1]/div[1]/div/div/h1'
    condition_xpath='/html/body/div[1]/div/div[3]/main/article/div[2]/section[3]/div[2]/div[3]/div[2]/span'
    condition_xpath1='/html/body/div[1]/div[1]/div[3]/main/article/div[2]/section[3]/div[2]/div[2]/div[2]/span'
    condition_xpath_shop='/html/body/div[1]/div[1]/div[2]/main/article/div[2]/section[3]/div[2]/div[2]/div[2]/span'
    user_xpath='/html/body/div[1]/div/div[3]/main/article/div[2]/section[5]/div[2]/a'
    user_xpath_shop='/html/body/div[1]/div[1]/div[2]/main/article/div[2]/section[4]/div[2]/div[2]/a'

    # Find the element containing the price (replace 'xpath_expression' with the actual XPath of the element)
    if "shops" in url:
        price_element = driver.find_element(by=By.XPATH,value=price_xpath_shop)
        name_element = driver.find_element(by=By.XPATH,value=name_xpath_shop)
        condition_element = driver.find_element(by=By.XPATH,value=condition_xpath_shop)
        condition1_element = driver.find_element(by=By.XPATH,value=condition_xpath_shop)
        user_xpath = driver.find_element(by=By.XPATH,value=user_xpath_shop)
    else:
        price_element = driver.find_element(by=By.XPATH,value=price_xpath)
        name_element = driver.find_element(by=By.XPATH,value=name_xpath)
        condition_element = driver.find_element(by=By.XPATH,value=condition_xpath)
        condition1_element = driver.find_element(by=By.XPATH,value=condition_xpath1)
        user_xpath = driver.find_element(by=By.XPATH,value=user_xpath)
    translator = GoogleTranslator(source='ja', target='en')

    # Extract the price value
    CONDITION_STATE=["New, unused","almost unused","There is no noticeable scratches or dirt","there are some scratches and dirt.","There are scratches and dirt","Overall condition is poor"]
    price = int(price_element.text.replace(',',''))
    japanese_name = name_element.text
    english_name = translator.translate(japanese_name).replace("[", "").replace("]", "")
    condition_in_ja=condition_element.text
    condition_in_en=translator.translate(condition_in_ja)
    condition1_in_ja=condition1_element.text
    condition1_in_en=translator.translate(condition1_in_ja)
    if condition_in_en in CONDITION_STATE:
        product_condition=condition_in_en
    elif condition1_in_en in CONDITION_STATE:
        product_condition=condition1_in_en
    if product_condition == CONDITION_STATE[0] or product_condition == CONDITION_STATE[1]:
        product_condition = "NEW"
    else:
        product_condition = "2ND"
    user_xpath=user_xpath.get_attribute("href")
    product_info = f"{url},{english_name},NA,{product_condition},{user_xpath}\n"
    products_list.append(product_info)
    print(product_info)
driver.quit()

with open ('output.txt','w') as f:
    for item in products_list:
        f.write(item)