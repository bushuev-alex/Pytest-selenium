import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_presence_of_basket_button(browser):
    browser.get(link)
    time.sleep(3)
    assert browser.find_element_by_css_selector("#add_to_basket_form button"), 'the button is not present'
    time.sleep(3)
