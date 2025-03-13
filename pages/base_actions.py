from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
from dateutil.relativedelta import relativedelta
import random
import string


class BaseActions:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by, value, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value))).click()

    def click_multiple_elements(self, element_ids, timeout=10):
        for element_id in element_ids:
            self.click_element(By.ID, element_id, timeout)

    def send_keys_to_element(self, by, value, keys, timeout=10):
        self.click_element(by, value, timeout)
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value)))
        element.clear()
        element.send_keys(keys)

    @staticmethod
    def generate_guest_name():
        part1 = ''.join(random.choices(string.ascii_uppercase, k=5))
        part2 = ''.join(random.choices(string.ascii_uppercase, k=5))
        suffix = random.choice(["MR", "MRS"])
        return f"{part1}/{part2}/{suffix}"

    def send_current_date(self, element_id):
        current_date = date.today()
        formatted_date = current_date.strftime("%d%m%Y")
        self.send_keys_to_element(By.ID, element_id, formatted_date)

    def send_future_date(self, element_id):
        future_date = date.today() + relativedelta(months=12)
        formatted_date = future_date.strftime("%d%m%Y")
        self.send_keys_to_element(By.ID, element_id, formatted_date)

    def to_homepage(self):
        self.click_element(By.ID, "__xmlview3--HOME-BDI-content")

    def get_link(self):
        url = "https://reserve.kube.ugmk.com/webapp/index.html#/home"
        self.driver.get(url)
