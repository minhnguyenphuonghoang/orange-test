from selenium.webdriver.common.by import By
from POM.components.base import BasePage


class SearchResult(BasePage):
    ADD_BTN = (By.ID, "btnAdd")
    DELETE_BTN = (By.ID, "btnDelete")
    RESULT_TABLE = (By.ID, "resultTable")

    def click_add(self):
        self.driver.find_element(*self.ADD_BTN).click()

    def verify_result(self, result_arr):
        """
        result_arr = [
            {
                'vacancy': '',
                'job_title': '',
                'hiring_manager': '',
                'status': ''
            },
            ...
        ]"""
        result_table = self.driver.find_element(*self.RESULT_TABLE)

        # verify number of rows match w/ number of expected result
        rows = result_table.find_elements(By.XPATH, "//tbody/tr")
        assert len(rows) == len(
            result_arr
        ), "Number of rows is not equal to number of results"

        # verify each row matches with expected result
        for result in result_arr:
            ele = '//td[.="{}"]'.format(result.get("vacancy"))
            ele += '/following-sibling::td[text()="{}"]'.format(result.get("job_title"))
            ele += '/following-sibling::td[text()="{}"]'.format(
                result.get("hiring_manager")
            )
            ele += '/following-sibling::td[text()="{}"]'.format(result.get("status"))

            assert result_table.find_element(By.XPATH, ele).is_displayed()
