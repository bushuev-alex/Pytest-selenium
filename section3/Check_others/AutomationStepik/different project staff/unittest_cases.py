from selenium import webdriver
import time
import unittest


class TestReg(unittest.TestCase):
    def test_check_1st(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('form div div:nth-child(section1) input')
        input1.send_keys('Denis')
        input2 = browser.find_element_by_css_selector('form div div:nth-child(section2) input')
        input2.send_keys('Filitov')
        input3 = browser.find_element_by_css_selector('form div div:nth-child(section3) input')
        input3.send_keys('email')
        time.sleep(5)
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'error, welcome text not the same')
        browser.quit()

    def test_check_2nd(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('form div div:nth-child(section1) input')
        input1.send_keys('Denis')
        input2 = browser.find_element_by_css_selector('form div div:nth-child(section2) input')
        input2.send_keys('Filitov')
        input3 = browser.find_element_by_css_selector('form div div:nth-child(section3) input')
        input3.send_keys('email')
        time.sleep(5)
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         'error, welcome text not the same')
        browser.quit()


if __name__ == "__main__":
    unittest.main()

