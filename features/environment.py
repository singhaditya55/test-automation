from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from time import sleep

def before_all(context):
    """Setup before all test cases run"""
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    
    # Initialize Page Objects
    context.signup_page = SignupPage(context.driver)
    context.login_page = LoginPage(context.driver)

def after_all(context):
    """Teardown after all test cases"""
    sleep(2)
    context.driver.quit()
