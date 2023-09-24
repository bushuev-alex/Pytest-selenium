import time
import pytest
from selenium import webdriver

def test_items(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    assert browser.find_element_by_css_selector(".btn.btn-lg.btn-primary"), "Кнопка не отображена"