Feature: Sign Up and Login Functionality

  Scenario: User successfully registers an account
    Given I am on the signup page
    When I enter valid details and submit the form
    Then I should see a success message

  Scenario: User logs in with registered credentials
    Given I am on the login page
    When I enter valid credentials
    Then I should be redirected to the dashboard
