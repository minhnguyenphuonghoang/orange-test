from selenium.webdriver.common.by import By
from POM.components.main_menu import MainMenu


class Dashboard(MainMenu):

    DASHBOARD = (By.XPATH, '//h1[text()="Dashboard"]')

    def verify_dashboard_is_displayed(self):
        element = self.driver.find_element(*self.DASHBOARD)
        assert element.is_displayed()
