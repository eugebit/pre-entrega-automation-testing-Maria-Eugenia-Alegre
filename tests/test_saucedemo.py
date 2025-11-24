import time
import pytest
import selenium
# from utils.helpers import get_driver, take_screenshot
# from selenium.webdriver.common.by import By
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#

# @pytest.fixture  # (scope='session')mantiene la sesion iniciada para ejecutar dos los test que se deben ejecutar
# def driver():
#     driver = get_driver()
#     yield driver  # mantiene la sesion iniciada
#     driver.quit()


# def test_catalog(driver):
#     test_name = 'test_catalog'
#     login_saucedemo(driver)
#     products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
#
#     title = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CLASS_NAME, 'app_logo'))
#     ).text
#     menu = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, 'react-burger-menu-btn'))
#     ).text
#     take_screenshot(driver, test_name)
#     assert title == 'Swag Labs'  # Verifico que el titulo este correcto
#
#     assert len(products) > 0  # verifico que haya una lista de productos con al menos un producto
#     assert menu == "Open Menu"  # verifico que exista el menu

#
# def test_shopping_cart(driver):
#     test_name = 'test_shopping_cart'
#     login_saucedemo(driver)
#     products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
#     products[0].find_element(By.TAG_NAME, 'button').click()
#
#     cant_items_carts = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_badge'))
#     ).text
#
#     WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, 'shopping_cart_container'))
#     ).click()
#
#     title = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CLASS_NAME, 'title'))
#     ).text
#     take_screenshot(driver, test_name)
#     assert cant_items_carts == '1'
#     assert title == 'Your Cart'
