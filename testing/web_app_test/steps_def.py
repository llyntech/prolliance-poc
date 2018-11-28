import allure
import test_config

#Define step
@allure.step
def load_home_page(web_driver, home_page):
    web_driver.get(home_page)
    assert test_config.home_page_title in web_driver.title

