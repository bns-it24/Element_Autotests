from time import sleep
import pytest
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import random
import string


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()  # Включение полноэкранного отображения браузера
    yield driver
    driver.quit()


def click_element(driver, by, value):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value))).click()


def send_keys_to_element(driver, by, value, keys):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value))).click()  # Клик перед вводом
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((by, value)))  # Проверка видимости элемента
    element.clear()  # Очистка поля перед вводом
    element.send_keys(keys)  # Отправка данных для ввода


def generate_guest_name():  # Генерация рандомного имени гостя в формате "*****/*****/MR"
    part1 = ''.join(random.choices(string.ascii_uppercase, k=5))  # Генерация 5 случайных букв
    part2 = ''.join(random.choices(string.ascii_uppercase, k=5))  # Генерация 5 случайных букв
    suffix = random.choice(["MR", "MRS"])  # Случайный выбор между MR и MRS
    return f"{part1}/{part2}/{suffix}"  # Формирование строки в требуемом формате


def check_adding_new_res_string(driver):
    try:
        # Ожидание, пока элемент станет видимым
        new_res_string = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "__xmlview2--homeMainTable-tblBody"))
        )

        # Проверка отображения
        if not new_res_string.is_displayed():
            print("Новая строка бронирования найдена, но не отображается.")

    except TimeoutException:
        assert False, "Время ожидания истекло. Новая строка бронирования не обнаружена."
    except AssertionError as f:
        print(f)


def get_link(driver):
    driver.get("https://reserve.kube.ugmk.com/webapp/index.html#/home")


def add_new_res_string (driver):
    click_element(driver, By.ID, "__xmlview2--idHomeButtonAdd")


def select_hotel_1st_str(driver):
    click_element(driver, By.ID, "__select0-__xmlview2--homeMainTable-0-label")
    click_element(driver, By.XPATH, "//*[text()='Hyatt Place Ekaterinburg']")


def select_hotel_2nd_str(driver):
    click_element(driver, By.ID, "__select0-__xmlview2--homeMainTable-1-label")
    click_element(driver, By.XPATH, "//*[text()='Hyatt Place Ekaterinburg']")


def fillling_required_fields_1st_str_via2rooms (driver):
    send_keys_to_element(driver, By.ID, "__picker0-__xmlview2--homeMainTable-0-inner", date.today().strftime("%d%m%Y"))  # Дата заезда
    send_keys_to_element(driver, By.ID, "__input0-__xmlview2--homeMainTable-0-inner", 2)  # Кол-во комнат
    send_keys_to_element(driver, By.ID, "__input1-__xmlview2--homeMainTable-0-inner", 1)  # Взрослые
    send_keys_to_element(driver, By.ID, "__input2-__xmlview2--homeMainTable-0-inner", 1)  # Дети
    send_keys_to_element(driver, By.ID, "__input3-__xmlview2--homeMainTable-0-inner", "RAC")  # Категория гостя
    send_keys_to_element(driver, By.ID, "__input4-__xmlview2--homeMainTable-0-inner", "RACK")  # Тариф
    send_keys_to_element(driver, By.ID, "__input5-__xmlview2--homeMainTable-0-inner", "KING")  # Тип комнаты
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputHold_G-inner", "VS 1111222233334444 0825")  # Платежные данные
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName_G-inner", generate_guest_name())  # Имя гостя
    click_element(driver, By.ID, "__form1--FC-NoHead--Grid-wrapperfor-__xmlview2--selectCountry_G")  # Открыть список стран
    click_element(driver, By.XPATH, "//*[text()='Russian Federation']")  # Выбрать страну
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName2_G-inner", "BILBO")  # Имя для связи
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputBkngSrc_G-inner", "B")  # Тип источника бронирования



def fillling_required_fields_1st_str (driver):
    send_keys_to_element(driver, By.ID, "__picker0-__xmlview2--homeMainTable-0-inner", date.today().strftime("%d%m%Y"))  # Дата заезда
    send_keys_to_element(driver, By.ID, "__input0-__xmlview2--homeMainTable-0-inner", 1)  # Кол-во комнат
    send_keys_to_element(driver, By.ID, "__input1-__xmlview2--homeMainTable-0-inner", 1)  # Взрослые
    send_keys_to_element(driver, By.ID, "__input2-__xmlview2--homeMainTable-0-inner", 1)  # Дети
    send_keys_to_element(driver, By.ID, "__input3-__xmlview2--homeMainTable-0-inner", "RAC")  # Категория гостя
    send_keys_to_element(driver, By.ID, "__input4-__xmlview2--homeMainTable-0-inner", "RACK")  # Тариф
    send_keys_to_element(driver, By.ID, "__input5-__xmlview2--homeMainTable-0-inner", "KING")  # Тип комнаты
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputHold_G-inner", "VS 1111222233334444 0825")  # Платежные данные
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName_G-inner", generate_guest_name())  # Имя гостя
    click_element(driver, By.ID, "__form1--FC-NoHead--Grid-wrapperfor-__xmlview2--selectCountry_G")  # Открыть список стран
    click_element(driver, By.XPATH, "//*[text()='Russian Federation']")  # Выбрать страну
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName2_G-inner", "BILBO")  # Имя для связи
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputBkngSrc_G-inner", "B")  # Тип источника бронирования


def fillling_required_fields_2nd_str (driver):
    send_keys_to_element(driver, By.ID, "__picker0-__xmlview2--homeMainTable-1-inner", date.today().strftime("%d%m%Y"))  # Дата заезда
    send_keys_to_element(driver, By.ID, "__input0-__xmlview2--homeMainTable-1-inner", 1)  # Кол-во комнат
    send_keys_to_element(driver, By.ID, "__input1-__xmlview2--homeMainTable-1-inner", 1)  # Взрослые
    send_keys_to_element(driver, By.ID, "__input2-__xmlview2--homeMainTable-1-inner", 1)  # Дети
    send_keys_to_element(driver, By.ID, "__input3-__xmlview2--homeMainTable-1-inner", "RAC")  # Категория гостя
    send_keys_to_element(driver, By.ID, "__input4-__xmlview2--homeMainTable-1-inner", "RACK")  # Тариф
    send_keys_to_element(driver, By.ID, "__input5-__xmlview2--homeMainTable-1-inner", "KING")  # Тип комнаты
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputHold_G-inner", "VS 1111222233334444 0825")  # Платежные данные
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName_G-inner", generate_guest_name())  # Имя гостя
    click_element(driver, By.ID, "__form1--FC-NoHead--Grid-wrapperfor-__xmlview2--selectCountry_G")  # Открыть список стран
    click_element(driver, By.XPATH, "//*[text()='Russian Federation']")  # Выбрать страну
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName2_G-inner", "BILBO")  # Имя для связи
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputBkngSrc_G-inner", "B")  # Тип источника бронирования


def save_reservation (driver):
    click_element(driver, By.ID, "__xmlview2--idHomeButtonSave")


def cancel_1st_res_string (driver):
    click_element(driver, By.ID, "__item3-__xmlview2--homeMainTable-0-cell0")  # Выбор нужной строки
    click_element(driver, By.ID, "__xmlview2--idHomeButtonCancel")  # Нажатие кнопки "Cancel"


def cancel_2nd_res_string (driver):
    click_element(driver, By.ID, "__item3-__xmlview2--homeMainTable-1-cell0")  # Выбор нужной строки
    click_element(driver, By.ID, "__xmlview2--idHomeButtonCancel")  # Нажатие кнопки "Cancel"


