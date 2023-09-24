from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    URL_TO_LOGIN_PAGE = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    URL_TO_MAIN_PAGE = "http://selenium1py.pythonanywhere.com/"


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    # URL_TO_PROD_PAGE =
    # "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    URL_TO_PROD_PAGE = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    BASKET_SELECTOR = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    PROD_NAME_SELECTOR = (By.CLASS_NAME, "col-sm-6.product_main h1")
    PROD_PRICE_SELECTOR = (By.CLASS_NAME, "col-sm-6.product_main p.price_color")
    PROD_NAME_SELECTOR_CONFIRM = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-success.fade.in strong")
    PROD_PRICE_SELECTOR_CONFIRMED = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-info.fade.in strong")
    LINKS_TO_PARAMS = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]
