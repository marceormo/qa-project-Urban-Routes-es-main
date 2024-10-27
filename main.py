from time import sleep

import data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import locators


from locators import UrbanRoutesPage

from methods import MethodsUrbanRoutesPage


def is_displayed():
    pass


class TestUrbanRoutes:
    driver = None
    methods = None

    @classmethod
    def setup_class(cls):

        # Configurar las opciones del navegador
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

            # Iniciar el servicio de Chrome
        service = Service()  # Puedes pasar el path del driver aquí si es necesario

            # Inicializar el driver con opciones
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.get(data.urban_routes_url)
        cls.locators = UrbanRoutesPage()
        #cls.methods = MethodsUrbanRoutesPage(cls.driver)
        cls.routes_page = MethodsUrbanRoutesPage(cls.driver)
        cls.driver.implicitly_wait(10)

#configurar pagina
    def test_set_route(self):
        self.routes_page.set_from()
        self.routes_page.set_to()
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

#pedir taxi
    def test_click_order_taxi_button(self):
        self.routes_page.click_order_taxi_button()
        assert self.routes_page.check_click_order_taxi_button()

#Seleccionar tarifa Comfort
    def test_comfort_rate(self):
        self.routes_page.comfort_rate()
        assert self.routes_page.driver.find_element(*locators.UrbanRoutesPage.comfort_image).is_displayed()

#Rellenar "Numero de telefono"
    def test_phone_number_button(self):
        self.routes_page.phone_number_button()
        self.routes_page.phone_number()
        self.routes_page.check_phone_number()
        assert  self.routes_page.check_phone_number() == data.phone_number

    def test_sms_code(self):
        self.routes_page.click_button_next()
        self.routes_page.sms_code()
        self.routes_page.click_confirm_button()
        assert self.routes_page.check_click_confirm_button()


#Agregar tarjeta de credito
    def test_click_payment_method(self):
        self.routes_page.click_payment_method()
        self.routes_page.add_card_button()
        self.routes_page.card_number()
        assert self.routes_page.check_card_number() == data.card_number

    def test_card_code(self):
        self.routes_page.card_code()
        self.routes_page.click_outside_focus()
        self.routes_page.add_click()
        self.routes_page.close_click()
        self.routes_page.verified_card()
        assert self.routes_page.check_card_code() == data.card_code

#Enviar mensaje al conductor
    def test_click_message_for_driver(self):
        self.routes_page.click_message_for_driver()
        self.routes_page.message_for_driver()
        self.routes_page.confirm_message()
        assert self.routes_page.verify_message() == data.message_for_driver

#Pedir una manta y un pañuelo
    def test_add_blanket_scarf(self):
        self.routes_page.add_blanket_scarf()
        assert self.routes_page.check_add_blanket_scarf()

#pedir dos helados
    def test_two_click_counter_ice_cream(self):
        self.routes_page.two_click_counter_ice_cream()
        assert self.routes_page.verify_ice_cream() == "2"

#pedir un taxi
    def test_order_taxi(self):
        self.routes_page.order_taxi()
        assert self.routes_page.check_order_taxi()

    @classmethod
    def teardown_class(cls):
        sleep(10)
        cls.driver.quit()