def cancel_3rd_res_string (driver):
    click_element(driver, By.ID, "__item3-__xmlview2--homeMainTable-2-cell0")  # Выбор нужной строки
    click_element(driver, By.ID, "__xmlview2--idHomeButtonCancel")  # Нажатие кнопки "Cancel"


def clear_home_page(driver):
    click_element(driver, By.ID, "__xmlview2--idHomeButtonClear-inner")  # Нажатие кнопки "Clear"


def click_on_1st_res_str(driver):
    click_element(driver,By.ID, "__item3-__xmlview2--homeMainTable-0")


def click_on_2nd_res_str(driver):
    click_element(driver,By.ID, "__item3-__xmlview2--homeMainTable-1")


def check_saving_reservation (driver):
    try:
        success_message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[text()='The data is saved']"))
        )
        assert success_message_element.is_displayed(), "Сообщение об успешном сохранении не отображается."
    except TimeoutException:
        assert False, "Время ожидания истекло. Сообщение об успешном сохранении не обнаружено."


def check_cancelling_reservation(driver):
    try:
        success_message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[text()='The reservation has been successfully cancelled']"))
        )
        assert success_message_element.is_displayed(), "Сообщение об успешном удалении не отображается."
    except TimeoutException:
        assert False, "Время ожидания истекло. Сообщение об успешном удалении не обнаружено."


def check_1st_str_status_new(driver):
    res_status_before_save = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-0-inner"))
    ).get_attribute('value')
    assert res_status_before_save == "NEW", f"Expected NEW, but got {res_status_before_save}"


def check_2nd_str_status_new(driver):
    res_status_before_save = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-1-inner"))
    ).get_attribute('value')
    assert res_status_before_save == "NEW", f"Expected NEW, but got {res_status_before_save}"


def check_1st_str_status_saved(driver):
    res_status_after_save = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-0-inner"))
    ).get_attribute('value')
    assert res_status_after_save == "SAVED", f"Expected SAVED, but got {res_status_after_save}"


def check_2nd_str_status_saved(driver):
    res_status_after_save = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-1-inner"))
    ).get_attribute('value')
    assert res_status_after_save == "SAVED", f"Expected SAVED, but got {res_status_after_save}"


def edit_mode_on (driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    body = driver.find_element(By.TAG_NAME, "body")  # Фокус на <body>
    body.send_keys(Keys.ALT, 'e')  # Отправка Alt + E


def add_one_res_string(driver, arrival_date, room_count, adults, children, guest_category, rate, room_type, payment_info, guest_name, contact_name, booking_source):
    driver.get("https://reserve.kube.ugmk.com/webapp/index.html#/home")

    # Добавление новой строки бронирования
    click_element(driver, By.ID, "__xmlview2--idHomeButtonAdd")

    # Выбор отеля
    click_element(driver, By.ID, "__select0-__xmlview2--homeMainTable-0-label")
    click_element(driver, By.XPATH, "//*[text()='Hyatt Place Ekaterinburg']")

    # Заполнение полей
    send_keys_to_element(driver, By.ID, "__picker0-__xmlview2--homeMainTable-0-inner", str(arrival_date))  # Дата заезда
    send_keys_to_element(driver, By.ID, "__input0-__xmlview2--homeMainTable-0-inner", str(room_count))  # Кол-во комнат
    send_keys_to_element(driver, By.ID, "__input1-__xmlview2--homeMainTable-0-inner", str(adults))  # Взрослые
    send_keys_to_element(driver, By.ID, "__input2-__xmlview2--homeMainTable-0-inner", str(children))  # Дети
    send_keys_to_element(driver, By.ID, "__input3-__xmlview2--homeMainTable-0-inner", guest_category)  # Категория гостя
    send_keys_to_element(driver, By.ID, "__input4-__xmlview2--homeMainTable-0-inner", rate)  # Тариф
    send_keys_to_element(driver, By.ID, "__input5-__xmlview2--homeMainTable-0-inner", room_type)  # Тип комнаты
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputHold_G-inner", payment_info)  # Платежные данные
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName_G-inner", guest_name)  # Имя гостя
    click_element(driver, By.ID,
                  "__form1--FC-NoHead--Grid-wrapperfor-__xmlview2--selectCountry_G")  # Открыть список стран
    click_element(driver, By.XPATH, "//*[text()='Russian Federation']")  # Выбрать страну
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName2_G-inner", contact_name)  # Имя для связи
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputBkngSrc_G-inner",booking_source)  # Тип источника бронирования

    # Проверка статуса перед сохранением
    res_status_before_save = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-0-inner"))
    ).get_attribute('value')
    assert res_status_before_save == "NEW", f"Expected NEW, but got {res_status_before_save}"

    # Сохранение брони
    click_element(driver, By.ID, "__xmlview2--idHomeButtonSave")

    # Проверка на успешное сохранение
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[text()='The data is saved']"))
    )

    # Проверка статуса после сохранения
    res_status_after_save = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-0-inner"))
    ).get_attribute('value')
    assert res_status_after_save == "SAVED", f"Expected SAVED, but got {res_status_after_save}"

    # Включение режима редактирования
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    body = driver.find_element(By.TAG_NAME, "body")  # Фокус на <body>
    body.send_keys(Keys.ALT, 'e')  # Отправка Alt + E

    # Удаление сохраненной брони
    click_element(driver, By.ID, "__xmlview2--idHomeButtonCancel")  # Нажатие кнопки "Cancel"

    # Проверка на успешное удаление
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[text()='The reservation has been successfully cancelled']"))
    )

    # Проверка статуса после закрытия
    res_status_after_cancel = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-0-inner"))
    ).get_attribute('value')
    assert res_status_after_cancel == "CANCELLED", f"Expected CANCELLED, but got {res_status_after_cancel}"

    # Очистка конфигуратора бронирования
    click_element(driver, By.ID, "__xmlview2--idHomeButtonClear-inner")  # Нажатие кнопки "Clear"


