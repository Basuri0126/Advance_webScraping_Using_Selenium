import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)

driver.get('https://www.smartprix.com/mobiles')
time.sleep(3)

exclude_out_of_stock = driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/span')
exclude_out_of_stock.click()
time.sleep(3)

exclude_upcoming = driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/span')
exclude_upcoming.click()
time.sleep(3)


old_height = driver.execute_script('return document.body.scrollHeight')
while True:

    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(2)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height

html = driver.page_source
with open('smartprix.html', 'w', encoding='utf-8') as f:
    f.write(html)