from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_actions import BaseActions
from tests.final_test import logger


class RateManagement(BaseActions):
    RATE_MANAGEMENT_BUTTON = "__button0-internalBtn-BDI-content"
    RATES_BUTTON = "//*[text()='Rates']"
    CLASSES_BUTTON = "//*[text()='Classes']"
    HOTEL_SELECTOR = "__xmlview4--rate_search_hotel-label"
    HOTEL_OPTION = "__item11-__xmlview4--rate_search_hotel-1"
    CLASS_HOTEL_SELECTOR = "__xmlview4--rate_class_search_hotel-label"
    CLASS_HOTEL_OPTION = "__item11-__xmlview4--rate_class_search_hotel-1"
    RATE_CODE_INPUT = "__xmlview4--rate_dialog_rate_code-__xmlview4--rate_manager1-0-inner"
    RATE_DESCRIPTION_INPUT = "__xmlview4--rate_dialog_rate_description-__xmlview4--rate_manager1-0-inner"
    RATE_CATEGORY_SELECT = "__xmlview4--rate_dialog_rate_category-__xmlview4--rate_manager1-0-label"
    RATE_CATEGORY_OPTION = "__item17-__xmlview4--rate_manager1-0-__xmlview4--rate_dialog_rate_category-__xmlview4--rate_manager1-0-2"
    BEGIN_SELL_DATE_INPUT = "__xmlview4--rate_dialog_begin_sell_date-__xmlview4--rate_manager1-0-inner"
    END_SELL_DATE_INPUT = "__xmlview4--rate_dialog_end_sell_date-__xmlview4--rate_manager1-0-inner"
    MARKET_SELECT = "__xmlview4--rate_dialog_market-__xmlview4--rate_manager1-0-label"
    MARKET_OPTION = "__item18-__xmlview4--rate_manager1-0-__xmlview4--rate_dialog_market-__xmlview4--rate_manager1-0-10"
    SOURCE_SELECT = "__xmlview4--rate_dialog_source-__xmlview4--rate_manager1-0-label"
    SOURCE_OPTION = "__item19-__xmlview4--rate_manager1-0-__xmlview4--rate_dialog_source-__xmlview4--rate_manager1-0-2"
    ROOM_TYPE_SELECT = "__xmlview4--rate_dialog_room_type-__xmlview4--rate_manager1-0-arrow"
    ROOM_TYPE_KING = "//*[text()='KING']"
    ROOM_TYPE_TWIN = "//*[text()='TWIN']"
    COMMISSION_INPUT = "__xmlview4--rate_dialog_commission-__xmlview4--rate_manager1-0-inner"
    ADULT_MAX_INPUT = "__xmlview4--rate_dialog_adult_max-__xmlview4--rate_manager1-0-inner"
    CHILD_MAX_INPUT = "__xmlview4--rate_dialog_child_max-__xmlview4--rate_manager1-0-inner"
    TRX_CODE_SELECT = "__xmlview4--rate_dialog_trx_code-__xmlview4--rate_manager1-0-arrow"
    TRX_CODE_OPTION = "__item21-__xmlview4--rate_manager1-0-__xmlview4--rate_dialog_trx_code-__xmlview4--rate_manager1-0-3"
    CURRENCY_CODE_SELECT = "__xmlview4--rate_dialog_currency_code-__xmlview4--rate_manager1-0-arrow"
    CURRENCY_CODE_OPTION = "__item22-__xmlview4--rate_manager1-0-__xmlview4--rate_dialog_currency_code-__xmlview4--rate_manager1-0-0"
    ACTIVE_CHECKBOX = "__xmlview4--rate_dialog_cb_active-__xmlview4--rate_manager1-0-CbBg"
    RATE_DETAILS_BUTTON = "__filter0-text"
    STAY_DATE_RANGE_INPUT = "__xmlview4--rate_dialog_stay_date_range-__xmlview4--rate_manager_date_ranges-0-inner"
    BASE_PRICE_INPUT = "__xmlview4--rate_dialog_base_price-__xmlview4--rate_manager_date_ranges-0-inner"
    WEEKDAYS_CHECKBOXES = [
        "__box26-__xmlview4--rate_manager_date_ranges-0-CbBg",
        "__box27-__xmlview4--rate_manager_date_ranges-0-CbBg",
        "__box28-__xmlview4--rate_manager_date_ranges-0-CbBg",
        "__box29-__xmlview4--rate_manager_date_ranges-0-CbBg",
        "__box30-__xmlview4--rate_manager_date_ranges-0-CbBg",
        "__box31-__xmlview4--rate_manager_date_ranges-0-CbBg",
        "__box32-__xmlview4--rate_manager_date_ranges-0-CbBg"
    ]
    CLASS_CODE_INPUT = "__xmlview4--class_dialog_code-__xmlview4--class_manager-0-inner"
    CLASS_DESCRIPTION_INPUT = "__xmlview4--class_dialog_description-__xmlview4--class_manager-0-inner"
    CLASS_BEGIN_DATE_INPUT = "__xmlview4--class_dialog_begin_sell_date-__xmlview4--class_manager-0-inner"
    CLASS_END_DATE_INPUT = "__xmlview4--class_dialog_end_sell_date-__xmlview4--class_manager-0-inner"
    CLASS_ACTIVE_CHECKBOX = "__xmlview4--class_dialog_is_active-__xmlview4--class_manager-0-CbBg"
    DELETE_RATE_BUTTON = "__button10-__clone5-img"
    DELETE_CLASS_BUTTON = "__button9-__clone5-img"
    CONFIRM_DELETE_BUTTON = "__mbox-btn-0-BDI-content"
    RATE_ADD_BUTTON = "__button8-inner"
    RATE_SAVE_BUTTON = "__button13-BDI-content"
    CLASS_ADD_BUTTON = "__button7-img"
    CLASS_SAVE_BUTTON = "__button12-BDI-content"

    def __init__(self, driver):
        super().__init__(driver)

    def open_rates(self):
        self.click_element(By.ID, self.RATE_MANAGEMENT_BUTTON)
        self.click_element(By.XPATH, self.RATES_BUTTON)
        self.click_element(By.ID, self.HOTEL_SELECTOR)
        self.click_element(By.ID, self.HOTEL_OPTION)

    def open_classes(self):
        self.click_element(By.ID, self.RATE_MANAGEMENT_BUTTON)
        self.click_element(By.XPATH, self.CLASSES_BUTTON)
        self.click_element(By.ID, self.CLASS_HOTEL_SELECTOR)
        self.click_element(By.ID, self.CLASS_HOTEL_OPTION)

    def search_rate(self, rate_code):
        self.send_keys_to_element(By.ID, "__xmlview4--rate_search_rate_code-inner", rate_code)
        self.click_element(By.ID, "__button7-BDI-content")

    def search_class(self, class_code):
        self.send_keys_to_element(By.ID, "__xmlview4--rate_class_search_code-inner", class_code)
        self.click_element(By.ID, "__xmlview4--rate_class_search_button-content")

    def fill_rate_required_fields(self, rate_code, rate_description):
        self.send_keys_to_element(By.ID, self.RATE_CODE_INPUT, rate_code)
        self.send_keys_to_element(By.ID, self.RATE_DESCRIPTION_INPUT, rate_description)
        self.click_element(By.ID, self.RATE_CATEGORY_SELECT)
        self.click_element(By.ID, self.RATE_CATEGORY_OPTION)
        self.send_current_date(self.BEGIN_SELL_DATE_INPUT)
        self.send_future_date(self.END_SELL_DATE_INPUT)
        self.click_element(By.ID, self.MARKET_SELECT)
        self.click_element(By.ID, self.MARKET_OPTION)
        self.click_element(By.ID, self.SOURCE_SELECT)
        self.click_element(By.ID, self.SOURCE_OPTION)
        self.click_element(By.ID, self.ROOM_TYPE_SELECT)
        self.click_element(By.XPATH, self.ROOM_TYPE_KING)
        self.click_element(By.ID, self.ROOM_TYPE_SELECT)
        self.click_element(By.XPATH, self.ROOM_TYPE_TWIN)
        self.send_keys_to_element(By.ID, self.COMMISSION_INPUT, "777")
        self.send_keys_to_element(By.ID, self.ADULT_MAX_INPUT, "5")
        self.send_keys_to_element(By.ID, self.CHILD_MAX_INPUT, "2")
        self.click_element(By.ID, self.TRX_CODE_SELECT)
        self.click_element(By.ID, self.TRX_CODE_OPTION)
        self.click_element(By.ID, self.CURRENCY_CODE_SELECT)
        self.click_element(By.ID, self.CURRENCY_CODE_OPTION)
        self.click_element(By.ID, self.ACTIVE_CHECKBOX)
        self.click_element(By.ID, self.RATE_DETAILS_BUTTON)
        self.send_keys_to_element(By.ID, self.STAY_DATE_RANGE_INPUT, "01012025-31122025")
        self.send_keys_to_element(By.ID, self.BASE_PRICE_INPUT, "777")
        self.click_multiple_elements(self.WEEKDAYS_CHECKBOXES)

    def fill_class_required_fields(self):
        self.send_keys_to_element(By.ID, self.CLASS_CODE_INPUT, "NtestN")
        self.send_keys_to_element(By.ID, self.CLASS_DESCRIPTION_INPUT, "Test plus test")
        self.send_current_date(self.CLASS_BEGIN_DATE_INPUT)
        self.send_future_date(self.CLASS_END_DATE_INPUT)
        self.click_element(By.ID, self.CLASS_ACTIVE_CHECKBOX)

    def delete_rate(self, rate_code):
        self.search_rate(rate_code)
        self.click_element(By.ID, self.DELETE_RATE_BUTTON)
        self.click_element(By.ID, self.CONFIRM_DELETE_BUTTON)

    def delete_class(self, class_code):
        self.search_class(class_code)
        self.click_element(By.ID, self.DELETE_CLASS_BUTTON)
        self.click_element(By.ID, self.CONFIRM_DELETE_BUTTON)


