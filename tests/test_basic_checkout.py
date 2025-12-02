from django.contrib.auth import login
from selenium.webdriver.common.by import By
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.checkout_page import Checkout

from page.shopping_cart_page import ShoppingCartPage
from utils.helpers import take_screenshot
from utils.helpers import USERNAME,PASSWORD


def test_basic_checkout(driver):
    test_name = 'test_basic_check_out'
    # 1. me logueo
    loginpage = LoginPage(driver)
    inventory = InventoryPage(driver)
    shopping_cart = ShoppingCartPage(driver)
    checkout = Checkout(driver)
    loginpage.open()
    loginpage.login(USERNAME,PASSWORD)
    inventory.add_item_to_cart(1)
    shopping_cart.go_to_your_cart()
    shopping_cart.click_checkout()
    assert checkout.is_at_checkout()==True
    checkout.fill_data()
    checkout.click_continue_button()
    assert checkout.is_at_checkout_overview()==True
    take_screenshot(driver, test_name)
    checkout.click_finish_button()
    assert checkout.is_checkout_complete()==True
    checkout.click_back_home_button()
    assert inventory.is_at_inventory_page()==True
    loginpage.logout()
    assert loginpage.is_in_login_page()

