from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from deep_translator import GoogleTranslator
from selenium.webdriver.chrome.options import Options
import lib

CONDITION_STATE=["新品、未使用","未使用に近い","目立った傷や汚れなし","やや傷や汚れあり","傷や汚れあり","全体的に状態が悪い"]
rate = int(input(f"Input the rate now:\n"))
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
    chrome_options.binary_location = f"chrome-mac-arm64/chrome"

# Initialize Chrome WebDriver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service,options=chrome_options)
products_list = []
with open("fetch_info_link_input.txt",'r') as urls_file:
    urls=urls_file.readlines()
for url in urls:
    url=url.strip().replace("/en","")
    driver.implicitly_wait(30)
    price_format,price = 0,0
    english_name,product_condition,user_url = "","",""
    translator = GoogleTranslator(source='ja', target='en')
    # Navigate to the webpage
    driver.get(url)
    if "mercari" in url:
        if "product" in url:
            price_xpath='/html/body/div[1]/div[1]/div[2]/main/article/div[2]/section[1]/section[1]/div/div/span[2]'
            name_xpath='/html/body/div[1]/div[1]/div[2]/main/article/div[2]/section[1]/div[1]/div/div/h1'
            condition_xpath=['/html/body/div[1]/div[1]/div[2]/main/article/div[2]/section[3]/div[2]/div[2]/div[2]/span','/html/body/div[1]/div[1]/div[2]/main/article/div[2]/section[3]/div[2]/div[3]/div[2]/span']
            user_xpath='/html/body/div[1]/div[1]/div[2]/main/article/div[2]/section[4]/div[2]/div[2]/a'
        elif "item" in url:
            price_xpath=['/html/body/div[1]/div/div[3]/main/article/div[2]/section[1]/section[1]/div/div[1]/div/span[2]']
            name_xpath=['/html/body/div[1]/div/div[3]/main/article/div[2]/section[1]/div/div/div/h1']
            condition_xpath=['/html/body/div[1]/div/div[3]/main/article/div[2]/section[3]/div[2]/div[3]/div[2]/span','/html/body/div[1]/div[1]/div[3]/main/article/div[2]/section[3]/div[2]/div[2]/div[2]/span']
            user_xpath=['/html/body/div[1]/div/div[3]/main/article/div[2]/section[5]/div[2]/a','/html/body/div[1]/div[1]/div[3]/main/article/div[2]/section[6]/div[2]/a']
    elif "paypayfleamarket" in url:
        price_xpath='/html/body/div[1]/div/main/div[1]/div[2]/aside/div[1]/div[1]/div[3]/div/div/span'
        name_xpath='/html/body/div[1]/div/main/div[1]/div[2]/aside/div[1]/div[1]/div[1]/div[1]/h1/span'
        condition_xpath=['/html/body/div[1]/div/main/div[1]/div[2]/aside/div[2]/table/tbody/tr[3]/td/span','/html/body/div[1]/div/main/div[1]/div[2]/aside/div[2]/table/tbody/tr[2]/td/span']
        user_xpath='/html/body/div[1]/div/main/div[1]/div[2]/aside/div[4]/div[1]/div[1]/a'
    # check for price
    for item in price_xpath:
        try:
            price_element = driver.find_element(by=By.XPATH,value=item)
        except Exception as e:
            # print(f"Error in the {item} XPATH for finding price in {url}. Skipping for now...") # debuggging line
            continue
        else:
            price = int(lib.remove_non_numeric(price_element.text).strip())
            price_format = '{:8,.0f}'.format(price*rate)
            # print(f"Price is: {price}") # debuggging line
    #check for user_profile url
    for item in user_xpath:
        try:
            user_xpath = driver.find_element(by=By.XPATH,value=item)
        except Exception as e:
            # print(f"Error in the {item} XPATH for finding user in {url}. Skipping for now...") # debuggging line
            continue
        else:
            user_url=user_xpath.get_attribute("href")
            # print(f"User profile is: {user_url}") # debuggging line
    # check for name:
    for item in name_xpath:
        try:
            name_element = driver.find_element(by=By.XPATH,value=item)
        except Exception as e:
            # print(f"Error in the {item} XPATH for finding name in {url}. Skipping for now...") # debuggging line
            continue
        else:
            japanese_name = name_element.text
            english_name = lib.remove_special_characters(translator.translate(japanese_name))
    # check for condition:
    for item in condition_xpath:
        try:
            condition_element = driver.find_element(by=By.XPATH,value=item)
        except Exception as e:
            # print(f"Error in the {item} XPATH for finding condition in {url}. Skipping for now...")# debuggging line
            continue
        else:
            condition_in_ja=condition_element.text
            condition_in_en=translator.translate(condition_in_ja)
            # print(condition_in_en) # debuggging line
            if condition_in_ja in CONDITION_STATE:
                product_condition=condition_in_ja
            if product_condition == CONDITION_STATE[0] or product_condition == CONDITION_STATE[1]:
                product_condition = "NEW"
            else:
                product_condition = "2ND"
    product_info = f"{url},{english_name},NA,{product_condition},{user_url},{price}"
    products_list.append(product_info)
    print(f"{url}\t{english_name}\t{price_format}\t{product_condition}")
driver.quit()
with open ('fetch_info_link_output.txt','w') as f:
    for item in products_list:
        f.write(f"{item}\n")