from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By

try:
    link = " http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.ID, value="treasure").get_attribute("valuex")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    answer = calc(input1)

    input2 = browser.find_element(By.ID, value="answer")
    input2.send_keys(answer)

    input3 = browser.find_element(By.ID, value="robotCheckbox")
    input3.click()

    input4 = browser.find_element(By.ID, value="robotsRule")
    input4.click()


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element(By.TAG_NAME, value="h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
