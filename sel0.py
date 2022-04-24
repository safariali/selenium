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
driver = webdriver.Chrome(ChromeDriverManager().install())
'''
PATH = "C:\\Users\\mypc\\Desktop\\SeleniumYoutube\\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service=s)
url = 'https://www.techwithtim.net/'
driver.get(url)
search = driver.find_element(
    By.XPATH, '//*[@id="search-2"]/form/label/input')  # found search text box //*[@id="post-3696"]
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main"]'))
    )
    articles = main.find_element(By.TAG_NAME, "article")
    # print("Type of articles::::", articles)

    for a in articles:
        header = a.find_element(By.CLASS_NAME, "entry-summary")
        # header = a.find_element_by_class_name("entry-summary")
        print(header.text)

finally:
    driver.quit()


# print("type of main.text is:     ::::::", type(main.text))
# print(main.text)
