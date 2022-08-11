from selenium.webdriver.common.by import By
from POM.components.base import BasePage
from selenium.webdriver.support.ui import Select
import time


class FilterForm(BasePage):
    SEARCH_BTN = (By.ID, "btnSrch")
    RESET_BTN = (By.ID, "btnRst")

    def select_dropdown(self, dropdown_ele, value):
        select = Select(self.driver.find_element(*dropdown_ele))
        select.select_by_visible_text(value)

    def click_search(self):
        self.driver.find_element(*self.SEARCH_BTN).click()
        # for element is updated
        # temporarily solution, better to track if element is updated or not
        time.sleep(2)
