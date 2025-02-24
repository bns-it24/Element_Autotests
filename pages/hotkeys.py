from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.homepage import HomePage, HomePageChecks
from pages.base_actions import BaseActions
from datetime import date
import time


class HotKeys(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.home_page = HomePage(driver)
        self.home_checks = HomePageChecks(driver)

    def hotkeys_alt_s_e_x(self):

        self.home_page.get_link("http://localhost:443/webapp/index.html#/home")
        self.home_page.add_new_res_string()
        self.home_page.select_hotel(1)

        self.home_page.fill_required_fields(
            row_index=1,
            arrival_date=date.today().strftime("%d%m%Y"),
            room_count=1,
            adults=1,
            children=1,
            guest_category="RAC",
            rate="RACK",
            room_type="KING",
            payment_info="VS 1111222233334444 0825",
            guest_name=self.home_page.generate_guest_name(),
            country="Russian Federation",
            contact_name="BILBO",
            booking_source="B"
        )

        self.send_hotkey_to_element(By.ID, "__item3-__xmlview2--homeMainTable-0", Keys.ALT, 's')
        self.home_checks.check_saving_reservation()

        self.send_hotkey_to_body(Keys.ALT, 'e')

        self.send_hotkey_to_element(By.ID, "__item3-__xmlview2--homeMainTable-0", Keys.ALT, 'x')
        self.home_checks.check_cancelling_reservation()

        self.home_page.clear_home_page()

    def hotkeys_alt_i(self):

        self.home_page.get_link("http://localhost:443/webapp/index.html#/home")
        self.home_page.add_new_res_string()
        self.home_page.select_hotel(1)

        # Заполнение обязательных полей
        self.home_page.fill_required_fields(
            row_index=1,
            arrival_date=date.today().strftime("%d%m%Y"),
            room_count=1,
            adults=1,
            children=1,
            guest_category="RAC",
            rate="RACK",
            room_type="KING",
            payment_info="VS 1111222233334444 0825",
            guest_name=self.home_page.generate_guest_name(),
            country="Russian Federation",
            contact_name="BILBO",
            booking_source="B"
        )

        self.home_page.save_reservation()
        self.home_checks.check_saving_reservation()

        # Включение режима редактирования
        self.home_page.edit_mode_on()

        # Изменение имени гостя
        self.home_page.send_keys_to_element(By.ID, "__xmlview2--homeTabInputName_G-inner", "THIN/MARIA/MRS")
        self.home_checks.verify_field_value(By.ID, "__xmlview2--homeTabInputName_G-inner", "THIN/MARIA/MRS")

        # Отмена изменений (Alt + I)
        self.send_hotkey_to_body(Keys.ALT, 'i')
        self.click_element(By.ID, "__mbox-btn-0-BDI-content")

        # Проверка отмены изменений
        self.home_checks.verify_field_value(By.ID, "__xmlview2--homeTabInputName_G-inner", "", negate=True)

        # Закрытие брони
        self.home_page.cancel_reservation(1)
        self.home_checks.check_cancelling_reservation()
        self.home_page.clear_home_page()

    def hotkeys_alt_n_h(self):

        self.home_page.get_link("http://localhost:443/webapp/index.html#/home")
        time.sleep(5)

        # Добавление строки бронирования (Alt + N)
        self.send_hotkey_to_body(Keys.ALT, 'n')
        self.home_checks.check_adding_new_res_string()

        # Выбор отеля и заполнение полей
        self.home_page.select_hotel(1)
        self.home_page.fill_required_fields(
            row_index=1,
            arrival_date=date.today().strftime("%d%m%Y"),
            room_count=1,
            adults=1,
            children=1,
            guest_category="RAC",
            rate="RACK",
            room_type="KING",
            payment_info="VS 1111222233334444 0825",
            guest_name=self.home_page.generate_guest_name(),
            country="Russian Federation",
            contact_name="BILBO",
            booking_source="B"
        )

        self.home_page.save_reservation()
        self.home_checks.check_saving_reservation()

        # Включение режима редактирования
        self.home_page.edit_mode_on()

        # Подселение (Alt + H)
        self.send_hotkey_to_element(By.ID, "__item3-__xmlview2--homeMainTable-0", Keys.ALT, 'h')
        time.sleep(1)

        # Проверка статуса "NEW_SHARED"
        self.home_checks.verify_field_value(By.ID, "__input7-__xmlview2--homeMainTable-1-inner", "NEW_SHARED")

        # Проверка пустых полей
        self.home_checks.verify_field_value(By.ID, "__input1-__xmlview2--homeMainTable-0-inner", "")
        self.home_checks.verify_field_value(By.ID, "__input2-__xmlview2--homeMainTable-0-inner", "")

        # Заполнение недостающих полей
        self.home_page.fill_guest_info(row_index=1)

        # Сохранение брони
        self.home_page.save_reservation()
        self.home_checks.verify_field_value(By.ID, "__input7-__xmlview2--homeMainTable-0-inner", "SAVED_SHARED")

        # Отмена брони
        self.home_page.cancel_reservation(1)
        self.home_checks.check_cancelling_reservation()
        self.home_page.clear_home_page()

    def send_hotkey_to_body(self, modifier_key, key):

        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys(modifier_key, key)

    def send_hotkey_to_element(self, by, value, modifier_key, key):

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))
        element.send_keys(modifier_key, key)