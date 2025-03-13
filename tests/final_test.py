from datetime import date
from selenium.webdriver.common.by import By
from pages.homepage import HomePage
from pages.homepage import HomePageChecks
from pages.rate_management import RateManagement, RateManagementChecks
import pytest
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

test_data_onepage = [
    {
        "row_index": 1,
        "arrival_date": date.today().strftime("%d%m%Y"),
        "room_count": "1",
        "adults": "1",
        "children": "0",
        "guest_category": "RAC",
        "rate": "TOT",
        "room_type": "KING",
        "payment_info": "VS 1111222233334444 0825",
        "guest_name": "THIN/MARIA/MRS",
        "country": "USA",
        "contact_name": "BORIS",
        "booking_source": "K"
    },
    {
        "row_index": 2,
        "arrival_date": date.today().strftime("%d%m%Y"),
        "room_count": "1",
        "adults": "2",
        "children": "0",
        "guest_category": "AWD",
        "rate": "SWAG",
        "room_type": "TWIN",
        "payment_info": "CA",
        "guest_name": "THIN/MARIA/MRS",
        "country": "Russian Federation",
        "contact_name": "ANTON",
        "booking_source": "K"
    }
]

test_data_multipage = [
    {
        "row_index": 1,
        "arrival_date": date.today().strftime("%d%m%Y"),
        "room_count": "1",
        "adults": "1",
        "children": "0",
        "guest_category": "RAC",
        "rate": "TOT",
        "room_type": "KING",
        "payment_info": "VS 1111222233334444 0825",
        "guest_name": "THIN/MARIA/MRS",
        "country": "USA",
        "contact_name": "BORIS",
        "booking_source": "K"
    },
    {
        "row_index": 2,
        "arrival_date": date.today().strftime("%d%m%Y"),
        "room_count": "1",
        "adults": "2",
        "children": "0",
        "guest_category": "AWD",
        "rate": "SWAG",
        "room_type": "TWIN",
        "payment_info": "CA",
        "guest_name": "THIN/MARIA/MRS",
        "country": "Russian Federation",
        "contact_name": "ANTON",
        "booking_source": "K"
    },
    {
        "row_index": 3,
        "arrival_date": date.today().strftime("%d%m%Y"),
        "room_count": "1",
        "adults": "1",
        "children": "1",
        "guest_category": "RAC",
        "rate": "TOT",
        "room_type": "KING",
        "payment_info": "VS 1111222233334444 0825",
        "guest_name": "THIN/MARIA/MRS",
        "country": "USA",
        "contact_name": "BORIS",
        "booking_source": "K"
    }
]

@pytest.mark.parametrize("reservation_data", test_data_onepage)
def test_onepage_reservation(driver, reservation_data):
    home_page = HomePage(driver)
    home_checks = HomePageChecks(driver)

    logger.info(f"Запуск цикла бронирования для строки {reservation_data['row_index']}")

    logger.info("Открытие домашней страницы")
    home_page.get_link()

    logger.info(f"Добавление и сохранение строки бронирования {reservation_data['row_index']}")
    home_page.run_custom_reservation(
        row_index=reservation_data["row_index"],
        arrival_date=reservation_data["arrival_date"],
        room_count=reservation_data["room_count"],
        adults=reservation_data["adults"],
        children=reservation_data["children"],
        guest_category=reservation_data["guest_category"],
        rate=reservation_data["rate"],
        room_type=reservation_data["room_type"],
        payment_info=reservation_data["payment_info"],
        guest_name=reservation_data["guest_name"],
        country=reservation_data["country"],
        contact_name=reservation_data["contact_name"],
        booking_source=reservation_data["booking_source"]
    )
    home_checks.check_reservation_status(row_index=reservation_data["row_index"], expected_status="NEW")
    home_checks.check_saving_reservation()
    home_checks.check_reservation_status(row_index=reservation_data["row_index"], expected_status="SAVED")

    logger.info("Включение режима редактирования")
    home_page.edit_mode_on()

    logger.info(f"Отмена строки бронирования {reservation_data['row_index']}")
    home_page.cancel_reservation(row_index=reservation_data["row_index"])
    home_checks.check_cancelling_reservation()
    home_checks.check_reservation_status(row_index=reservation_data["row_index"], expected_status="CANCELLED")

    logger.info("Очистка конфигуратора бронирования")
    home_page.clear_home_page()

    logger.info(f"Цикл бронирования для строки {reservation_data['row_index']} завершен")


