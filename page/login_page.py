import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import URL
from selenium.webdriver.common.by import By

class LoginPage:
    _INPUT_NAME = (By.NAME, 'user-name')
    _INPUT_PASSWORD = (By.NAME, 'password')
    _LOGIN_BUTTON = (By.NAME, 'login-button')
    MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(URL)
        time.sleep(2)

    def login(self,username,password):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._INPUT_NAME)
        ).send_keys(username)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._INPUT_PASSWORD)
        ).send_keys(password)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._LOGIN_BUTTON)
        ).click()

    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
        ).click()  # el * desarma la tupla,no hizo falta poner el * como dijo bray
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGOUT_BUTTON)
        ).click()
        time.sleep(3)
    def is_in_login_page(self):
        return URL in self.driver.current_url
