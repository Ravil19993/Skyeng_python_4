from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


browser.get("https://the-internet.herokuapp.com/inputs")
sleep(1)


try:
    browser.find_element(By.CSS_SELECTOR, "input").send_keys("1000")
    browser.find_element(By.CSS_SELECTOR, "input").clear()
    browser.find_element(By.CSS_SELECTOR, "input").send_keys("999")
    print('Success')
except:
    print("Failed")