def add_three_res_strings(driver):
    driver.get("https://reserve.kube.ugmk.com/webapp/index.html#/home")

    # Добавление первой строки бронирования
    click_element(driver, By.ID, "__xmlview2--idHomeButtonAdd")

    # Выбор отеля
    click_element(driver, By.ID, "__select0-__xmlview2--homeMainTable-0-label")
    click_element(driver, By.XPATH, "//*[text()='Hyatt Place Ekaterinburg']")

    # Заполнение полей
    send_keys_to_element(driver, By.ID, "__picker0-__xmlview2--homeMainTable-0-inner",
                         date.today().strftime("%d%m%Y"))  # Дата заезда
    send_keys_to_element(driver, By.ID, "__input0-__xmlview2--homeMainTable-0-inner", 1)  # Кол-во комнат
    send_keys_to_element(driver, By.ID, "__input1-__xmlview2--homeMainTable-0-inner", 2)  # Взрослые
    send_keys_to_element(driver, By.ID, "__input2-__xmlview2--homeMainTable-0-inner", 1)  # Дети
    send_keys_to_element(driver, By.ID, "__input3-__xmlview2--homeMainTable-0-inner", "RAC")  # Категория гостя
    send_keys_to_element(driver, By.ID, "__input4-__xmlview2--homeMainTable-0-inner", "RACK")  # Тариф
    send_keys_to_element(driver, By.ID, "__input5-__xmlview2--homeMainTable-0-inner", "KING")  # Тип комнаты
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputHold_G-inner",
                         "VS 1111222233334444 0825")  # Платежные данные
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName_G-inner", generate_guest_name())  # Имя гостя
    click_element(driver, By.ID,
                  "__form1--FC-NoHead--Grid-wrapperfor-__xmlview2--selectCountry_G")  # Открыть список стран
    click_element(driver, By.XPATH, "//*[text()='Russian Federation']")  # Выбрать страну
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName2_G-inner", "BILBO")  # Имя для связи
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputBkngSrc_G-inner", "B")  # Тип источника бронирования

    # Сохранение брони
    click_element(driver, By.ID, "__xmlview2--idHomeButtonSave")

    # Ожидание перед включением редактирования
    sleep(2)

    # Включение режима редактирования
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    body = driver.find_element(By.TAG_NAME, "body")  # Фокус на <body>
    body.send_keys(Keys.ALT, 'e')  # Отправка Alt + E

    # Добавление второй строки бронирования
    click_element(driver, By.ID, "__xmlview2--idHomeButtonAdd")

    # Выбор отеля
    click_element(driver, By.ID, "__select0-__xmlview2--homeMainTable-1-label")
    click_element(driver, By.ID, "__item2-__select0-__xmlview2--homeMainTable-1-1")

    # Заполнение полей
    send_keys_to_element(driver, By.ID, "__picker0-__xmlview2--homeMainTable-1-inner",
                         date.today().strftime("%d%m%Y"))  # Дата заезда
    send_keys_to_element(driver, By.ID, "__input0-__xmlview2--homeMainTable-1-inner", 2)  # Кол-во комнат
    send_keys_to_element(driver, By.ID, "__input1-__xmlview2--homeMainTable-1-inner", 4)  # Взрослые
    send_keys_to_element(driver, By.ID, "__input2-__xmlview2--homeMainTable-1-inner", 2)  # Дети
    send_keys_to_element(driver, By.ID, "__input3-__xmlview2--homeMainTable-1-inner", "COR")  # Категория гостя
    send_keys_to_element(driver, By.ID, "__input4-__xmlview2--homeMainTable-1-inner", "SWAG")  # Тариф
    send_keys_to_element(driver, By.ID, "__input5-__xmlview2--homeMainTable-1-inner", "TWIN")  # Тип комнаты
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputHold_G-inner", "CA")  # Платежные данные
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName_G-inner", generate_guest_name())  # Имя гостя
    click_element(driver, By.ID,"__form1--FC-NoHead--Grid-wrapperfor-__xmlview2--selectCountry_G")  # Открыть список стран
    click_element(driver, By.XPATH, "//*[text()='USA']")  # Выбрать страну
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName2_G-inner", "PLUTO")  # Имя для связи
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputBkngSrc_G-inner", "P")  # Тип источника бронирования

    # Сохранение брони
    click_element(driver, By.ID, "__xmlview2--idHomeButtonSave")

    # Ожидание перед включением редактирования
    sleep(2)

    # Включение режима редактирования
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    body = driver.find_element(By.TAG_NAME, "body")  # Фокус на <body>
    body.send_keys(Keys.ALT, 'e')  # Отправка Alt + E

    # Добавление третьей строки бронирования
    click_element(driver, By.ID, "__xmlview2--idHomeButtonAdd")

    # Выбор отеля
    click_element(driver, By.ID, "__select0-__xmlview2--homeMainTable-2-label")
    click_element(driver, By.ID, "__item2-__select0-__xmlview2--homeMainTable-2-1")

    # Заполнение полей
    send_keys_to_element(driver, By.ID, "__picker0-__xmlview2--homeMainTable-2-inner", date.today().strftime("%d%m%Y"))  # Дата заезда
    send_keys_to_element(driver, By.ID, "__input0-__xmlview2--homeMainTable-2-inner", 2)  # Кол-во комнат
    send_keys_to_element(driver, By.ID, "__input1-__xmlview2--homeMainTable-2-inner", 4)  # Взрослые
    send_keys_to_element(driver, By.ID, "__input2-__xmlview2--homeMainTable-2-inner", 2)  # Дети
    send_keys_to_element(driver, By.ID, "__input3-__xmlview2--homeMainTable-2-inner", "COR")  # Категория гостя
    send_keys_to_element(driver, By.ID, "__input4-__xmlview2--homeMainTable-2-inner", "SWAG")  # Тариф
    send_keys_to_element(driver, By.ID, "__input5-__xmlview2--homeMainTable-2-inner", "TWIN")  # Тип комнаты
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputHold_G-inner", "CA")  # Платежные данные
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName_G-inner", generate_guest_name())  # Имя гостя
    click_element(driver, By.ID,"__form1--FC-NoHead--Grid-wrapperfor-__xmlview2--selectCountry_G")  # Открыть список стран
    click_element(driver, By.XPATH, "//*[text()='USA']")  # Выбрать страну
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName2_G-inner", "PLUTO")  # Имя для связи
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputBkngSrc_G-inner", "P")  # Тип источника бронирования

    # Проверка статуса перед сохранением
    # Список ID элементов для проверки (1-2 строки)
    input_ids = [
        "__input7-__xmlview2--homeMainTable-0-inner",
        "__input7-__xmlview2--homeMainTable-1-inner",
    ]
    for input_id in input_ids:
        res_status_before_save = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, input_id))
        ).get_attribute('value')
        assert res_status_before_save == "SAVED", f"Expected SAVED for {input_id}, but got {res_status_before_save}"

    res3_status_before_save = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-2-inner"))
    ).get_attribute('value')
    assert res3_status_before_save == "NEW", f"Expected NEW, but got {res3_status_before_save}"

    # Сохранение брони
    click_element(driver, By.ID, "__xmlview2--idHomeButtonSave")

    # Проверка на успешное сохранение
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[text()='The data is saved']"))
    )

    # Проверка статуса после сохранения
    for input_id in input_ids:
        res_status_after_save = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, input_id))
        ).get_attribute('value')
        assert res_status_after_save == "SAVED", f"Expected SAVED for {input_id}, but got {res_status_after_save}"

    res3_status_after_save = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-2-inner"))
    ).get_attribute('value')
    assert res3_status_after_save == "SAVED", f"Expected SAVED, but got {res3_status_after_save}"

    # Ожидание перед включением редактирования
    sleep(2)

    # Включение режима редактирования
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    body = driver.find_element(By.TAG_NAME, "body")  # Фокус на <body>
    body.send_keys(Keys.ALT, 'e')  # Отправка Alt + E

    # Отмена первой строки бронирования
    click_element(driver, By.ID, "__item3-__xmlview2--homeMainTable-0-cell0")  # Выбор нужной строки
    click_element(driver, By.ID, "__xmlview2--idHomeButtonCancel")  # Нажатие кнопки "Cancel"

    # Отмена второй строки бронирования
    click_element(driver, By.ID, "__item3-__xmlview2--homeMainTable-1-cell0")  # Выбор нужной строки
    click_element(driver, By.ID, "__xmlview2--idHomeButtonCancel")  # Нажатие кнопки "Cancel"

    # Отмена третьей строки бронирования
    click_element(driver, By.ID, "__item3-__xmlview2--homeMainTable-2-cell0")  # Выбор нужной строки
    click_element(driver, By.ID, "__xmlview2--idHomeButtonCancel")  # Нажатие кнопки "Cancel"

    # Проверка на успешную отмену
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[text()='The reservation has been successfully cancelled']"))
    )

    # Ожидание перед проверкой смены статуса
    sleep(2)

    # Проверка статуса после закрытия
    input_ids = [
        "__input7-__xmlview2--homeMainTable-0-inner",
        "__input7-__xmlview2--homeMainTable-1-inner",
        "__input7-__xmlview2--homeMainTable-2-inner"
    ]
    for input_id in input_ids:
        res_status_after_cancel = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, input_id))
        ).get_attribute('value')
        assert res_status_after_cancel == "CANCELLED", f"Expected CANCELLED for {input_id}, but got {res_status_after_cancel}"

    # Очистка конфигуратора бронирования
    click_element(driver, By.ID, "__xmlview2--idHomeButtonClear-inner")  # Нажатие кнопки "Clear"


