import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()  # Убедитесь, что у вас установлен правильный WebDriver
    driver.maximize_window()
    yield driver
    driver.quit()


