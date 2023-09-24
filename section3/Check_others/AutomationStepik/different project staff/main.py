import pytest
import time
import math
from selenium import webdriver

answer = math.log(int(time.time()))

@pytest.fixture(scope='function')
def browser():
    print('/nI start the browser')
    browser = webdriver.Chrome()
    yield  browser
    print('/nI close the browser, thank you for testing')
    browser.quit()


class TestAlienStuff:

    @pytest.mark.parametrize('custom_link', ['95', '96', '97', '98', '99', '03', '04', '05'])
    def test_check_alien_tasks(self, browser, custom_link):
        link = f'https://stepik.org/lesson/2368{custom_link}/step/1'
        browser.get(link)
        inp = browser.find_element_by_css_selector('#velvet86')
        inp.send_keys(answer)
    