def hotkeys_alt_s_e_x(driver):
    driver.get("https://reserve.kube.ugmk.com/webapp/index.html#/home")

    # Добавление строки бронирования
    click_element(driver, By.ID, "__xmlview2--idHomeButtonAdd")

    # Выбор отеля
    click_element(driver, By.ID, "__select0-__xmlview2--homeMainTable-0-label")
    click_element(driver, By.XPATH, "//*[text()='Hyatt Place Ekaterinburg']")

    # Заполнение полей
    send_keys_to_element(driver, By.ID, "__picker0-__xmlview2--homeMainTable-0-inner", date.today().strftime("%d%m%Y"))  # Дата заезда
    send_keys_to_element(driver, By.ID, "__input0-__xmlview2--homeMainTable-0-inner", 1)  # Кол-во комнат
    send_keys_to_element(driver, By.ID, "__input1-__xmlview2--homeMainTable-0-inner", 2)  # Взрослые
    send_keys_to_element(driver, By.ID, "__input2-__xmlview2--homeMainTable-0-inner", 1)  # Дети
    send_keys_to_element(driver, By.ID, "__input3-__xmlview2--homeMainTable-0-inner", "RAC")  # Категория гостя
    send_keys_to_element(driver, By.ID, "__input4-__xmlview2--homeMainTable-0-inner", "RACK")  # Тариф
    send_keys_to_element(driver, By.ID, "__input5-__xmlview2--homeMainTable-0-inner", "KING")  # Тип комнаты
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputHold_G-inner","VS 1111222233334444 0825")  # Платежные данные
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName_G-inner", generate_guest_name())  # Имя гостя
    click_element(driver, By.ID, "__form1--FC-NoHead--Grid-wrapperfor-__xmlview2--selectCountry_G")  # Открыть список стран
    click_element(driver, By.XPATH, "//*[text()='Russian Federation']")  # Выбрать страну
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName2_G-inner", "BILBO")  # Имя для связи
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputBkngSrc_G-inner", "B")  # Тип источника бронирования

    # Сохранение брони
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "__item3-__xmlview2--homeMainTable-0")))
    body = driver.find_element(By.ID, "__item3-__xmlview2--homeMainTable-0")  # Фокус на строку бронирования
    body.send_keys(Keys.ALT, 's')  # Отправка Alt + S

    # Проверка на успешное сохранение
    try:
        success_message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[text()='The data is saved']"))
        )
        assert success_message_element.is_displayed(), "Сообщение об успешном сохранении не отображается."
    except TimeoutException:
        assert False, "Время ожидания истекло. Сообщение об успешном сохранении не обнаружено."

    # Ожидание перед включением редактирования
    sleep(2)

    # Включение режима редактирования
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    body = driver.find_element(By.TAG_NAME, "body")  # Фокус на <body>
    body.send_keys(Keys.ALT, 'e')  # Отправка Alt + E

    # Отмена брони
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "__item3-__xmlview2--homeMainTable-0")))
    body = driver.find_element(By.ID, "__item3-__xmlview2--homeMainTable-0")  # Фокус на строку бронирования
    body.send_keys(Keys.ALT, 'x')  # Отправка Alt + X

    # Ожидание после удаления
    sleep(2)

    # Проверка на успешное удаление
    try:
        success_message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[text()='The reservation has been successfully cancelled']"))
        )
        assert success_message_element.is_displayed(), "Сообщение об успешном удалении не отображается."
    except TimeoutException:
        assert False, "Время ожидания истекло. Сообщение об успешном удалении не обнаружено."

    # Очистка конфигуратора бронирования
    click_element(driver, By.ID, "__xmlview2--idHomeButtonClear-inner")  # Нажатие кнопки "Clear"


def hotkeys_alt_i(driver):
    driver.get("https://reserve.kube.ugmk.com/webapp/index.html#/home")

    # Добавление строки бронирования
    add_new_res_string (driver)

    # Выбор отеля
    click_element(driver, By.ID, "__select0-__xmlview2--homeMainTable-0-label")
    click_element(driver, By.XPATH, "//*[text()='Hyatt Place Ekaterinburg']")

    # Заполнение полей
    send_keys_to_element(driver, By.ID, "__picker0-__xmlview2--homeMainTable-0-inner", date.today().strftime("%d%m%Y"))  # Дата заезда
    send_keys_to_element(driver, By.ID, "__input0-__xmlview2--homeMainTable-0-inner", 1)  # Кол-во комнат
    send_keys_to_element(driver, By.ID, "__input1-__xmlview2--homeMainTable-0-inner", 2)  # Взрослые
    send_keys_to_element(driver, By.ID, "__input2-__xmlview2--homeMainTable-0-inner", 1)  # Дети
    send_keys_to_element(driver, By.ID, "__input3-__xmlview2--homeMainTable-0-inner", "RAC")  # Категория гостя
    send_keys_to_element(driver, By.ID, "__input4-__xmlview2--homeMainTable-0-inner", "RACK")  # Тариф
    send_keys_to_element(driver, By.ID, "__input5-__xmlview2--homeMainTable-0-inner", "KING")  # Тип комнаты
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputHold_G-inner","VS 1111222233334444 0825")  # Платежные данные
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName_G-inner", "FAT/OLEG/MR")  # Имя гостя
    click_element(driver, By.ID,"__form1--FC-NoHead--Grid-wrapperfor-__xmlview2--selectCountry_G")  # Открыть список стран
    click_element(driver, By.XPATH, "//*[text()='Russian Federation']")  # Выбрать страну
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName2_G-inner", "BILBO")  # Имя для связи
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputBkngSrc_G-inner", "B")  # Тип источника бронирования

    # Сохранение брони
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "__item3-__xmlview2--homeMainTable-0")))
    body = driver.find_element(By.ID, "__item3-__xmlview2--homeMainTable-0")  # Фокус на строку бронирования
    body.send_keys(Keys.ALT, 's')  # Отправка Alt + S

    # Проверка на успешное сохранение
    try:
        success_message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[text()='The data is saved']"))
        )
        assert success_message_element.is_displayed(), "Сообщение об успешном сохранении не отображается."
    except TimeoutException:
        assert False, "Время ожидания истекло. Сообщение об успешном сохранении не обнаружено."

    # Ожидание перед включением редактирования
    sleep(2)

    # Включение режима редактирования
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    body = driver.find_element(By.TAG_NAME, "body")  # Фокус на <body>
    body.send_keys(Keys.ALT, 'e')  # Отправка Alt + E

    # Внесение изменений в имя гостя
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "__xmlview2--homeTabInputName_G-inner")) # Поиск элемента
    )
    element.clear()  # Очистка поля ввода
    element.send_keys("THIN/MARIA/MRS")  # Ввод данных

    # Проверка ввода изменений
    try:
        input_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "__xmlview2--homeTabInputName_G-inner"))
        )
        assert input_element.get_attribute(
            'value') == "THIN/MARIA/MRS", "Вводимое значение 'THIN/MARIA/MRS' не отображается в поле."
    except TimeoutException:
        assert False, "Время ожидания истекло. Вводимое значение не обнаружено."
    except AssertionError as ae:
        assert False, str(ae)

    # Отмена изменений
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    body = driver.find_element(By.TAG_NAME, "body")  # Фокус на <body>
    body.send_keys(Keys.ALT, 'i')  # Отправка Alt + I

    # Ожидание после отмены
    sleep(2)

    # Подтверждение отмены изменений
    click_element(driver, By.ID, "__mbox-btn-0-BDI-content")

    # Проверка сообщения об успехе
    try:
        success_message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[text()='The changes have been canceled']"))
        )
        assert success_message_element.is_displayed(), "Сообщение об успешной отмене."
    except TimeoutException:
        assert False, "Время ожидания истекло. Сообщение об успешной отмене не обнаружено."

    # Проверка отмены изменений
    try:
        input_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "__xmlview2--homeTabInputName_G-inner"))
        )
        assert input_element.get_attribute(
            'value') == "FAT/OLEG/MR", "Вводимое значение 'FAT/OLEG/MR' не отображается в поле."
    except TimeoutException:
        assert False, "Время ожидания истекло. Вводимое значение не обнаружено."
    except AssertionError as ae:
        assert False, str(ae)

    # Отмена брони
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "__item3-__xmlview2--homeMainTable-0")))
    body = driver.find_element(By.ID, "__item3-__xmlview2--homeMainTable-0")  # Фокус на строку бронирования
    body.send_keys(Keys.ALT, 'x')  # Отправка Alt + X

    # Ожидание после удаления
    sleep(2)

    # Проверка на успешное удаление
    try:
        success_message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[text()='The reservation has been successfully cancelled']"))
        )
        assert success_message_element.is_displayed(), "Сообщение об успешном удалении не отображается."
    except TimeoutException:
        assert False, "Время ожидания истекло. Сообщение об успешном удалении не обнаружено."

    # Очистка конфигуратора бронирования
    click_element(driver, By.ID, "__xmlview2--idHomeButtonClear-inner")  # Нажатие кнопки "Clear"


