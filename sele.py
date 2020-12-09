from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import ActionChains
import csv
import time

DRIVER_PATH = '/Users/jasonbeedle/Desktop/snaviescraper/chromedriver'

options = Options()
options.page_load_strategy = 'normal'

# Navigate to url
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.canalplus.com/programme-tv/")

# ActionChains(driver).click("contentRowGuide__tvGuideTimeSlice_0").perform()

results = driver.find_element_by_class_name(
    'application___387lb')

print(results.text)
# Create csv
outfile = open("seleniumtest.csv", 'a', newline='')
writer = csv.writer(outfile)

driver.quit
