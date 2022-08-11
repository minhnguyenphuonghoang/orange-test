from selenium.webdriver.common.by import By
from POM.components.main_menu import MainMenu
from POM.components.filter_form import FilterForm
from POM.components.search_result import SearchResult
import time


class Vacancies(MainMenu, FilterForm, SearchResult):

    VACANCIES = (By.XPATH, '//h1[text()="Vacancies"]')
    VACANCY_DROPDOWN = (By.ID, "vacancySearch_jobVacancy")

    def verify_vacancies_page_is_displayed(self):
        assert self.driver.find_element(*self.VACANCIES).is_displayed()
        assert self.driver.find_element(*self.VACANCY_DROPDOWN).is_displayed()
        time.sleep(
            2
        )  # for element is updated -> temporarily solution, better to track if element is updated or not
