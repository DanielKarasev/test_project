from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        registration_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        registration_password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        registration_password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)

        registration_email.send_keys(email)
        registration_password1.send_keys(password)
        registration_password2.send_keys(password)
        registration_button.click()
        
