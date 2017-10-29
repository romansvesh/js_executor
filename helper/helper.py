from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.main_page import MainPage


class Helper:
    def __init__(self, driver):
        self._driver = driver

    def wait_for_element(self, time, locator):
        wait = WebDriverWait(self._driver, time)
        wait.until(expected_conditions.element_to_be_clickable((locator[0], locator[1])))

    def get_element_offset_width(self):
        main = MainPage(self)
        self.wait_for_element(20, main.SEARCH_FIELD)
        element = main.get_search_field()
        a = self._driver.execute_script('''
        return arguments[0].offsetWidth
        ''', element)
        print(type(a))
        return a