from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
browser = webdriver.Firefox(firefox_profile='/home/alexander/.mozilla/firefox/pcrg2jsb.default-release')

browser.get("https://stepik.org/lesson/25969/step/8")
browser.quit()

