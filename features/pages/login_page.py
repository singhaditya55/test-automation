from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_URL = "https://magento.softwaretestingboard.com/customer/account/login/"
    EMAIL = (By.ID, "singhaditya@gmail.com")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "send2")
    DASHBOARD = (By.CLASS_NAME, "greet")

    def navigate(self):
        self.driver.get(self.LOGIN_URL)

    def login(self, email, password):
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_dashboard_message(self):
        return self.get_text(self.DASHBOARD)
