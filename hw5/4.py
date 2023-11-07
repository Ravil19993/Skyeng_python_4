from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


#for Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) #driver является идентификатором

driver.get("http://uitestingplayground.com/dynamicid")
sleep(1)

for i in range (0, 3):
    button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    sleep(1)
    print(i)