from selenium import webdriver
import os
from selenium.webdriver.common.by import By


os.environ['PATH'] += r'C:\SeleniumDrivers'
with webdriver.Chrome() as browser:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    _ = button.location_once_scrolled_into_view
    button.click()


# browser.execute_script("return arguments[0].scrollIntoView(true);", button)  ниже указано как проще