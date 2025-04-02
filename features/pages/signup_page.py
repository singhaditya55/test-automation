from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignupPage(BasePage):
    SIGNUP_URL = "https://magento.softwaretestingboard.com/customer/account/create/"
    FIRST_NAME = (By.ID, "Aditya")
    LAST_NAME = (By.ID, "Singh")
    EMAIL = (By.ID, "singhaditya@gmail.com")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "password")
    SIGNUP_BUTTON = (By.XPATH, "//button[@title='Create an Account']")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "message-success")

    def navigate(self):
        self.driver.get(self.SIGNUP_URL)

    def enter_signup_details(self, first_name, last_name, email, password):
        self.enter_text(self.FIRST_NAME, first_name)
        self.enter_text(self.LAST_NAME, last_name)
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.enter_text(self.CONFIRM_PASSWORD, password)

    def submit_form(self):
        self.click(self.SIGNUP_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
