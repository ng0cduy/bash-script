from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set up Chrome DevTools Protocol
chrome_driver_path = 'chromedriver-mac-arm64/chromedriver'
chrome_service = Service(chrome_driver_path)
chrome_service.start()
prefs = {
    "download.default_directory": "/path/to/download/directory",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
# Connect to Chrome DevTools
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Run headless if needed
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_experimental_option("prefs", prefs)# Specify the port Chrome DevTools Protocol is listening on
chrome_driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to a webpage
chrome_driver.get("https://jp.mercari.com/en/shops/product/4hS6JVowJ3tfhfXpkkxzyB")

# Get the current page URL
current_url = chrome_driver.get_downloadable_files()
print("Current URL:", current_url)

# After you're done, don't forget to quit the driver
chrome_driver.quit()
chrome_service.stop()
