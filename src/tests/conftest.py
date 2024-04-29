import pytest
# from selenium.webdriver.firefox import webdriver
from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from src.pages.sandbox_page import SandboxPage


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.WebDriver()
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(
        'https://thefreerangetester.github.io/sandbox-automation-testing/')
    yield driver
    driver.quit()


@pytest.fixture
def sandbox_page(driver):
    return SandboxPage(driver)
