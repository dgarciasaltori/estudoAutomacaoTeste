from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Chrome()
url = 'https://www.google.com'

driver.get(url)
name_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
name_field.send_keys("Fotos de Gatos")
name_field.send_keys(Keys.ENTER)
time.sleep(5)
driver.save_screenshot("teste.png")

driver.quit()