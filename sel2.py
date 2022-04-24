from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
PATH = "C:\\Users\\mypc\\Desktop\\SeleniumYoutube\\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service=s)
url = 'https://www.techwithtim.net/'
driver.get(url)
link = driver.find_element(By.LINK_TEXT, "Python Programming")
link.click()

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.LINK_TEXT, "Beginer Python Tutorials"))
)
element.click()


# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located(
#             (By.LINK_TEXT, "Beginer Python Tutorials"))
#     )
#     element.click()


# finally:
#     driver.quit()
