from selenium.webdriver.common.by import By
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.shopping_cart_page import ShoppingCartPage
from utils.helpers import take_screenshot
from utils.helpers import USERNAME, PASSWORD
from page.checkout_page import Checkout
from datetime import datetime
import time
import pytest


# @pytest.mark.smoke
def test_complete_purchase_flow(driver):
    test_name = 'test_complete_purchase_flow'
    loginpage = LoginPage(driver)
    inventory = InventoryPage(driver)
    shopping_cart = ShoppingCartPage(driver)
    checkout = Checkout(driver)
    loginpage.open()
    # 1. me logueo
    loginpage.login(USERNAME, PASSWORD)
    # 2.cheuqeo que estoy en inventory
    assert inventory.is_at_inventory_page() == True
    take_screenshot(driver, test_name)
    # 3.agrego productos al carrito
    cant_items = 3
    inventory.add_item_to_cart(cant_items)
    # 4.chequeo que se hayan agregado
    assert shopping_cart.items_in_cart() == cant_items
    take_screenshot(driver, test_name)
    # 5. voy a la pag del carrito
    shopping_cart.go_to_your_cart()
    assert shopping_cart.is_at_shopping_cart_page() == True
    take_screenshot(driver, test_name)
    # 6. comienzo el checkout
    shopping_cart.click_checkout()
    assert checkout.is_at_checkout() == True
    take_screenshot(driver, test_name)
    # 7. relleno la data que me pide la pag
    checkout.fill_data()
    time.sleep(3)
    take_screenshot(driver, test_name)
    # 8. le doy continuar
    checkout.click_continue_button()
    assert checkout.is_at_checkout_overview() == True
    take_screenshot(driver, test_name)
    # 10. finalizo el proceso de compra
    checkout.click_finish_button()
    assert checkout.is_checkout_complete() == True
    take_screenshot(driver, test_name)
    checkout.click_back_home_button()
    assert inventory.is_at_inventory_page() == True
    take_screenshot(driver, test_name)
    # 11. me deslogueo
    loginpage.logout()
    assert loginpage.is_in_login_page()
