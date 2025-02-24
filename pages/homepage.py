from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from base_actions import BaseActions
from tests.final_test import logger


class HomePage(BaseActions):
    HOME_BUTTON_ADD = "__xmlview2--idHomeButtonAdd"
    HOTEL_SELECT_1ST_STR = "__select0-__xmlview2--homeMainTable-0-label"
    HOTEL_SELECT_2ND_STR = "__select0-__xmlview2--homeMainTable-1-label"
    HOTEL_SELECT_3RD_STR = "__select0-__xmlview2--homeMainTable-2-label"
    HOTEL_OPTION = "__item2-__select0-__xmlview2--homeMainTable-{}-1"
    DATE_PICKER = "__picker0-__xmlview2--homeMainTable-{}-inner"
    ROOM_COUNT_INPUT = "__input0-__xmlview2--homeMainTable-{}-inner"
    ADULTS_INPUT = "__input1-__xmlview2--homeMainTable-{}-inner"
    CHILDREN_INPUT = "__input2-__xmlview2--homeMainTable-{}-inner"
    GUEST_CATEGORY_INPUT = "__input3-__xmlview2--homeMainTable-{}-inner"
    RATE_INPUT = "__input4-__xmlview2--homeMainTable-{}-inner"
    ROOM_TYPE_INPUT = "__input5-__xmlview2--homeMainTable-{}-inner"
    PAYMENT_INFO_INPUT = "__xmlview2--homeTabInputHold_G-inner"
    GUEST_NAME_INPUT = "__xmlview2--homeTabInputName_G-inner"
    COUNTRY_SELECT = "__form1--FC-NoHead--Grid-wrapperfor-__xmlview2--selectCountry_G"
    CONTACT_NAME_INPUT = "__xmlview2--homeTabInputName2_G-inner"
    BOOKING_SOURCE_INPUT = "__xmlview2--homeTabInputBkngSrc_G-inner"
    SAVE_BUTTON = "__xmlview2--idHomeButtonSave"
    CANCEL_BUTTON = "__xmlview2--idHomeButtonCancel"
    CLEAR_BUTTON = "__xmlview2--idHomeButtonClear-inner"
    RES_STRING_SELECT = "__item3-__xmlview2--homeMainTable-{}"

    def __init__(self, driver):
        super().__init__(driver)

    def add_new_res_string(self):
        self.click_element(By.ID, self.HOME_BUTTON_ADD)

    def select_hotel(self, row_index):
        self.click_element(By.ID, getattr(self, f"HOTEL_SELECT_{row_index}ST_STR"))
        self.click_element(By.ID, self.HOTEL_OPTION.format(row_index - 1))

    def fill_required_fields(self, row_index, arrival_date, room_count, adults, children, guest_category, rate, room_type,payment_info, guest_name, country, contact_name, booking_source):
        self.send_keys_to_element(By.ID, self.DATE_PICKER.format(row_index - 1), arrival_date)
        self.send_keys_to_element(By.ID, self.ROOM_COUNT_INPUT.format(row_index - 1), room_count)
        self.send_keys_to_element(By.ID, self.ADULTS_INPUT.format(row_index - 1), adults)
        self.send_keys_to_element(By.ID, self.CHILDREN_INPUT.format(row_index - 1), children)
        self.send_keys_to_element(By.ID, self.GUEST_CATEGORY_INPUT.format(row_index - 1), guest_category)
        self.send_keys_to_element(By.ID, self.RATE_INPUT.format(row_index - 1), rate)
        self.send_keys_to_element(By.ID, self.ROOM_TYPE_INPUT.format(row_index - 1), room_type)
        self.send_keys_to_element(By.ID, self.PAYMENT_INFO_INPUT, payment_info)
        self.send_keys_to_element(By.ID, self.GUEST_NAME_INPUT, guest_name)
        self.click_element(By.ID, self.COUNTRY_SELECT)
        self.click_element(By.XPATH, f"//*[text()='{country}']")
        self.send_keys_to_element(By.ID, self.CONTACT_NAME_INPUT, contact_name)
        self.send_keys_to_element(By.ID, self.BOOKING_SOURCE_INPUT, booking_source)

    def save_reservation(self):
        self.click_element(By.ID, self.SAVE_BUTTON)

    def cancel_reservation(self, row_index):
        self.click_element(By.ID, self.RES_STRING_SELECT.format(row_index - 1))
        self.click_element(By.ID, self.CANCEL_BUTTON)

    def clear_home_page(self):
        self.click_element(By.ID, self.CLEAR_BUTTON)

    def edit_mode_on(self):
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.ALT, 'e')

    def run_custom_reservation(self, row_index, arrival_date, room_count, adults, children, guest_category, rate,
                              room_type, payment_info, guest_name, country, contact_name, booking_source):
        self.add_new_res_string()
        self.select_hotel(row_index)
        self.fill_required_fields(row_index, arrival_date, room_count, adults, children, guest_category, rate, room_type,
                                 payment_info, guest_name, country, contact_name, booking_source)
        self.save_reservation()
        self.edit_mode_on()
        self.cancel_reservation(row_index)
        self.clear_home_page()

    def fill_guest_info(self, row_index):
        guest_name = self.generate_guest_name()
        self.send_keys_to_element(By.ID, self.GUEST_NAME_INPUT, guest_name)
        self.click_element(By.ID, self.COUNTRY_SELECT)
        self.click_element(By.XPATH, "//*[text()='Russian Federation']")

