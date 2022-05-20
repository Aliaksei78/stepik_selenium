from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import os

link = "http://SunInJuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


os.environ["PATH"] += r"C:\SeleniumDrivers"

with webdriver.Chrome() as browser:
    browser.get(link)

    x = int(browser.find_element(By.ID, 'input_value').text)
    y = str(calc(x))

    input4 = browser.find_element(By.ID, 'answer')
    input4.send_keys(y)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    radio = browser.find_element(By.ID, 'robotsRule')
    _ = radio.location_once_scrolled_into_view
    radio.click()

    btn = browser.find_element(By.TAG_NAME, 'button')
    _ = btn.location_once_scrolled_into_view
    btn.click()

    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
