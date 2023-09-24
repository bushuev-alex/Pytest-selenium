from selenium import webdriver
import unittest


URL = 'http://suninjuly.github.io/registration1.html'
URL2 = 'http://suninjuly.github.io/registration2.html'


class Tests(unittest.TestCase):
    def test_1(self) -> None:
        try:
            browser = _browser(URL)
            # заполняем обязательные поля
            for i in range(1, 4):
                input = browser.find_element_by_tag_name(
                    f'div:nth-child({i}) input')
                input.send_keys("lol")
            # нажимаем кнопку
            _button_clicker(browser, selector="button.btn")
            # находим элемент, содержащий текст и проверяем на совпадение
            welcome_text = browser.find_element_by_tag_name("h1").text
            self.assertEqual(
                welcome_text, "Congratulations! You have successfully registered!")
        finally:
            browser.quit()

    def test_2(self) -> None:
        try:
            browser = _browser(URL2)
            # заполняем обязательные поля
            for i in range(1, 4):
                input = browser.find_element_by_tag_name(
                    f'div:nth-child({i}) input')
                input.send_keys("lol")
            # нажимаем кнопку
            _button_clicker(browser, selector="button.btn")
            # находим элемент, содержащий текст и проверяем на совпадение
            welcome_text = browser.find_element_by_tag_name("h1").text
            self.assertEqual(
                welcome_text, "Congratulations! You have successfully registered!")
        finally:
            browser.quit()


def _browser(url: str) -> webdriver.Chrome:
    browser = webdriver.Chrome()
    browser.get(url)
    browser.implicitly_wait(1)
    return browser


def _button_clicker(browser: webdriver.Chrome, selector: str) -> None:
    button = browser.find_element_by_css_selector(selector)
    button.click()


if __name__ == '__main__':
    unittest.main()
