import json
import pytest
from resources.driver_manager import DriverManager


def pytest_addoption(parser):
    """Customize test command line options"""
    parser.addoption("--browser", action="store")
    parser.addoption("--base_url", action="store")


@pytest.fixture
def load_config(request, scope="session"):
    """Load config from json file"""
    # load config file
    with open("config.json") as config_file:
        config = json.load(config_file, encoding="utf-8")

    browser = request.config.option.browser
    if browser is not None:
        config["browser"] = browser

    base_url = request.config.option.base_url
    if base_url is not None:
        config["base_url"] = browser
    return config


@pytest.fixture
def browser(load_config):
    """Setup browser and load settings to browsers"""
    # Initialize the WebDriver instance
    driver_manager = DriverManager(load_config)
    yield driver_manager

    # Quit the WebDriver instance for the teardown
    driver_manager.driver.quit()
