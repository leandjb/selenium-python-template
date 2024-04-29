from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class SandboxPage(BasePage):
    ENVIAR_BUTTON = (By.XPATH, "//button[contains(text(),'Enviar')]")
    DYNAMIC_ID_BUTTON = (By.XPATH,
                         "//button[contains(text(),'Hacé click para generar un ID dinámico y mostrar el elemento oculto')]")
    HIDDEN_TEXT_LABEL = (By.ID, "hidden-element")

    def click_enviar_button(self):
        self.click_element(self.ENVIAR_BUTTON)

    def navigate_sandbox(self):
        self.navigate_to_url(
            'https://thefreerangetester.github.io/sandbox-automation-testing/')

    def click_dynamic_id_button(self):
        self.click_element(self.DYNAMIC_ID_BUTTON)

    def unselect_checkbox(self, label_text):
        self.unselect_checkbox(label_text)

    def select_checkbox_with_label(self, label_text):
        check_locator = (
            By.XPATH,
            f"//label[contains(.,'{label_text}')]//preceding-sibling::input[@type='checkbox']",
        )
        self.select_element_btn(check_locator)
