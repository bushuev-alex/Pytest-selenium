from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_cond
from math import log, sin


URL = 'http://suninjuly.github.io/explicit_wait2.html'


def create_browser(url: str) -> webdriver.Chrome:
    browser = webdriver.Chrome()
    browser.get(url)
    browser.implicitly_wait(5)
    return browser


def get_result(browser: webdriver.Chrome) -> None:
    alert = browser.switch_to.alert
    alert_text = alert.text.split(':')[-1]
    print(alert_text)
    browser.quit()


def test(browser: webdriver.Chrome) -> None:
    start_button = browser.find_element_by_id('book')
    start_button.click()
    # math
    x = int(browser.find_element_by_id('input_value').text)
    result = str(log(abs(12*sin(x))))

    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(result)

    end_button = browser.find_element_by_id('solve')
    end_button.click()


def main(url: str) -> None:
    try:
        browser = create_browser(url)
        WebDriverWait(browser, 15).until(
            exp_cond.text_to_be_present_in_element((By.ID, 'price'), '100'))
        test(browser)
    except Exception as ex:
        print(ex, '\n')
    finally:
        get_result(browser)


if __name__ == '__main__':
    main(URL)
