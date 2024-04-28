from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from deep_translator import GoogleTranslator
from selenium.webdriver.chrome.options import Options
import json
import lib

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")


# Path to your Chrome WebDriver executable
if lib.check_architecture() == "ARM":
    webdriver_path = 'chromedriver-mac-arm64/chromedriver'
    chrome_options.binary_location = f"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
else:
    webdriver_path = 'chromedriver-linux64/chromedriver'
    chrome_options.binary_location = f"chrome-linux64/chrome"

service = Service(webdriver_path)
driver = webdriver.Chrome(service=service,options=chrome_options)
products_list = []
with open("fetch_info_link_input.txt",'r') as urls_file:
    urls=urls_file.readlines()
for url in urls:
    url=url.strip()
    driver.implicitly_wait(10)
    driver.get(url)
    sold_or_not_state=""
    if "mercari" in url:
        if "item" in url:
            sold_or_not='/html/head/script[1]'
            sold_or_not_state=driver.find_element(By.CSS_SELECTOR,'script[type="application/ld+json"]')
            script_inner_html = sold_or_not_state.get_attribute("innerHTML")
            sold_or_not_state_dict = json.loads(script_inner_html)
            current_status = sold_or_not_state_dict['offers']['availability']
            script_inner_html = sold_or_not_state.get_attribute("innerHTML")
            sold_or_not_state_dict = json.loads(script_inner_html)
            current_status = sold_or_not_state_dict['offers']['availability']
        elif "product" in url:
            sold_or_not='/html/body/div[1]/div[1]/div[2]/main/article/div[1]/section/div/div/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div' # mer shop
            try:
                sold_or_not_state=driver.find_element(By.CSS_SELECTOR,'[aria-label="Sold"]') # mer shop
                current_status = sold_or_not_state.get_attribute("aria-label") # mershop
            except Exception as e:
                current_status = "AVAILABLE"
    elif "paypayfleamarket" in url:
        pass
    url_formatted = "{:<45}".format(url)
    if 'soldout' in current_status.lower() or 'sold' in current_status.lower():
        status = "{:<10}".format("SOLD")
    else:
        status = "{:<10}".format("AVAILABLE")
    available_state=f"{url_formatted}\t{status}"
    products_list.append(available_state)
    print(available_state)
driver.quit()

with open ('fetch_info_status_output.txt','w') as f:
    for item in products_list:
        f.write(f"{item}\n")