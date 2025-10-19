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
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-dev-shm-usage')
    service=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)


    time.sleep(5)
    return driver

def login_saucedemo(driver):
    driver.get(URL)
    time.sleep(2)
    #ingreso las credenciales
    driver.find_element(By.NAME,_INPUT_NAME).send_keys(USERNAME)
    time.sleep(2)
    driver.find_element(By.NAME,_INPUT_PASSWORD).send_keys(PASSWORD)
    time.sleep(2)
    driver.find_element(By.NAME,_LOGIN_BUTTON).click()
    time.sleep(2)
