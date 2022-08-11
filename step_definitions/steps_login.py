from pytest_bdd import given, when, then, parsers
from POM.pages.login import Login
from POM.pages.dashboard import Dashboard
from data import credentials


@given("I am on the login page")
def navigate_to_login_page(browser):
    """Navigate to login page"""
    browser.driver.get(browser.base_url)
    Login(browser.driver).verify_login_page_is_displayed()


@when(parsers.parse("I log in with username {username} and password {password}"))
def login(browser, username, password):
    """Login with username and password"""
    Login(browser.driver).input_username(username)
    Login(browser.driver).input_password(password)
    Login(browser.driver).click_login()


@then("I should be logged in")
def verify_login_successfully(browser):
    """Verify login successfully"""
    Dashboard(browser.driver).verify_dashboard_is_displayed()


@when("I login successfully")
def login_successfully(browser):
    """Login successfully"""
    login(browser, credentials.ADMIN_USERNAME, credentials.ADMIN_PASSWORD)
