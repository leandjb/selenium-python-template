import pytest
from src.pages.sandbox_page import SandboxPage


@pytest.mark.clic
def test_sandbox_click_enviar(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.click_enviar_button()
