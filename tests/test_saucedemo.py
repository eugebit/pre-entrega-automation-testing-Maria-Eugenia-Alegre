import time

import pytest
from utils.helpers import login_saucedemo, get_driver
from selenium.webdriver.common.by import By
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture  # (scope='session')mantiene la sesion iniciada para ejecutar dos los test que se deben ejecutar
def driver():
    driver = get_driver()
    yield driver  # mantiene la sesion iniciada
    driver.quit()


def test_login(driver):
    login_saucedemo(driver)
    assert "/inventory.html" in driver.current_url
    # por medio de Css_selector,dentro de este div padre va a ir a buscar una clase llamada título
    title = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert title == 'Products'


def test_catalog(driver):
    login_saucedemo(driver)
    time.sleep(2)
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    # chequeo que la lista tenga items
    assert len(products) > 0


def test_shopping_cart(driver):
    login_saucedemo(driver)
    time.sleep(4)

    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    cant_products = len(products)
    products[0].find_element(By.TAG_NAME, 'button').click()
    time.sleep(1)
    cant_items_carts = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert cant_items_carts == '1'
