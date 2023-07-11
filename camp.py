# open google.com
# search campusx
# learnwith.campusx.in
# dsmp course page

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


# Before: You need to download the chromedriver binary,
# unzip it somewhere on your PC and set the path to this driver like this:

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# s = Service("C:/Users/Shivam/Desktop/chromedriver.exe")
# driver = webdriver.Chrome(service=s)

# It’s boring!!! Moreover, every time a new version of the driver is released,
# you need to repeat all these steps again and again.

# With webdriver manager, you just need to do two simple steps:
# Install manager: pip install webdriver-manager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get('http://google.com')
time.sleep(3)

# fetch the search input box using xpath
user_input = driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')
user_input.send_keys('Campusx')
time.sleep(3)

user_input.send_keys(Keys.ENTER)
time.sleep(3)

link = driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[1]/div/div/div[1]/div/a')
link.click()
time.sleep(5)

link2 = driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/section[2]/a[1]')
link2.click()
time.sleep(3)

link3 = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[3]/div/a')
link3.click()
time.sleep(5)

link4 = driver.find_element(by=By.XPATH, value='//*[@id="1668499687678"]/a')
link4.click()
time.sleep(5)