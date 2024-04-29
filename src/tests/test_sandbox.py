import pytest
from src.pages.sandbox_page import SandboxPage


@pytest.mark.clic_enviar
@pytest.mark.regression
def test_sandbox_click_enviar(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.click_enviar_button()


@pytest.mark.dynamic_id
@pytest.mark.regression
def test_sandbox_click_dynamic_id(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.click_dynamic_id_button()

    actual_hidden_text = sandbox_page.wait_for_element(SandboxPage.HIDDEN_TEXT_LABEL)
    expected_hidden_text = "OMG, aparezco después de 3 segundos de haber hecho click en el botón 👻."

    assert expected_hidden_text in actual_hidden_text.text

@pytest.mark.checkbox
@pytest.mark.regression
def test_sandbox_checkboxes(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.select_checkbox_with_label("Torta")
