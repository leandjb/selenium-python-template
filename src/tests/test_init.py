import pytest

from selenium import webdriver

driver = webdriver.Chrome()


def test_enter_to_duckduckgo_website():
    driver.get("https://www.duckduckgo.com")
    page_title = driver.title
    expected_title = 'DuckDuckGo — Privacy, simplified.'
    assert page_title == expected_title
    driver.close()
