from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import lib
import sys

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--auto-open-devtools-for-tabs")

# Path to your Chrome WebDriver executable
if lib.check_architecture() == "ARM":
    webdriver_path = 'chromedriver-mac-arm64/chromedriver'
    chrome_options.binary_location = f"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
else:
    webdriver_path = 'chromedriver-linux64/chromedriver'
    chrome_options.binary_location = f"chrome-linux64/chrome"

service = Service(webdriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
link=sys.argv[1]
driver.get(link)
driver.implicitly_wait(10)
# Switch to the DevTools
img_links=[]
img_href_prefix="/html/body/div[1]/div[1]/div[2]/main/article/div[1]/section/div/div/div/div/div/div[2]/div[1]/div[2]/div/div["
img_href_suffix="]/div/div/div/div/figure/div[2]/picture/img"
for i in range (1,21):
    href=f"{img_href_prefix}{i}{img_href_suffix}"
    try:
        picture_link = driver.find_element(by=By.XPATH,value=href)
        img_source = picture_link.get_attribute("src").split("@")[0]
        img_links.append(img_source)
    except Exception as e:
        print(f"END THE RETRIEVING IMG IN {link}")
        break

with open("a.txt","w") as f:
    for item in img_links:
        f.write(f"{item}\n")

driver.quit()
