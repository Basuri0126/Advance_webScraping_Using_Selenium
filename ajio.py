from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)

driver.get('https://www.ajio.com/men-backpacks/c/830201001')
time.sleep(3)

old_height = driver.execute_script('return document.body.scrollHeight')

counter = 1
while True:

    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(counter)
    counter += 1
    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height

html = driver.page_source

with open('ajio.html', 'w', encoding='utf-8') as f:
    f.write(html)