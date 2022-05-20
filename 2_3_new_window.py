from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import os

link = "http://suninjuly.github.io/redirect_accept.html"
os.environ["PATH"] += r"C:\SeleniumDrivers"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(link)
    browser.implicitly_wait(5)

    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()  # на сайте заложено открытие нового окна

    # метод window_handles, который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто
    # две вкладки, выбираем вторую вкладку:
    # current_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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
