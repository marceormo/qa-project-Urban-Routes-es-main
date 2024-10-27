from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
import locators
from data import phone_number, card_number, card_code, message_for_driver


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(5):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")

        return code



class MethodsUrbanRoutesPage:
    driver = None

#Configurar la dirección
    def __init__(self, driver):
      self.driver = driver

#espera a cargar la pagina
    def wait_for_load_header(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.from_field))

#Configurar la direccion
    def set_from(self):
        self.driver.find_element(*locators.UrbanRoutesPage.from_field).send_keys(data.address_from)
    def set_to(self):
        self.driver.find_element(*locators.UrbanRoutesPage.to_field).send_keys(data.address_to)
    def get_from(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.from_field).get_property('value')
    def get_to(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.to_field).get_property('value')

#click "Pedir taxi"
    def click_order_taxi_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.click_order_taxi_button))
        self.driver.find_element(*locators.UrbanRoutesPage.click_order_taxi_button).click()
    def check_click_order_taxi_button(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.click_order_taxi_button).is_enabled()

#Seleccionar tarifa Comfort
    def comfort_rate(self):
        self.driver.find_element(*locators.UrbanRoutesPage.comfort_rate).click()


#espera a agregar numero
    def wait_for_phone_number_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.phone_number_button))
#Rellenar "Numero de Telefono"
    def phone_number_button(self):
        self.driver.find_element(*locators.UrbanRoutesPage.phone_number_button).click()
    def phone_number(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.phone_number).send_keys(phone_number)
    def check_phone_number(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.phone_number).get_property("value")
    def get_phone_number(self):
        self.driver.find_element(*locators.UrbanRoutesPage.phone_number).get_property("value")
    def click_button_next(self):
        self.driver.find_element(*locators.UrbanRoutesPage.click_button_next).click()

#enviar mensaje de texto
    def sms_code(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.sms_code).send_keys(retrieve_phone_code(self.driver))
    def click_confirm_button(self):
        self.driver.find_element(*locators.UrbanRoutesPage.click_confirm_button).click()
    def check_click_confirm_button(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.click_confirm_button).is_enabled()


#Agragar tarjeta de credito
    def click_payment_method(self):
        self.driver.find_element(*locators.UrbanRoutesPage.click_payment_method).click()
    def add_card_button(self):
        self.driver.find_element(*locators.UrbanRoutesPage.add_card_button).click()
    def card_number(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.card_number).send_keys(card_number)
    def check_card_number(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.card_number).get_property("value")

#codigo cvv
    def card_code(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.card_code).send_keys(card_code)
    def click_outside_focus(self):
        self.driver.find_element(*locators.UrbanRoutesPage.click_outside_focus).click()
    def add_click(self):
        self.driver.find_element(*locators.UrbanRoutesPage.add_click).click()
    def close_click(self):
        self.driver.find_element(*locators.UrbanRoutesPage.close_click).click()
    def verified_card(self):
        self.driver.find_element(*locators.UrbanRoutesPage.verified_card)
    def check_card_code(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.card_code).get_property("value")

#Mensaje para el conductor
    def click_message_for_driver(self):
        self.driver.find_element(*locators.UrbanRoutesPage.click_message_for_driver).click()
    def message_for_driver(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.message_for_driver).send_keys(message_for_driver)
    def confirm_message(self):
        self.driver.find_element(*locators.UrbanRoutesPage.confirm_message)
    def verify_message(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.confirm_message).get_property("value")

#Pedir una manta y un pañuelo
    def add_blanket_scarf(self):
        self.driver.find_element(*locators.UrbanRoutesPage.add_blanket_scarf).click()
    def check_add_blanket_scarf(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.add_blanket_scarf).is_enabled()

#pedir dos helados
    def two_click_counter_ice_cream(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.two_click_counter_ice_cream))
        self.driver.find_element(*locators.UrbanRoutesPage.two_click_counter_ice_cream).click()
        self.driver.find_element(*locators.UrbanRoutesPage.two_click_counter_ice_cream).click()
    def verify_ice_cream(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.counter_value).text

#pedir un taxi
    def order_taxi(self):
        self.driver.find_element(*locators.UrbanRoutesPage.order_taxi).click()
    def check_order_taxi(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.order_taxi).is_enabled()


