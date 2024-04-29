import unittest

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By


class FreeRangeTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = WebDriver()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_navigate_to_free_range_website(self):
        self.driver.get("https://www.freerangetesters.com")
        self.driver.find_element(By.XPATH,
                                 "//a[normalize-space()='Cursos' and @href]").click()
        assert self.driver.current_url == "https://www.freerangetesters.com/cursos"


if __name__ == '__main__':
    unittest.main()
