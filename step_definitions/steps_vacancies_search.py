from pytest_bdd import when, then, parsers
from POM.pages.vacancies import Vacancies
from data import vacancies_data


@then("I navigate to Vacancies page")
def navigate_to_vacancies_page(browser):
    """Navigate to Vacancies page"""
    browser.driver.get(browser.base_url + "/index.php/recruitment/viewJobVacancy")
    Vacancies(browser.driver).verify_vacancies_page_is_displayed()


@when(parsers.parse('I search for vacancy "{vacancy}"'))
def search_for_vacancy(browser, vacancy):
    """Search for a vacancy"""
    Vacancies(browser.driver).select_dropdown(Vacancies.VACANCY_DROPDOWN, vacancy)
    Vacancies(browser.driver).click_search()


@then("I should see the vacancy")
def verify_search_result(browser):
    """Verify search result"""
    Vacancies(browser.driver).verify_result(vacancies_data.valid_vacancy)
