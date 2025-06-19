from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    def add_product(self):
        self.should_be_add_button()
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BATTON)
        add_button.click()

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BATTON), "Add button is not presented"

    def should_be_allert_name_message(self):
        assert self.is_element_present(*ProductPageLocators.ALLERT_NAME_MASSAGE), "Allert name message is not presented"

    def should_be_allert_price_message(self):
        assert self.is_element_present(*ProductPageLocators.ALLERT_PRICE_MASSAGE), "Allert price message is not presented"

    def allert_name_message_correct(self):
        self.should_be_allert_name_message()
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.ALLERT_NAME_MASSAGE).text, ""

    def allert_price_message_correct(self):
        self.should_be_allert_price_message()
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(*ProductPageLocators.ALLERT_PRICE_MASSAGE).text, ""
