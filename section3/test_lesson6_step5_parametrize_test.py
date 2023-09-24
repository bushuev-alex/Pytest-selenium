import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest

links = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1'
         ]


@pytest.mark.parametrize('link', links)
def test_3_6_1(browser, link):
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    # input1 = browser.find_element_by_tag_name("textarea")
    input1 = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
    input1.send_keys(str(math.log(int(time.time()))))

    button1 = browser.find_element_by_class_name("submit-submission")
    button1.click()

    TestResult = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.TAG_NAME, "pre"))).text
    # text1 = browser.find_element_by_tag_name("pre").text
    assert TestResult == "Correct!", "Should be 'Correct!'"
