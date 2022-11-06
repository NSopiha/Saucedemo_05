# from webdriver_manager.chrome import ChromeDriverManager
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# PATH = '/Users/nataliiasopiha/PycharmProjects/Saucedemo_06/chromedriver'
#
# driver = webdriver.Chrome(PATH)

def test_sample():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    o = webdriver.FirefoxOptions()
    o.headless = True
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()), options=o
    )
    driver.get('https://www.saucedemo.com/')

    assert driver.title == 'Swag Labs'