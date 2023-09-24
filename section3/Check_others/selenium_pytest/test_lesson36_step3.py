from selenium import webdriver
import pytest
import time
import math


@pytest.fixture(scope='session')
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
    print(f'\n\n>>>> {TestAlienMessages.final_text} <<<<\n\n')


class TestAlienMessages():
    links = [
        'https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1'
    ]
    final_text = ''

    @pytest.mark.parametrize('link', links)
    def test_messages(self, link, browser: webdriver.Chrome):
        browser.get(link)
        text_field = browser.find_element_by_css_selector(
            'textarea')
        answer = str(math.log(int(time.time())))
        text_field.send_keys(answer)
        button = browser.find_element_by_css_selector(
            '.submit-submission')
        button.click()
        feedback = browser.find_element_by_tag_name('pre').text
        try:
            assert feedback == 'Correct!', feedback
        except AssertionError:
            TestAlienMessages.final_text += feedback
            assert feedback == 'Correct!', feedback
