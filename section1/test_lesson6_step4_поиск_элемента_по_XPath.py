from selenium import webdriver
import time

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, value="input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, value="last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, value="form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, value="country")
    input4.send_keys("Russia")
    button2 = browser.find_element(By.XPATH, value="//button[text()='Submit']")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
