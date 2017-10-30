from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Helper:
    def __init__(self, driver):
        self._driver = driver

    def wait_for_element(self, time, locator):
        wait = WebDriverWait(self._driver, time)
        wait.until(expected_conditions.element_to_be_clickable((locator[0], locator[1])))

    def get_scrollbar_existance(self):
        """True if scrollbar exists"""
        return self._driver.execute_script('return document.body.scrollHeight > window.innerHeight')
