# https://www.youtube.com/watch?v=Xjv1sY630Uc&t=5s
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# https://chromedriver.chromium.org/downloads
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
PATH = "C:\\Users\\mypc\\Desktop\\SeleniumYoutube\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

url = "https://orteil.dashnet.org/cookieclicker/"
driver.get(url)
driver.implicitly_wait(5)
cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i))
         for i in range(1, -1, -1)]
actions = ActionChains(driver)
actions.click(cookie)

# for i in range(1000):