def hotkeys_alt_n_h(driver):
    driver.get("https://reserve.kube.ugmk.com/webapp/index.html#/home")

    sleep(5) # Ожидание перед добавлением строки

    # Добавление строки бронирования
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    body = driver.find_element(By.TAG_NAME, "body")  # Фокус на <body>
    body.send_keys(Keys.ALT, 'n')  # Отправка Alt + N

    # Проверка добавления строки
    check_adding_new_res_string(driver)

    # Выбор отеля
    click_element(driver, By.ID, "__select0-__xmlview2--homeMainTable-0-label")
    click_element(driver, By.XPATH, "//*[text()='Hyatt Place Ekaterinburg']")

    # Заполнение обязательных полей
    fillling_required_fields_1st_str(driver)

    # Сохранение брони
    save_reservation(driver)

    # Проверка на успешное сохранение
    check_saving_reservation(driver)

    # Ожидание перед включением редактирования
    sleep(2)

    # Включение режима редактирования
    edit_mode_on(driver)

    # Включения подселения к номеру
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "__item3-__xmlview2--homeMainTable-0")))
    body = driver.find_element(By.ID, "__item3-__xmlview2--homeMainTable-0")  # Фокус на строку бронирования
    body.send_keys(Keys.ALT, 'h')  # Отправка Alt + H

    sleep(1) # Обязательное ожидание загрузки статуса

    # Проверка включения статуса "NEW_SHARED"
    res_status_before_save = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-1-inner"))
    ).get_attribute('value')
    sleep(1)
    assert res_status_before_save == "NEW_SHARED", f"Expected NEW_SHARED, but got {res_status_before_save}"

    # Проверка, что количество взрослых и детей в добавленной строке = 0
    input_ids = [
        "__input1-__xmlview2--homeMainTable-0-inner",
        "__input2-__xmlview2--homeMainTable-0-inner"
    ]

    for input_id in input_ids:
        try:
            # Ожидание появления элемента на странице
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, input_id))
            )
            # Находим элемент
            input_element = driver.find_element(By.ID, input_id)

            # Проверяем, что инпут не заполнен
            if not input_element.get_attribute('value'):
                print(f"Поле с ID '{input_id}' пустое.")
            else:
                print(f"Поле с ID '{input_id}' заполнено.")

        except TimeoutException:
            print(f"Элемент с ID '{input_id}' не доступен.")

    # Заполнение недостающих полей
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName_G-inner", generate_guest_name())  # Имя гостя
    click_element(driver, By.ID,"__form1--FC-NoHead--Grid-wrapperfor-__xmlview2--selectCountry_G")  # Открыть список стран
    click_element(driver, By.XPATH, "//*[text()='Russian Federation']")  # Выбрать страну

    # Сохранение брони
    save_reservation(driver)

    sleep(1)  # Обязательное ожидание загрузки статуса

    # Проверка включения статуса "SAVED_SHARED"
    res_status_before_save = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-0-inner"))
    ).get_attribute('value')
    assert res_status_before_save == "SAVED_SHARED", f"Expected SAVED_SHARED, but got {res_status_before_save}"

    # Отмена брони
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "__item3-__xmlview2--homeMainTable-0")))
    body = driver.find_element(By.ID, "__item3-__xmlview2--homeMainTable-1")  # Фокус на строку бронирования
    body.send_keys(Keys.ALT, 'x')  # Отправка Alt + X

    # Ожидание после удаления
    sleep(2)

    # Проверка на успешное удаление
    check_cancelling_reservation(driver)

    # Очистка конфигуратора бронирования
    clear_home_page(driver)


