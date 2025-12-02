from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils import faker


class Checkout:
    URL_CHECKOUT = 'https://www.saucedemo.com/checkout-step-one.html'
    URL_CHECKOUT_OVERVIEW = 'https://www.saucedemo.com/checkout-step-two.html'
    URL_CHECKOUT_FINISH = 'https://www.saucedemo.com/checkout-complete.html'

    _INPUT_NAME = (By.ID, 'first-name')
    _INPUT_LAST_NAME = (By.ID, 'last-name')
    _INPUT_POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    def __init__(self, driver):
        self.driver = driver

    def is_at_checkout(self):
        return self.URL_CHECKOUT in self.driver.current_url

    def is_at_checkout_overview(self):
        return self.URL_CHECKOUT_OVERVIEW in self.driver.current_url

    def is_checkout_complete(self):
        return self.URL_CHECKOUT_FINISH in self.driver.current_url

    def fill_data(self):
        datos = faker.generar_datos_checkout_fake()  # DEVUELVE UN DICCIONARIO CON UN SOLO SET DE DATOS

        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable(self._INPUT_NAME)
        ).send_keys(datos['name'])
        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable(self._INPUT_LAST_NAME)
        ).send_keys(datos['last_name'])
        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable(self._INPUT_POSTAL_CODE)
        ).send_keys(datos['zip_code'])

    def click_continue_button(self):
        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    def click_finish_button(self):
        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        ).click()

    def click_back_home_button(self):
        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable(self.BACK_HOME_BUTTON)
        ).click()
