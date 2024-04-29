import pytest
from selenium.webdriver.firefox import webdriver


@pytest.fixture
def browser():
    driver: webdriver = webdriver.WebDriver()
    driver.get("https://www.duckduckgo.com")
    yield driver
    driver.close()


@pytest.mark.init
def test_enter_to_duckduckgo_website(browser):
    page_title: str = browser.title
    expected_title: str = 'DuckDuckGo — Privacy, simplified.'
    assert page_title == expected_title
