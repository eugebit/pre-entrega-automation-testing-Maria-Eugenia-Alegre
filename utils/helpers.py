import pytest
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import requests
from datetime import datetime

URL = 'https://www.saucedemo.com'
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def get_driver():
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


def get_screenshot_name():
    # Generar nombre del archivo con la fecha y hora actual
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_name = f"captura_error{timestamp}.png"
    return screenshot_name


def take_screenshot(driver, test_name):
    screenshot_name = get_screenshot_name()
    path = '../Evidencias' + test_name + screenshot_name + '.png'
    driver.save_screenshot(path)
