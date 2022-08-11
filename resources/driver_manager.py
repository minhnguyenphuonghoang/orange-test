from selenium import webdriver


class DriverManager:
    """Manage browser, browser operations and cache"""

    def __init__(self, kwargs):
        # set new driver
        browser = kwargs.get("browser")
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "edge":
            self.driver = webdriver.Edge()
        elif browser == "safari":
            self.driver = webdriver.Safari()
        else:
            raise Exception("Browser not supported")

        # set driver options
        self.driver.implicitly_wait(kwargs.get("implicit_wait", 10))

        # set driver size
        if kwargs.get("maximize_browser"):
            self.driver.maximize_window()
        self.base_url = kwargs.get("base_url")

    def get_driver(self):
        """Return driver"""
        return self.driver

    def get_base_url(self):
        """Return base url"""
        return self.base_url
