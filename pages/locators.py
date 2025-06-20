from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASCET_BUTTON = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs a.btn.btn-default")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    HOLLOW_BASKET_MASSAGE = (By.CSS_SELECTOR, "#content_innet p")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    
class ProductPageLocators():
    ADD_BATTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > .price_color")
    ALLERT_NAME_MASSAGE = (By.CSS_SELECTOR, "#messages > .alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) > .alertinner > strong")
    ALLERT_PRICE_MASSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in > .alertinner strong")

