from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_hollow(self):
        self.should_be_no_items()
        self.should_be_hollow_massage()


    def should_be_hollow_massage(self):
        assert self.is_element_present(*BasketPageLocators.HOLLOW_BASKET_MASSAGE)

    def should_be_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)
    