class RateManagementChecks(BaseActions):
    RATE_SAVE_SUCCESS_MESSAGE = "//*[text()='The rate class 1TEST1 saved successfully']"
    RATE_DELETE_SUCCESS_MESSAGE = "//*[text()='The rate class 1TEST1 removed successfully']"
    CLASS_SAVE_SUCCESS_MESSAGE = "//*[text()='The rate class NtestN saved successfully']"
    CLASS_DELETE_SUCCESS_MESSAGE = "//*[text()='The rate class NtestN removed successfully']"

    def __init__(self, driver):
        super().__init__(driver)

    def check_saving_rate(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.RATE_SAVE_SUCCESS_MESSAGE)))
            logger.info("Тариф успешно сохранен")
        except TimeoutException:
            logger.error("Сообщение о сохранении тарифа не найдено")
            raise

    def check_deleting_rate(self):
        try:
            success_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.RATE_DELETE_SUCCESS_MESSAGE)))
            logger.info("Сообщение об успешном удалении тарифа отображается.")
            assert success_message_element.is_displayed(), "Сообщение об успешном удалении не отображается."
        except TimeoutException:
            logger.error("Сообщение об успешном удалении тарифа не найдено.")
            raise

    def check_saving_class(self):
        try:
            success_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.CLASS_SAVE_SUCCESS_MESSAGE)))
            logger.info("Сообщение об успешном сохранении класса отображается.")
            assert success_message_element.is_displayed(), "Сообщение об успешном сохранении не отображается."
        except TimeoutException:
            logger.error("Сообщение об успешном сохранении класса не найдено.")
            raise

    def check_deleting_class(self):
        try:
            success_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.CLASS_DELETE_SUCCESS_MESSAGE)))
            logger.info("Сообщение об успешном удалении класса отображается.")
            assert success_message_element.is_displayed(), "Сообщение об успешном удалении не отображается."
        except TimeoutException:
            logger.error("Сообщение об успешном удалении класса не найдено.")
            raise