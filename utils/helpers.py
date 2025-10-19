import pytest
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://www.saucedemo.com'
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

_INPUT_NAME = (By.NAME, 'user-name')
_INPUT_PASSWORD = (By.NAME, 'password')
_LOGIN_BUTTON = (By.NAME, 'login-button')


def get_driver():
    """
    --password-store=basic: This argument sets the password storage backend to a basic,
    non-integrated option, which effectively prevents Chrome's built-in password manager
    from functioning.
    no sé porque no está funcionando
    """
    chrome_options = Options()
    chrome_options.add_argument("--guest")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-dev-shm-usage')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    time.sleep(5)
    return driver


def login_saucedemo(driver):
    driver.get(URL)
    time.sleep(2)
    # ingreso las credenciales

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(_INPUT_NAME)
    ).send_keys(USERNAME)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(_INPUT_PASSWORD)
    ).send_keys(PASSWORD)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(_LOGIN_BUTTON)
    ).click()


def take_screenshot(driver, name):
    path = '../Evidencias/' + name + '.png'
    driver.save_screenshot(path)