@pytest.mark.parametrize("reservation_data", test_data_multipage)
def test_multipage_reservation(driver, reservation_data):
    home_page = HomePage(driver)
    home_checks = HomePageChecks(driver)

    logger.info("Открытие домашней страницы")
    home_page.get_link("http://localhost:443/webapp/index.html#/home")

    logger.info(f"Добавление и сохранение строки бронирования {reservation_data['row_index']}")
    home_page.run_custom_reservation(
        row_index=reservation_data["row_index"],
        arrival_date=reservation_data["arrival_date"],
        room_count=reservation_data["room_count"],
        adults=reservation_data["adults"],
        children=reservation_data["children"],
        guest_category=reservation_data["guest_category"],
        rate=reservation_data["rate"],
        room_type=reservation_data["room_type"],
        payment_info=reservation_data["payment_info"],
        guest_name=reservation_data["guest_name"],
        country=reservation_data["country"],
        contact_name=reservation_data["contact_name"],
        booking_source=reservation_data["booking_source"]
    )
    home_checks.check_saving_reservation()
    home_checks.check_reservation_status(row_index=reservation_data["row_index"], expected_status="SAVED")

    logger.info("Включение режима редактирования")
    home_page.edit_mode_on()

    logger.info(f"Отмена строки бронирования {reservation_data['row_index']}")
    home_page.cancel_reservation(row_index=reservation_data["row_index"])
    home_checks.check_cancelling_reservation()
    home_checks.check_reservation_status(row_index=reservation_data["row_index"], expected_status="CANCELLED")

    logger.info("Очистка конфигуратора бронирования")
    home_page.clear_home_page()


def test_add_rate_plan(driver):
    home_page = HomePage(driver)
    home_checks = HomePageChecks(driver)
    rate_mgmt = RateManagement(driver)
    rate_checks = RateManagementChecks(driver)

    logger.info("=== Начало теста: Добавление тарифного плана ===")

    try:
        logger.info("Шаг 1: Открытие раздела Rates")
        rate_mgmt.open_rates()

        logger.info("Шаг 2: Добавление нового тарифа")
        rate_mgmt.click_element(By.ID, rate_mgmt.RATE_ADD_BUTTON)

        logger.info("Шаг 3: Заполнение полей тарифа")
        rate_mgmt.fill_rate_required_fields(
            rate_code="1TEST1",
            rate_description="Testing Rate"
        )

        logger.info("Шаг 4: Сохранение тарифа")
        rate_mgmt.click_element(By.ID, rate_mgmt.RATE_SAVE_BUTTON)
        rate_checks.check_saving_rate()

        logger.info("Шаг 5: Возврат на домашнюю страницу")
        home_page.to_homepage()

        logger.info("Шаг 6: Создание бронирования")
        home_page.run_custom_reservation(
            row_index=1,
            arrival_date=date.today().strftime("%d%m%Y"),
            room_count="1",
            adults="1",
            children="0",
            guest_category="RAC",
            rate="1TEST1",
            room_type="KING",
            payment_info="VS 1111222233334444 0825",
            guest_name=home_page.generate_guest_name(),
            country="USA",
            contact_name="BORIS",
            booking_source="K"
        )
        home_checks.check_saving_reservation()

        logger.info("Шаг 7: Удаление тарифа")
        rate_mgmt.open_rates()
        rate_mgmt.delete_rate("1TEST1")
        rate_checks.check_deleting_rate()

        logger.info("=== Тест успешно завершен ===")

    except Exception as e:
        logger.error(f"ОШИБКА: {str(e)}")
        raise


def test_add_rate_class(driver):
    rate_mgmt = RateManagement(driver)
    rate_checks = RateManagementChecks(driver)

    logger.info("=== Начало теста: Добавление и удаление класса тарифов ===")

    try:
        logger.info("Шаг 1: Открытие раздела Classes")
        rate_mgmt.open_classes()

        logger.info("Шаг 2: Добавление нового класса")
        rate_mgmt.click_element(By.ID, rate_mgmt.CLASS_ADD_BUTTON)

        logger.info("Шаг 3: Заполнение обязательных полей")
        rate_mgmt.fill_class_required_fields()

        logger.info("Шаг 4: Сохранение класса")
        rate_mgmt.click_element(By.ID, rate_mgmt.RATE_SAVE_BUTTON)
        rate_checks.check_saving_class()

        logger.info("Шаг 5: Удаление класса")
        rate_mgmt.delete_class("NtestN")
        rate_checks.check_deleting_class()

        logger.info("=== Тест успешно завершен ===")

    except Exception as e:
        logger.error(f"ОШИБКА: {str(e)}")
        raise

def test_reservation (driver):

    home_page = HomePage(driver)
    home_checks = HomePageChecks(driver)

    logger.info(f"Запуск цикла бронирования для строки ['row_index = 1']")

    logger.info("Открытие домашней страницы")
    home_page.get_link()

    logger.info(f"Добавление и сохранение строки бронирования ['row_index = 1']")
    home_page.run_custom_reservation(
        row_index= 1,
        arrival_date= date.today().strftime("%d%m%Y"),
        room_count= 1,
        adults= 1,
        children= 1,
        guest_category= "AWD",
        rate= "RACK",
        room_type= "KING",
        payment_info= "VS 1111222233334444 0825",
        guest_name= "THIN/MARIA/MRS",
        country= "USA",
        contact_name= "BORIS",
        booking_source= "K"
    )
    home_checks.check_reservation_status(row_index= 1, expected_status="NEW")
    home_checks.check_saving_reservation()
    home_checks.check_reservation_status(row_index=1, expected_status="SAVED")

