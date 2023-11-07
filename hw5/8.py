from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://the-internet.herokuapp.com/login")
driver.implicitly_wait(0.1)
try:
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("tomsmith")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, ".fa-sign-in").click()


    text_from_page = driver.find_element(By.CSS_SELECTOR, "h4.subheader").text
    if text_from_page == "Welcome to the Secure Area. When you are done click logout below.":
        print("Авторизация прошла успешно")
    else:
        print("Неверный логин или пароль")
except:
    print("Код отработал неверно")