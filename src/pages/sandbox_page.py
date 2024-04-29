from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class SandboxPage(BasePage):
    ENVIAR_BUTTON = (By.XPATH, "//button[contains(text(),'Enviar')]")

    def click_enviar_button(self):
        self.click_element(self.ENVIAR_BUTTON)

    def navigate_sandbox(self):
        self.navigate_to_url('https://thefreerangetester.github.io/sandbox-automation-testing/')

