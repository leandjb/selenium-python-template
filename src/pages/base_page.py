from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
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

    def type_text(self, locator, text):
        self.wait_for_element(locator).clear()
        self.wait_for_element(locator).send_keys(text)

    def select_text_from_dropdown(self, locator, text):
        select = Select(self.wait_for_element(locator))
        select.select_by_visible_text(text)

    def select_index_from_dropdown(self, locator, index):
        select = Select(self.wait_for_element(locator))
        select.select_by_index(index)

    def select_element_btn(self, locator):
        """Select checkbox or radiobutton if it is not selected"""
        checkbox = self.wait_for_element(locator)
        if not checkbox.is_selected():
            checkbox.click()

    def unselect_checkbox(self, locator):
        """Unselect the checkbox or radiobutton if it is selected"""
        checkbox = self.wait_for_element(locator)
        if checkbox.is_selected():
            checkbox.click()
