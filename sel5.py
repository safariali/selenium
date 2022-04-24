from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
''' 
https://www.youtube.com/watch?v=9_5Wqgni_Xw
Python Selenium Tutorial #5 - UnitTest Framework (Part 1)
'''
PATH = "C:\\Users\\mypc\\Desktop\\SeleniumYoutube\\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service=s)
url = 'https://orteil.dashnet.org/cookieclicker/'
driver.get(url)
# wait 5 seconds before finding elements in line below
driver.implicitly_wait(5)
cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, "productPrice" + str(i))
         for i in range(1, -1, -1)]

actions = ActionChains(driver)
actions.click(cookie)
for i in range(500):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    print(count)
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
