from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

link = "http://suninjuly.github.io/selects1.html"

os.environ["PATH"] += r"C:\SeleniumDrivers"
with webdriver.Chrome() as browser:
    browser.get(link)

    x = int(browser.find_element(By.ID, 'num1').text)
    y = int(browser.find_element(By.ID, 'num2').text)

    z = str(x + y)

    my_select = Select(browser.find_element(By.TAG_NAME, 'select'))
    my_select.select_by_value(z)

    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()

    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
