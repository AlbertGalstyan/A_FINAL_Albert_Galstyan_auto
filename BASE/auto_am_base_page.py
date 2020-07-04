from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base_Page_Auto():
    def __init__(self, driver):
        self.driver = driver

    def _visit(self, url):
        self.driver.get(url)

    def _find(self, locator):
        return self.driver.find_element(locator["by"],
                                        locator["value"])

    def _find_elements(self, locator):
        return self.driver.find_elements(locator["by"],
                                         locator["value"])

    def _click(self, locator):
        self._find(locator).click()

    def _type(self, locator, input):
        self._find(locator).send_keys(input)

    def _get_attribute(self, locator, value):
        return self._find(locator).get_attribute(value)

    def _find_text(self, locator):
        return self._find(locator).text

    def _is_displayed(self, locator, timeout=0):
        if timeout > 0:
            try:

                wait = WebDriverWait(self.driver, timeout)
                wait.until(expected_conditions.visibility_of_element_located(
                    (locator["by"],
                     locator["value"]
                     )))
            except TimeoutException:
                return False
            return True
        else:
            try:
                return self._find(locator).is_displayed()
            except NoSuchElementException:
                return False
