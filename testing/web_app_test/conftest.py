import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import test_config

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser types: chrome, firefox or ie"
    )


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def init_wd(browser,scope="module"):

    if browser == 'chrome':
        dc = DesiredCapabilities.CHROME
    if browser == 'firefox':
        dc = DesiredCapabilities.FIREFOX
    driver = webdriver.Remote(command_executor=test_config.hub_url,desired_capabilities=dc)
    yield driver

    driver.quit()

