import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    ask_for_taxi_button = (By.XPATH, "//button[text()='Pedir un taxi']")
    comfort_tariff = (By.XPATH, "//div[text()='Comfort']")
    phone_number_button = (By.CLASS_NAME, "np-text")
    phone_window_field = (By.ID, 'phone')
    next_button = (By.XPATH, "//button[text()='Siguiente']")
    sms_code_field = (By.ID, 'code')
    confirm_button = (By.XPATH, "//button[text()='Confirmar']")
    payment_method_button = (By.CLASS_NAME, 'pp-text')
    add_card_button = (By.CLASS_NAME, 'pp-plus-container')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.XPATH, "//div[@class='card-code-input']//input[@id='code']")
    link_card_button = (By.CSS_SELECTOR, ".pp-buttons button[type='submit']")
    close_payment_window_button = (By.CSS_SELECTOR, '.payment-picker .close-button')
    message_field = (By.ID, 'comment')
    blanket_tissues_switch = (By.CLASS_NAME,'switch')
    ice_cream_plus_button = (By.CLASS_NAME, 'counter-plus')
    find_taxi_button = (By.CLASS_NAME, 'smart-button-wrapper')
    driver_search_modal = (By.CLASS_NAME, 'order-header-title')
    phone_number_display = (By.CLASS_NAME, "np-text")
    payment_method_label = (By.CLASS_NAME, "pp-value-text")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_ask_for_taxi_button(self):
        self.driver.find_element(*self.ask_for_taxi_button).click()

    def click_comfort_tariff(self):
        self.driver.find_element(*self.comfort_tariff).click()

    def click_phone_number_button(self):
        self.driver.find_element(*self.phone_number_button).click()

    def set_phone_number(self, phone):
        self.driver.find_element(*self.phone_window_field).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def set_sms_code(self, code):
        self.driver.find_element(*self.sms_code_field).send_keys(code)

    def click_confirm_button(self):
        self.driver.find_element(*self.confirm_button).click()

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def set_message_for_driver(self, message):
        self.driver.find_element(*self.message_field).send_keys(message)

    def click_blanket_tissues(self):
        self.driver.find_element(*self.blanket_tissues_switch).click()

    def add_ice_cream(self, quantity):
        button = self.driver.find_element(*self.ice_cream_plus_button)
        for _ in range(quantity):
            button.click()

    def click_find_taxi(self):
        self.driver.find_element(*self.find_taxi_button).click()

    def click_payment_method(self):
        self.driver.find_element(*self.payment_method_button).click()

    def click_add_card(self):
        self.driver.find_element(*self.add_card_button).click()

    def set_card_number(self, card_number):
        self.driver.find_element(*self.card_number_field).send_keys(card_number)

    def set_card_code(self, card_code):
        cvv_field = self.driver.find_element(*self.card_code_field)
        cvv_field.send_keys(card_code)
        cvv_field.send_keys(Keys.TAB)
        self.driver.find_element(By.CLASS_NAME, "payment-picker").click()

    def click_link_card(self):
        self.driver.find_element(*self.link_card_button).click()

    def click_close_payment_window(self):
        self.driver.find_element(*self.close_payment_window_button).click()

    def get_registered_phone_number(self):
        return self.driver.find_element(*self.phone_number_display).text

    def get_payment_method_text(self):
        return self.driver.find_element(*self.payment_method_label).text


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, 'from')))
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_plan(self):
        routes_page = UrbanRoutesPage(self.driver)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(routes_page.ask_for_taxi_button))
        routes_page.click_ask_for_taxi_button()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(routes_page.comfort_tariff))
        routes_page.click_comfort_tariff()
        tarifa_comfort = self.driver.find_element(*routes_page.comfort_tariff)
        assert tarifa_comfort.is_displayed()

    def test_fill_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(routes_page.phone_number_button))
        routes_page.click_phone_number_button()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(routes_page.phone_window_field))
        routes_page.set_phone_number(data.phone_number)
        routes_page.click_next_button()
        sms_code = retrieve_phone_code(self.driver)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(routes_page.sms_code_field))
        routes_page.set_sms_code(sms_code)
        routes_page.click_confirm_button()
        telefono_en_pantalla = routes_page.get_registered_phone_number()
        assert telefono_en_pantalla == data.phone_number

    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(routes_page.payment_method_button))
        routes_page.click_payment_method()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(routes_page.add_card_button))
        routes_page.click_add_card()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(routes_page.card_number_field))
        routes_page.set_card_number(data.card_number)
        routes_page.set_card_code(data.card_code)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(routes_page.link_card_button))
        routes_page.click_link_card()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(routes_page.close_payment_window_button))
        routes_page.click_close_payment_window()
        metodo_actual = routes_page.get_payment_method_text()
        assert metodo_actual == "Tarjeta"

    def test_comment_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        message = data.message_for_driver
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(routes_page.message_field))
        routes_page.set_message_for_driver(message)
        valor_mensaje = self.driver.find_element(*routes_page.message_field).get_property('value')
        assert valor_mensaje == message

    def test_order_blanket_and_handkerchiefs(self):
        routes_page = UrbanRoutesPage(self.driver)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(routes_page.blanket_tissues_switch))
        routes_page.click_blanket_tissues()
        switch_estado = self.driver.find_element(*routes_page.blanket_tissues_switch)
        assert switch_estado.is_enabled()

    def test_order_2_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_ice_cream(2)
        valor_helados = self.driver.find_element(By.CLASS_NAME, 'counter-value').text
        assert valor_helados == "2"

    def test_car_search_model_appears(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_find_taxi()
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(routes_page.driver_search_modal))
        search_modal = self.driver.find_element(*routes_page.driver_search_modal)
        assert search_modal.is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()