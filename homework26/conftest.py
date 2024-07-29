import pytest
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
@pytest.fixture(scope="session")
def driver():
    driver = webdriver.WebDriver()  # Ініціалізуємо веб-драйвер
    yield driver
    driver.quit()


@pytest.fixture
def open_start_page(driver):
    return driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")

