from selenium.webdriver.common.by import By
from POM.components.base import BasePage


class MainMenu(BasePage):
    DASHBOARD = (By.ID, "menu_dashboard_index")
    RECRUITMENT = (By.ID, "menu_recruitment_viewRecruitmentModule")

    def click_dashboard(self):
        self.driver.find_element(*self.DASHBOARD).click()

    def click_recruitment(self):
        self.driver.find_element(*self.RECRUITMENT).click()
