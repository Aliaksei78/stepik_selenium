from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import os

link = "http://suninjuly.github.io/alert_accept.html"
os.environ["PATH"] += r"C:\SeleniumDrivers"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(link)
    browser.implicitly_wait(5)

    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = int(browser.find_element(By.ID, 'input_value').text)
    y = str(calc(x))

    input4 = browser.find_element(By.ID, 'answer')
    input4.send_keys(y)

    but2 = browser.find_element(By.TAG_NAME, 'button')
    but2.click()

    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
