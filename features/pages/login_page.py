from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_URL = "https://magento.softwaretestingboard.com/customer/account/login/"

    # Corrected element locators
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "pass")
    LOGIN_BUTTON = (By.ID, "send2")
    DASHBOARD = (By.CLASS_NAME, "greet")

    def navigate(self):
        """Navigate to the Login Page"""
        self.driver.get(self.LOGIN_URL)

    def login(self, email, password):
        """Enter login details and submit"""
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_dashboard_message(self):
        """Retrieve the dashboard welcome message"""
        return self.get_text(self.DASHBOARD)
