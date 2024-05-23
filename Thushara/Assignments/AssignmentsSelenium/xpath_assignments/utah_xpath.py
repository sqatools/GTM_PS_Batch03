import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.visitutah.com/places-to-go/")
things_to_do = driver.find_element(By.XPATH,"//a[@href ='/things-to-do']")
things_to_do.click()
dinosaurs = driver.find_element(By.XPATH,"//a[@href='/things-to-do/History-Culture/Dinosaurs-Paleontology']")
dinosaurs.click()
time.sleep(10)
driver.close()