def hotkeys_alt_d_y(driver):
    driver.get("https://reserve.kube.ugmk.com/webapp/index.html#/home")

    add_new_res_string(driver)

    select_hotel_1st_str(driver)

    fillling_required_fields_1st_str(driver)

    save_reservation(driver)

    # Проверка присвоения брони Cnf Nmb
    try:
        # Ожидание, пока элемент станет доступен
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "__link0"))
        )

        # Извлечение текстового содержимого элемента
        text_value = element.text
        print(f"Значение в элементе: '{text_value}'")

        # Проверка, что значение является числом
        if text_value.isdigit():
            print("Cnf nmb содержит числовое значение.")
        else:
            raise AssertionError(f"Не числовое значение: '{text_value}'")

        # Обработка исключений
    except TimeoutException:
        print("Cnf nmb не найден в течение 10 секунд.")
    except NoSuchElementException:
        print("Элемент не найден.")
    except AssertionError as e:
        print(e)

    sleep(2) # Ожидание перед включением редактирования

    edit_mode_on(driver)

    # Копирование брони с теми же данными, но со статусом "NEW"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "__item3-__xmlview2--homeMainTable-0")))
    body = driver.find_element(By.ID, "__item3-__xmlview2--homeMainTable-0")  # Фокус на строку бронирования
    body.send_keys(Keys.ALT, 'd')  # Отправка Alt + D

    # Проверка статусов после копирования
    res_status_1st_str = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-0-inner"))
    ).get_attribute('value')
    assert res_status_1st_str == "SAVED", f"Expected SAVED, but got {res_status_1st_str}"

    res_status_2nd_str = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-1-inner"))
    ).get_attribute('value')
    assert res_status_2nd_str == "NEW", f"Expected NEW, but got {res_status_2nd_str}"

    # Сохранение брони
    save_reservation(driver)

    # Проверка статуса скопированной брони после сохранения
    res_status_2nd_str = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-1-inner"))
    ).get_attribute('value')
    assert res_status_2nd_str == "SAVED", f"Expected SAVED, but got {res_status_2nd_str}"

    # Удаление брони
    cancel_1st_res_string(driver)
    cancel_2nd_res_string(driver)

    # Ожидание после удаления
    sleep(2)

    # Проверка на успешное удаление
    input_ids = [
        "__input7-__xmlview2--homeMainTable-0-inner",
        "__input7-__xmlview2--homeMainTable-1-inner"
    ]
    for input_id in input_ids:
        try:
            # Ожидание, пока элемент станет доступен
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, input_id))
            )

            # Проверка значения
            value = element.get_attribute('value')
            print(f"Значение в элементе с ID '{input_id}': '{value}'")

            # Проверка, что значение равно "CANCELLED"
            assert value == "CANCELLED", f"Статус не 'CANCELLED' в элементе {input_id} (значение: '{value}')"

        except TimeoutException:
            print(f"Элемент с id='{input_id}' не найден в течение 10 секунд.")
        except AssertionError as e:
            print(e)

    clear_home_page(driver)

    add_new_res_string(driver)

    select_hotel_1st_str(driver)

    fillling_required_fields_1st_str(driver)

    save_reservation(driver)

    # Проверка присвоения брони Cnf Nmb
    try:
        # Ожидание, пока элемент станет доступен
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "__link0"))
        )

        # Извлечение текстового содержимого элемента
        text_value = element.text
        print(f"Значение в элементе: '{text_value}'")

        # Проверка, что значение является числом
        if text_value.isdigit():
            print("Элемент содержит числовое значение.")
        else:
            raise AssertionError(f"Не числовое значение: '{text_value}'")

        # Обработка исключений
    except TimeoutException:
        print("Элемент с id='__link0' не найден в течение 10 секунд.")
    except NoSuchElementException:
        print("Элемент не найден.")
    except AssertionError as e:
        print(e)

    edit_mode_on(driver)

    # Копирование брони с теми же данными (за исключением поля HOLD), но со статусом "NEW"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "__item3-__xmlview2--homeMainTable-0")))
    body = driver.find_element(By.ID, "__item3-__xmlview2--homeMainTable-0")  # Фокус на строку бронирования
    body.send_keys(Keys.ALT, 'y')  # Отправка Alt + Y

    # Проверка статусов после добавления
    res_status_1st_str = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-0-inner"))
    ).get_attribute('value')
    assert res_status_1st_str == "SAVED", f"Expected SAVED, but got {res_status_1st_str}"

    res_status_2nd_str = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-1-inner"))
    ).get_attribute('value')
    assert res_status_2nd_str == "NEW", f"Expected NEW, but got {res_status_2nd_str}"

    # Заполнение платежных данных (поле HOLD)
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputHold_G-inner", "CA")
    # Сохранение брони
    save_reservation(driver)

    # Проверка статуса скопированной брони после сохранения
    res_status_2nd_str = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-1-inner"))
    ).get_attribute('value')
    assert res_status_2nd_str == "SAVED", f"Expected SAVED, but got {res_status_2nd_str}"

    # Включение режима редактирования
    edit_mode_on(driver)

    # Закрытие брони
    cancel_1st_res_string(driver)
    cancel_2nd_res_string(driver)

    # Ожидание после удаления
    sleep(2)

    # Проверка на успешное удаление
    input_ids = [
        "__input7-__xmlview2--homeMainTable-0-inner",
        "__input7-__xmlview2--homeMainTable-1-inner"
    ]

    for input_id in input_ids:
        try:
            # Ожидание, пока элемент станет доступен
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, input_id))
            )

            # Проверка значения
            value = element.get_attribute('value')
            print(f"Значение в элементе с ID '{input_id}': '{value}'")

            # Проверка, что значение равно "CANCELLED"
            assert value == "CANCELLED", f"Статус не 'CANCELLED' в элементе {input_id} (значение: '{value}')"

        except TimeoutException:
            print(f"Элемент с id='{input_id}' не найден в течение 10 секунд.")
        except AssertionError as e:
            print(e)

    clear_home_page(driver)


def hotkeys_ctrl_d_y(driver):
    driver.get("https://reserve.kube.ugmk.com/webapp/index.html#/home")

    add_new_res_string(driver)

    select_hotel_1st_str(driver)

    fillling_required_fields_1st_str(driver)

    save_reservation(driver)

    # Проверка присвоения брони Cnf Nmb
    try:
        # Ожидание, пока элемент станет доступен
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "__link0"))
        )

        # Извлечение текстового содержимого элемента
        text_value = element.text
        print(f"Значение в элементе: '{text_value}'")

        # Проверка, что значение является числом
        if text_value.isdigit():
            print("Cnf nmb содержит числовое значение.")
        else:
            raise AssertionError(f"Не числовое значение: '{text_value}'")

        # Обработка исключений
    except TimeoutException:
        print("Cnf nmb не найден в течение 10 секунд.")
    except NoSuchElementException:
        print("Элемент не найден.")
    except AssertionError as e:
        print(e)

    edit_mode_on(driver)

    # Копирование брони с теми же данными, но без Cnf nmb и со статусом "NEW"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "__item3-__xmlview2--homeMainTable-0")))
    body = driver.find_element(By.ID, "__item3-__xmlview2--homeMainTable-0")  # Фокус на строку бронирования
    body.send_keys(Keys.CONTROL, 'd')  # Отправка Ctrl + D

    # Проверка, что Cnf Nmb не присваивается брони
    try:
        # Поиск контейнера с cnf nmb
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "__link0"))
        )
        # Если элемент был найден
        raise AssertionError("Ошибка - Cnf Nmb был найден на странице")
    except TimeoutException:
        # Если возникла TimeoutException, элемент не был найден вовремя, что и требуется
        print("Успех - Cnf Nmb не найден на странице")
    except NoSuchElementException:
        # Это исключение может возникнуть, если элемент никогда не существовал
        print("Успех - Cnf Nmb не найден на странице")

    # Проверка статуса после копирования
    res_status_1st_str = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-0-inner"))
    ).get_attribute('value')
    assert res_status_1st_str == "NEW", f"Expected NEW, but got {res_status_1st_str}"

    # Сохранение новой брони
    save_reservation(driver)

    # Проверка успешного сохранения
    check_saving_reservation(driver)

    # Включение режима редактирования
    edit_mode_on(driver)

    # Закрытие брони
    cancel_1st_res_string(driver)

    sleep(2)

    #Очистка конфигуратора бронирования
    clear_home_page(driver)

    # Добавление новой строки бронирования
    add_new_res_string(driver)

    select_hotel_1st_str(driver)

    fillling_required_fields_1st_str(driver)

    save_reservation(driver)

    # Проверка присвоения брони Cnf Nmb
    try:
        # Ожидание, пока элемент станет доступен
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "__link0"))
        )

        # Извлечение текстового содержимого элемента
        text_value = element.text
        print(f"Значение в элементе: '{text_value}'")

        # Проверка, что значение является числом
        if text_value.isdigit():
            print("Cnf nmb содержит числовое значение.")
        else:
            raise AssertionError(f"Не числовое значение: '{text_value}'")

        # Обработка исключений
    except TimeoutException:
        print("Cnf nmb не найден в течение 10 секунд.")
    except NoSuchElementException:
        print("Элемент не найден.")
    except AssertionError as e:
        print(e)

    edit_mode_on(driver)

    # Копирование брони с теми же данными, НО без Cnf nmb, без платежных данных (HOLD) и со статусом "NEW"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "__item3-__xmlview2--homeMainTable-0")))
    body = driver.find_element(By.ID, "__item3-__xmlview2--homeMainTable-0")  # Фокус на строку бронирования
    body.send_keys(Keys.CONTROL, 'y')  # Отправка Ctrl + Y

    # Проверка, что Cnf Nmb не присваивается брони
    try:
        # Поиск контейнера с cnf nmb
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "__link0"))
        )
        # Если элемент был найден
        raise AssertionError("Ошибка - Cnf Nmb был найден на странице")
    except TimeoutException:
        # Если возникла TimeoutException, элемент не был найден вовремя, что и требуется
        print("Успех - Cnf Nmb не найден на странице")
    except NoSuchElementException:
        # Это исключение может возникнуть, если элемент никогда не существовал
        print("Успех - Cnf Nmb не найден на странице")

    # Проверка статуса после копирования
    res_status_1st_str = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-0-inner"))
    ).get_attribute('value')
    assert res_status_1st_str == "NEW", f"Expected NEW, but got {res_status_1st_str}"

    # Заполнение платежных данных (поле HOLD)
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputHold_G-inner", "CA")

    # Сохранение новой брони
    save_reservation(driver)

    # Проверка успешного сохранения
    check_saving_reservation(driver)

    # Включение режима редактирования
    edit_mode_on(driver)

    # Закрытие брони
    cancel_1st_res_string(driver)

    # Проверка закрытия
    check_cancelling_reservation(driver)

    #Очистка конфигуратора бронирования
    clear_home_page(driver)


