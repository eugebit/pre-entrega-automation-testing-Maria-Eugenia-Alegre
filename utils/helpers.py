import pytest
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://www.saucedemo.com'
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

_INPUT_NAME = 'user-name'
_INPUT_PASSWORD = 'password'
_LOGIN_BUTTON = 'login-button'


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
    driver.find_element(By.NAME, _INPUT_NAME).send_keys(USERNAME)
    time.sleep(2)
    driver.find_element(By.NAME, _INPUT_PASSWORD).send_keys(PASSWORD)
    time.sleep(2)
    driver.find_element(By.NAME, _LOGIN_BUTTON).click()
    time.sleep(2)


def take_screenshot(driver, name):
    path = '../Evidencias/' + name + '.png'
    driver.save_screenshot(path)