class HomePageChecks(BaseActions):
    RES_TABLE_BODY = "__xmlview2--homeMainTable-tblBody"
    SUCCESS_SAVE_MESSAGE = "//*[text()='The data is saved']"
    SUCCESS_CANCEL_MESSAGE = "//*[text()='The reservation has been successfully cancelled']"
    RES_STATUS_INPUT = "__input7-__xmlview2--homeMainTable-{}-inner"

    def __init__(self, driver):
        super().__init__(driver)

    def check_adding_new_res_string(self):
        try:
            new_res_string = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, self.RES_TABLE_BODY)))
            logger.info("Новая строка бронирования отображается.")
            assert new_res_string.is_displayed(), "Новая строка бронирования найдена, но не отображается."
        except TimeoutException:
            logger.error("Новая строка бронирования не обнаружена.")
            raise

    def check_saving_reservation(self):
        try:
            success_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.SUCCESS_SAVE_MESSAGE)))
            logger.info("Сообщение об успешном сохранении бронирования отображается.")
            assert success_message_element.is_displayed(), "Сообщение об успешном сохранении не отображается."
        except TimeoutException:
            logger.error("Сообщение об успешном сохранении бронирования не найдено.")
            raise

    def check_cancelling_reservation(self):
        try:
            success_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.SUCCESS_CANCEL_MESSAGE)))
            logger.info("Сообщение об успешном удалении бронирования отображается.")
            assert success_message_element.is_displayed(), "Сообщение об успешном удалении не отображается."
        except TimeoutException:
            logger.error("Сообщение об успешном удалении бронирования не найдено.")
            raise

    def verify_field_value(self, by, value, expected_value, negate=False):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((by, value)))
            actual_value = element.get_attribute('value')
            if negate:
                logger.info(f"Проверка: значение поля НЕ равно '{expected_value}'.")
                assert actual_value != expected_value, f"Значение поля равно '{expected_value}', но не должно быть."
            else:
                logger.info(f"Проверка: значение поля равно '{expected_value}'.")
                assert actual_value == expected_value, f"Ожидаемое значение: '{expected_value}', фактическое: '{actual_value}'."
        except TimeoutException:
            logger.error(f"Элемент с локатором '{value}' не найден.")
            raise

    def check_reservation_status(self, row_index, expected_status):
        try:
            res_status = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, self.RES_STATUS_INPUT.format(row_index))))
            logger.info(f"Проверка статуса бронирования: ожидаемый статус - '{expected_status}'.")
            assert res_status == expected_status, f"Ожидаемый статус - {expected_status}, фактический статус - {res_status}"
        except TimeoutException:
            logger.error(f"Статус бронирования в строке {row_index} не обнаружен.")
            raise