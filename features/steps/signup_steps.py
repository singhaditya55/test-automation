from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from time import sleep
from behave import given, when, then

def before_all(context):
    """Setup before all scenarios"""
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.signup_page = SignupPage(context.driver)
    context.login_page = LoginPage(context.driver)

def after_all(context):
    """Teardown after all scenarios"""
    sleep(2)
    context.driver.quit()

@given("I am on the signup page")
def step_open_signup(context):
    context.signup_page.navigate()

@when("I enter valid details and submit the form")
def step_enter_signup_details(context):
    """Dynamically take user details from feature file"""
    context.signup_page.enter_signup_details("Aditya", "Singh", "testuser5055@example.com", "Password@123")
    context.signup_page.submit_form()

@then("I should see a success message")
def step_verify_success_message(context):
    """Verify if signup success message appears"""
    success_message = context.signup_page.get_success_message()
    print(f"Success Message Found: {success_message}")  # Debugging
    assert "Thank you for registering" in success_message, "Signup failed!"

@given("I am on the login page")
def step_open_login(context):
    context.login_page.navigate()

@when("I enter valid credentials")
def step_enter_login_details(context):
    context.login_page.login("testuser5055@example.com", "Password@123")

@then("I should be redirected to the dashboard")
def step_verify_dashboard(context):
    dashboard_message = context.login_page.get_dashboard_message()
    print(f"Dashboard Message Found: {dashboard_message}")  # Debugging
    assert "Welcome" in dashboard_message, "Login failed!"
