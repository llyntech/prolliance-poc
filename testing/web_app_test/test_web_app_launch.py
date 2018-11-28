import pytest


from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import test_config
import steps_def



#Define test case
@pytest.mark.parametrize('home_page', [test_config.app_url])
def test_load_website (init_wd, home_page):
    wd=init_wd
    steps_def.load_home_page(wd, home_page) # load one test step defined in steps_def.py