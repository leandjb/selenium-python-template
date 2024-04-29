import pytest
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


@pytest.fixture
def browser():
    driver = webdriver.WebDriver()
    driver.implicitly_wait(4)
    driver.get(
        "https://thefreerangetester.github.io/sandbox-automation-testing/")
    # driver.maximize_window()

    yield driver
    driver.close()


@pytest.mark.search
def test_checkbox(browser):
    container_checkbox = browser.find_element(By.CLASS_NAME, "mt-3")
    checkbox_burger = container_checkbox.find_element(By.ID,
                                                      "checkbox-1")  # locator inside container
    checkbox_burger.click()


@pytest.mark.search
def test_checkbox_2(browser):
    container_checkbox = browser.find_element(By.CLASS_NAME, "mt-3")
    checkbox_burger = browser.find_element(By.ID, "checkbox-1")
    checkbox_burger.click()


@pytest.mark.hoveronbutton
def test_hover_enviar_button(browser):
    button = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        # (By.CSS_SELECTOR, "button.btn:nth-child(5)")))
        (By.XPATH, "//button[contains(text(),'Enviar')]")))

    color_before_hover = button.value_of_css_property("background-color")

    ActionChains(browser).move_to_element(button).perform()
    WebDriverWait(browser, 10).until(
        lambda d: button.value_of_css_property(
            "background-color") != color_before_hover)

    color_after_hover = button.value_of_css_property("background-color")

    assert color_before_hover != color_after_hover
