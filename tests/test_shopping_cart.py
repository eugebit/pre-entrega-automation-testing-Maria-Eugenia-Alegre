from selenium.webdriver.common.by import By
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.shopping_cart_page import ShoppingCartPage
from utils.helpers import take_screenshot


def test_shopping_cart(driver):
    test_name = 'test_shopping_cart'
    # 1. me logueo
    loginpage = LoginPage(driver)
    inventory = InventoryPage(driver)
    shopping_cart = ShoppingCartPage(driver)
    loginpage.open()
    loginpage.login()
    # 2.cheuqeo que estoy en inventory
    inventory.is_at_inventory_page()
    # 3.agrego productos al carrito
    inventory.add_item_to_cart()
    # 4.chequeo que se hayan agregado
    assert shopping_cart.items_in_cart() > 0
    # 5. voy a la pag del carrito
    shopping_cart.go_to_your_cart()
    take_screenshot(driver, test_name)
    assert shopping_cart.is_at_shopping_cart_page()
    # 6. me deslogueo
    loginpage.logout()
    assert loginpage.is_in_login_page()