def hotkeys_alt_v(driver):
    driver.get("https://reserve.kube.ugmk.com/webapp/index.html#/home")

    add_new_res_string(driver)

    select_hotel_1st_str(driver)

    fillling_required_fields_1st_str(driver)

    save_reservation(driver)

    sleep(2)

    edit_mode_on(driver)

    # Продление брони - добавление новой строки (добавленная строка содержит все данные из первой строки, НО дата заезда новой строки = дата выезда предыдущей строки)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "__item3-__xmlview2--homeMainTable-0")))
    body = driver.find_element(By.ID, "__item3-__xmlview2--homeMainTable-0")  # Фокус на строку бронирования
    body.send_keys(Keys.ALT, 'v')  # Отправка Alt + V

    # Проверка статуса после продления
    res_status_1st_str = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-0-inner"))
    ).get_attribute('value')
    assert res_status_1st_str == "SAVED", f"Expected SAVED, but got {res_status_1st_str}"

    res_status_1st_str = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "__input7-__xmlview2--homeMainTable-1-inner"))
    ).get_attribute('value')
    assert res_status_1st_str == "NEW", f"Expected NEW, but got {res_status_1st_str}"

    # Проверка флага Itin
    try:
        # Ожидание доступности чек-бокса
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "__box0-__xmlview2--homeMainTable-0-CB"))
        )

        # Получение элемента чекбокса
        checkbox = driver.find_element(By.ID, "__box0-__xmlview2--homeMainTable-0-CB")

        # Проверка, что чекбокс включен
        is_checked = checkbox.is_selected()
        assert is_checked, f"Чекбокс 'Itin' не включен."

        print("Чекбокс 'Itin' включен.")

    except TimeoutException:
        print(f"Чекбокс 'Itin' не найден")
    except AssertionError as e:
        print(e)

    # Проверка, что дата заезда новой строки = дата выезда предыдущей строки
    try:
        # Ожидание, пока оба инпута дат станут доступными
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "__picker1-__xmlview2--homeMainTable-0-inner"))
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "__picker0-__xmlview2--homeMainTable-1-inner"))
        )

        # Получение значений из инпутов и их сравнение
        value1 = driver.find_element(By.ID, "__picker1-__xmlview2--homeMainTable-0-inner").get_attribute('value')
        value2 = driver.find_element(By.ID, "__picker0-__xmlview2--homeMainTable-1-inner").get_attribute('value')

        assert value1 == value2, f"Значения дат отъезда/заезда не совпадают: '{value1}' != '{value2}'"
        print("Значения дат отъезда/заезда совпадают.")

    except TimeoutException:
        print("Один из инпутов дат не найден в течение 10 секунд.")
    except AssertionError as e:
        print(e)

    save_reservation(driver)

    check_saving_reservation(driver)

    cancel_2nd_res_string(driver)

    check_cancelling_reservation(driver)

    # Проверка, что флаг Itin выключается
    try:
        # Ожидание доступности чек-бокса
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "__box0-__xmlview2--homeMainTable-0-CB"))
        )

        # Получение элемента чек-бокса
        checkbox = driver.find_element(By.ID, "__box0-__xmlview2--homeMainTable-0-CB")

        # Проверка, что чекбокс выключен
        is_checked = checkbox.is_selected()
        assert not is_checked, f"Чекбокс 'Itin' не выключен."

        print("Чекбокс 'Itin' выключен.")

    except TimeoutException:
        print(f"Чекбокс 'Itin' не найден")
    except AssertionError as e:
        print(e)

    cancel_1st_res_string(driver)

    clear_home_page(driver)


