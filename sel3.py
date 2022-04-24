from selenium import webdriver
PATH = "C:\\Users\\mypc\\Desktop\\SeleniumYoutube\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(
    options=options, executable_path=r'PATH')
driver.get('https://www.google.com/')
