from selenium import webdriver
from selenium.types import WaitExcTypes
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/classattr")
sleep(1)

for i in range (0, 3):
    driver.find_element(By.CSS_SELECTOR, ".btn-primary.btn-test").click()
    try:
        sleep(1)
        driver.switch_to.alert.accept()
        print("Alert accepted")
    except:
        print("no Alert found")