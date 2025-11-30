import pytest
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import requests

URL = 'https://www.saucedemo.com'


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


def take_screenshot(driver, name):
    path = '../Evidencias/' + name + '.png'
    driver.save_screenshot(path)

