from selenium.webdriver.common.by import By



#configurar la direccion
class UrbanRoutesPage:

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    #pedir taxi
    text_pedir_un_taxi = (By.XPATH, '//*[text()="Pedir un taxi"]')
    click_order_taxi_button =(By.CLASS_NAME,"button.round")

    #Elegir tarifa comfort
    comfort_image = (By.XPATH, "//img[@alt='Comfort']")
    comfort_rate = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')

    #agregar numero de telefono
    phone_number_button = (By.CLASS_NAME, "np-text")
    phone_number = (By.CSS_SELECTOR, "#phone.input")
    click_button_next = (By.XPATH, '//*[text()="Siguiente"]')
    sms_code = (By.XPATH, '//*[@placeholder="xxxx"]')
    click_confirm_button = (By.XPATH, '//*[text()="Confirmar"]')

    #Agregar tarjeta de Credito
    click_payment_method = (By.CSS_SELECTOR, ".pp-button.filled")
    add_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
    card_number = (By.XPATH, '//*[@placeholder="1234 4321 1408"]')
    card_code = (By.CSS_SELECTOR, "#code.card-input")
    click_outside_focus = (By.CLASS_NAME, "card-wrapper")
    add_click = (By.XPATH, '//*[text()="Agregar"]')
    close_click = (By.XPATH, "//div[@class='payment-picker open']/div[@class='modal']/div[@class='section active']/button[@class='close-button section-close']")
    verified_card = (By.CLASS_NAME, "pp-value-text")

    #Escribir un mensaje para el conductor
    click_message_for_driver = (By.XPATH, '//*[text()="Mensaje para el conductor..."]')
    message_for_driver = (By.XPATH, '//*[@placeholder="Traiga un aperitivo"]')
    confirm_message = (By.XPATH, '//*[@placeholder="Traiga un aperitivo"]')

    #pedir una manta y un pañuelo
    add_blanket_scarf = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')

    #Pedir 2 helados
    two_click_counter_ice_cream = (By.CLASS_NAME, "counter-plus")
    counter_value = (By.CLASS_NAME, "counter-value")

    #Pedir un taxi
    order_taxi = (By.CLASS_NAME, "smart-button-main")

