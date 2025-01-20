from time import sleep
import pytest
from selenium import webdriver
from selenium.common import TimeoutException
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
    assert res_status_after_cancel == "CANCELLED", f"Expected SAVED, but got {res_status_after_cancel}"

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

    # Проверка на успешное удаление
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

def hotkeys_Alt_S_E_X(driver):
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

def test_hotkeys(driver):
    hotkeys_Alt_S_E_X(driver)