from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(locator))

    def click_element(self, locator):
        self.wait_for_element(locator).click()

    def navigate_to_url(self, url):
        self.driver.get(url)


