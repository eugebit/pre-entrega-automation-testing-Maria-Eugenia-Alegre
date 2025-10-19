import time
import pytest
import selenium
from utils.helpers import login_saucedemo, get_driver, take_screenshot
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
    test_name = 'test_login'
    login_saucedemo(driver)
    time.sleep(4)
    take_screenshot(driver, test_name)
    assert '/inventory.html' in driver.current_url
    # por medio de Css_selector,dentro de este div padre va a ir a buscar una clase llamada título
    title = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert title == 'Products'


def test_catalog(driver):
    test_name = 'test_catalog'
    login_saucedemo(driver)
    time.sleep(2)
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    time.sleep(2)
    title = driver.find_element(By.CLASS_NAME, 'app_logo').text
    menu = driver.find_element(By.ID, "react-burger-menu-btn").text
    take_screenshot(driver, test_name)

    # Verifico que el titulo este correcto
    assert title == 'Swag Labs'
    # verifico que haya una lista de productos con al menos un producto
    assert len(products) > 0
    assert menu == "Open Menu"


def test_shopping_cart(driver):
    test_name = 'test_shopping_cart'
    login_saucedemo(driver)
    time.sleep(4)

    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    products[0].find_element(By.TAG_NAME, 'button').click()
    time.sleep(1)
    cant_items_carts = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    driver.find_element(By.ID, 'shopping_cart_container').click()
    time.sleep(2)
    title = driver.find_element(By.CLASS_NAME, 'title').text
    take_screenshot(driver, test_name)
    assert cant_items_carts == '1'
    assert title == 'Your Cart'
