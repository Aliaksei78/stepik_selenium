from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
os.environ["PATH"] += r"C:\SeleniumDrivers"

with webdriver.Chrome() as browser:
    browser.get(link)
    browser.implicitly_wait(5)
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys("Smolensk")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'text1.txt')  # добавляем к этому пути имя добавляемого файла
    browser.find_element(By.CSS_SELECTOR, '#file').send_keys(file_path)  # добавляем файл

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
