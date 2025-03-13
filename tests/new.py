from pages.homepage import HomePage, HomePageChecks
from pages.base_actions import BaseActions
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("driver")
class TestReservationFlow:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.home_page = HomePage(driver)
        self.checks = HomePageChecks(driver)
        self.home_page.get_link()

    def test_full_reservation_cycle(self):
        test_data = {
            "row_index": 1,
            "arrival_date": "01102023",
            "room_count": "1",
            "adults": "2",
            "children": "0",
            "guest_category": "TEST",
            "rate": "1000",
            "room_type": "TWIN",
            "payment_info": "CASH",
            "guest_name": BaseActions.generate_guest_name(),
            "country": "Russian Federation",
            "contact_name": "Test Contact",
            "booking_source": "TEST"
        }

        self.home_page.add_new_res_string()
        self.checks.check_adding_new_res_string()

        self.home_page.select_hotel(test_data["row_index"])

        self.home_page.fill_required_fields(**test_data)
        self.home_page.save_reservation()
        self.checks.check_saving_reservation()

        self.home_page.edit_mode_on()
        self.home_page.cancel_reservation(test_data["row_index"])
        self.checks.check_cancelling_reservation()

        self.home_page.clear_home_page()
        self.checks.verify_field_value(
            By.ID,
            self.home_page.GUEST_NAME_INPUT,
            "",
            negate=False
        )