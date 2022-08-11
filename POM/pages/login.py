from selenium.webdriver.common.by import By
from POM.components.base import BasePage


class Login(BasePage):
    """Lgin page"""

    USERNAME_TXT = (By.ID, "txtUsername")
    PASSWORD_TXT = (By.ID, "txtPassword")
    LOGIN_BTN = (By.ID, "btnLogin")

    def verify_login_page_is_displayed(self):
        """Verify login page is displayed"""
        assert self.driver.find_element(*self.USERNAME_TXT).is_displayed()
        assert self.driver.find_element(*self.PASSWORD_TXT).is_displayed()
        assert self.driver.find_element(*self.LOGIN_BTN).is_displayed()

    def input_username(self, username):
        """Input username"""
        self.driver.find_element(*self.USERNAME_TXT).send_keys(username)

    def input_password(self, password):
        """Input password"""
        self.driver.find_element(*self.PASSWORD_TXT).send_keys(password)

    def click_login(self):
        """Click login"""
        self.driver.find_element(*self.LOGIN_BTN).click()
