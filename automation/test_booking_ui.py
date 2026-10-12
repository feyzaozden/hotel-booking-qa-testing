
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://automationintesting.online/"


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()

    yield browser

    browser.quit()


def test_homepage_loads(driver):
    driver.get(BASE_URL)

    heading = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h1")
        )
    )

    assert heading.is_displayed()
    assert heading.text.strip() != ""


def test_rooms_navigation(driver):
    driver.get(BASE_URL)

    rooms_link = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "Rooms")
        )
    )

    rooms_link.click()

    WebDriverWait(driver, 15).until(
        EC.url_contains("#rooms")
    )

    assert "#rooms" in driver.current_url