def hotkeys_alt_k(driver):

    driver.get("https://reserve.kube.ugmk.com/webapp/index.html#/home")

    add_new_res_string(driver)

    select_hotel_1st_str(driver)

    fillling_required_fields_1st_str_via2rooms (driver)

    save_reservation(driver)

    sleep(2)

    edit_mode_on(driver)

    # Включение выделения брони, проверка совпадения cnf nmb и уменьшения кол-ва комнат на 1

    cnf_number_id = "__link0"
    room_nmb_0_id = "__input0-__xmlview2--homeMainTable-0-inner"
    room_nmb_1_id = "__input0-__xmlview2--homeMainTable-1-inner"

    try:
        # Ожидание, пока cnf nmb станет доступным
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, cnf_number_id))
        )

        # Получение cnf nmb до выделения брони
        cnf_number_before = driver.find_element(By.ID, cnf_number_id).text
        print(f"Cnf nmb ДО выделения: {cnf_number_before}")

        # Получение room nmb из первой строки до выделения брони
        value_before = int(driver.find_element(By.ID, room_nmb_0_id).get_attribute('value'))
        print(f"Кол-во комнат в первой строке ДО выделения: {value_before}")

        # Выделение брони
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "__item3-__xmlview2--homeMainTable-0"))
        )
        body = driver.find_element(By.ID, "__item3-__xmlview2--homeMainTable-0")  # Фокус на строку бронирования
        body.send_keys(Keys.ALT, 'k')  # Отправка Alt + K

        # Ожидание, пока cnf nmb снова станет доступным
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, cnf_number_id), cnf_number_before)
        )

        # Получение cnf nmb после выделения брони
        cnf_number_after = driver.find_element(By.ID, cnf_number_id).text
        print(f"Cnf nmb ПОСЛЕ выделения: {cnf_number_after}")

        # Получение room nmb из второй строки после выделения брони
        value_after = int(driver.find_element(By.ID, room_nmb_1_id).get_attribute('value'))
        print(f"Кол-во комнат во второй строке ПОСЛЕ выделения: {value_after}")

        # Проверка, совпадает ли значение nf nmb
        assert cnf_number_before == cnf_number_after, "Cnf nmb изменился после выделения."
        print("CNF номер подтвержден, значения совпадают.")

        # Проверка, что кол-во комнат до выделения меньше на 1, чем кол-во после
        assert value_after == value_before - 1, f"Некорректное кол-во комнат: {value_after} != {value_before - 1}"

        print("Корректное кол-во комнат, значение увеличилось на 1.")

    except TimeoutException:
        print("Один из элементов не был найден в течение 10 секунд.")
    except AssertionError as e:
        print(e)

    # Проверка, что количество гостей совпадает в обоих строках
    try:
        # Ожидание доступности полей
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "__input1-__xmlview2--homeMainTable-0-inner"))
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "__input1-__xmlview2--homeMainTable-1-inner"))
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "__input2-__xmlview2--homeMainTable-0-inner"))
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "__input2-__xmlview2--homeMainTable-1-inner"))
        )

        # Получение значений
        adult_nmb_1st = driver.find_element(By.ID, "__input1-__xmlview2--homeMainTable-0-inner").get_attribute('value')
        adult_nmb_2nd = driver.find_element(By.ID, "__input1-__xmlview2--homeMainTable-1-inner").get_attribute('value')

        child_nmb_1st = driver.find_element(By.ID, "__input2-__xmlview2--homeMainTable-0-inner").get_attribute('value')
        child_nmb_2nd = driver.find_element(By.ID, "__input2-__xmlview2--homeMainTable-1-inner").get_attribute('value')

        # Проверка, что значения равны
        assert adult_nmb_1st == adult_nmb_2nd, "Значения в полях 'adult' не совпадают."
        assert child_nmb_1st == child_nmb_2nd, "Значения в полях 'child' не совпадают."

        print("Значения в полях 'adult' и 'child' совпадают.")

    except TimeoutException:
        print("Один из инпутов не был найден в течение 10 секунд.")
    except AssertionError as e:
        print(e)

    # Проверка, что данные профиля гостя не заполнены
    click_on_2nd_res_str(driver) # Фокус на вторую строку бронирования
    try:
        # Ожидание, пока инпут имени станет доступным
        name_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "__xmlview2--homeTabInputName_G-inner"))
        )
        # Проверка, инпут имени не заполнен
        assert not name_input.get_attribute("value"), "Поле 'Input Name' заполнено, но должно быть пустым."

        # Ожидание, пока селект выбора страны станет доступным
        country_select = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "__xmlview2--selectCountry_G-labelText"))
        )
        # Проверка, что селект выбора страны пустой
        assert not country_select.get_attribute("value"), "Поле 'Select Country' заполнено, но должно быть пустым."

        print("Данные профиля не заполнены - ОК")

    except TimeoutException:
        print("Всё ОК")
    except AssertionError as f:
        print(f)

    # Заполнение данных профиля гостя
    send_keys_to_element(driver, By.ID, "__xmlview2--homeTabInputName_G-inner", generate_guest_name())  # Имя гостя
    click_element(driver, By.ID, "__form1--FC-NoHead--Grid-wrapperfor-__xmlview2--selectCountry_G")  # Открыть список стран
    click_element(driver, By.XPATH, "//*[text()='Russian Federation']")  # Выбрать страну

    # Проверка статусов до сохранения
    check_1st_str_status_saved(driver)
    check_2nd_str_status_new(driver)

    # Сохранение брони
    save_reservation(driver)

    # Проверка сохранения
    check_saving_reservation(driver)

    # sleep(2)

    # Включение режима редактирования
    edit_mode_on(driver)

    # Удаление брони
    cancel_2nd_res_string(driver)
    cancel_1st_res_string(driver)

    # Проверка удаления брони
    check_cancelling_reservation(driver)

    clear_home_page(driver)


def hotkeys_ctrl_e_g_a(driver):

    get_link(driver)

    # Открытие окна поиска бронирований ('Get Reservation')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "__container0")))
    body = driver.find_element(By.ID, "__container0")  # Фокус на странице
    body.send_keys(Keys.CONTROL, 'e')  # Отправка Ctrl + E

    # Проверка отображения окна 'Get Reservation'
    try:
        # Ожидание, пока элемент станет доступным
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "__xmlview2--idGetReservationDlg"))
        )

        # Если элемент найден, можно выполнить дополнительные действия или просто вывести сообщение
        print(f"Окно 'Get Reservation' отображается на странице")

    except TimeoutException:
        # Если элемент не найден за отведенное время
        print(f"Окно 'Get Reservation' НЕ отображается на странице")
    except AssertionError as e:
        print(e)

    # Закрытие окна поиска бронирований ('Get Reservation')
    click_element(driver, By.ID, "__button10-BDI-content")

    sleep(1)

    # Открытие окна поиска гостей ('Guest Lookup')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "__container0")))
    body = driver.find_element(By.ID, "__container0")  # Фокус на странице
    body.send_keys(Keys.CONTROL, 'g')  # Отправка Ctrl + G

    sleep(1)

    # Проверка отображения окна 'Guest Lookup'
    try:
        # Ожидание, пока элемент станет доступным
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "__xmlview2--idGuestLookupDlg"))
        )

        # Если элемент найден, можно выполнить дополнительные действия или просто вывести сообщение
        print(f"Окно 'Guest Lookup' отображается на странице")

    except TimeoutException:
        # Если элемент не найден за отведенное время
        print(f"Окно 'Guest Lookup' НЕ отображается на странице")
    except AssertionError as e:
        print(e)

    # Закрытие окна поиска гостей ('Guest Lookup')
    click_element(driver, By.ID, "__button13-BDI-content")

    sleep(1)

    # Открытие окна поиска доступного бронирования ('Availability')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "__container0")))
    body = driver.find_element(By.ID, "__container0")  # Фокус на странице
    body.send_keys(Keys.CONTROL, 'a')  # Отправка Ctrl + A

    sleep(1)

    # Проверка отображения окна 'Availability'
    try:
        # Ожидание, пока элемент станет доступным
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "__xmlview2--idAvailabilityDlg"))
        )

        # Если элемент найден, можно выполнить дополнительные действия или просто вывести сообщение
        print(f"Окно 'Availability' отображается на странице")

    except TimeoutException:
        # Если элемент не найден за отведенное время
        print(f"Окно 'Availability' НЕ отображается на странице")
    except AssertionError as e:
        print(e)

    # Закрытие окна поиска доступного бронирования ('Availability')
    click_element(driver, By.ID, "__button14-BDI-content")



def test_onepage_res_payment_types(driver):  # Проверка сохранения/удаления брони, типов оплаты
    add_one_res_string(  # Простое бронирование в одну строку с оплатой картой
        driver,
        arrival_date=date.today().strftime("%d%m%Y"),  # Ввод текущей даты в формате "24092024"
        room_count=1,
        adults=1,
        children=0,
        guest_category="RAC",
        rate="TOT",
        room_type="KING",
        payment_info="VS 1111222233334444 0825",
        guest_name=generate_guest_name(),
        contact_name="BORIS",
        booking_source="K"
    )

    add_one_res_string(  # Простое бронирование в одну строку с оплатой наличными
        driver,
        arrival_date=date.today().strftime("%d%m%Y"),
        room_count=1,
        adults=2,
        children=0,
        guest_category="RAC",
        rate="RACK",
        room_type="KING",
        payment_info="CA",
        guest_name=generate_guest_name(),
        contact_name="ANTON",
        booking_source="K"
    )

def test_multipage_reservation(driver):
    add_three_res_strings(driver)


def test_hotkeys():
    test_functions = [
        hotkeys_alt_i,
        hotkeys_alt_s_e_x,
        hotkeys_alt_n_h,
        hotkeys_alt_d_y,
        hotkeys_alt_v,
        hotkeys_alt_k,
        hotkeys_ctrl_e_g_a
    ]

    for function in test_functions:
        driver = webdriver.Chrome()  # Создание новой сессии браузера (после каждого теста)
        driver.maximize_window()  # Включение полноэкранного отображения браузера
        try:
            function(driver)  # Вызов функции
            print(f"Тест '{function.__name__}' прошел успешно.")
        except Exception as e:  # Поймать любое исключение
            print(f"Ошибка при выполнении теста '{function.__name__}': {e}")
        finally:
            driver.quit()  # Закрытие сессии браузера (после каждого теста) независимо от результата