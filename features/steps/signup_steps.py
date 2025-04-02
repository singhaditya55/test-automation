from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from time import sleep

def before_all(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.signup_page = SignupPage(context.driver)
    context.login_page = LoginPage(context.driver)

def after_all(context):
    sleep(2)
    context.driver.quit()

@given("I am on the signup page")
def step_open_signup(context):
    context.signup_page.navigate()

@when("I enter valid details and submit the form")
def step_enter_signup_details(context):
    context.signup_page.enter_signup_details("Aditya", "Singh", "singhaditya5298@gmail.com", "Aditya@987")
    context.signup_page.submit_form()

@then("I should see a success message")
def step_verify_success_message(context):
    assert "Thank you for registering" in context.signup_page.get_success_message()

@given("I am on the login page")
def step_open_login(context):
    context.login_page.navigate()

@when("I enter valid credentials")
def step_enter_login_details(context):
    context.login_page.login("singhaditya5298@gmail.com", "Aditya@987")

@then("I should be redirected to the dashboard")
def step_verify_dashboard(context):
    assert "Welcome" in context.login_page.get_dashboard_message()
