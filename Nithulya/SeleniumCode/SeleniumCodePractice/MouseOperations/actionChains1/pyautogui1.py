import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
import pyautogui

driver = webdriver.Chrome()
def context_click_operation():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    homeElement = driver.find_element(By.XPATH, "//div[@class='menu-custom-main-menu-container']//a[text()='Home']")
    action = ActionChains(driver)
    action.context_click(homeElement).perform()
    time.sleep(2)
    for i in range(6):
        pyautogui.press('down')
        time.sleep(1)

    pyautogui.press('enter')
    time.sleep(4)

context_click_operation()
driver.close()