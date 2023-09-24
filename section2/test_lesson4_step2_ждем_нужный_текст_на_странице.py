import time, math

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    price100 = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    button1 = browser.find_element(By.ID, value="book")
    button1.click()

    X1 = browser.find_element(By.ID, value="input_value").text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(int(X1))

    input1 = browser.find_element(By.ID, value="answer")
    input1.send_keys(y)

    button2 = browser.find_element(By.ID, value="solve")
    button2.click()

    # message = browser.find_element_by_id("verify_message")
    # assert "successful" in message.text
    time.sleep(5)

finally:
    browser.quit()
