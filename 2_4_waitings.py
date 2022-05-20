from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
import os

link = "http://suninjuly.github.io/explicit_wait2.html"
os.environ["PATH"] += r"C:\SeleniumDrivers"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(link)
    browser.implicitly_wait(5)

    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    btn = browser.find_element(By.ID, 'book')
    btn.click()

    x = browser.find_element(By.ID, 'input_value')
    x = x.text

    y = str(calc(x))

    input4 = browser.find_element(By.ID, 'answer')
    input4.send_keys(y)

    but2 = browser.find_element(By.ID, 'solve')
    but2.click()

    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
