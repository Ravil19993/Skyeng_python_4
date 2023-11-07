from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By #Добавляем класс By из селениума


#for Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

for i in range (0, 5):
    button = driver.find_element(By.CSS_SELECTOR, "button").click()


length = len(driver.find_elements(By.CSS_SELECTOR, "button.added-manually"))
print('Количество кнопок удаления = ', length)
