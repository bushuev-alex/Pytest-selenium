from typing import Union
from selenium import webdriver
import time


def test_add_to_cart_button(browser: Union[webdriver.Chrome, webdriver.Firefox]):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    browser.implicitly_wait(5)
    button = browser.find_element_by_css_selector('.btn-add-to-basket').is_enabled()
    time.sleep(10)
    assert button, 'alert is not "Deferred benefit offer"'
