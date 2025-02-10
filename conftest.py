import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()  # Включение полноэкранного отображения браузера
    driver.implicitly_wait(2) # Замена слипу (будет автоматически ждать появление элемента 2 сек.)
    yield driver
    driver.quit()