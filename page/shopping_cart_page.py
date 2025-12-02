from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ShoppingCartPage:
    URL_CURRENT = 'https://www.saucedemo.com/cart.html'
    # MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    # LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')
    SHOPPING_CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    SHOPPING_CART_BUTTON = (By.ID, 'shopping_cart_container')
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def is_at_shopping_cart_page(self):
        return self.URL_CURRENT in self.driver.current_url

    def items_in_cart(self):
        items_in_cart = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SHOPPING_CART_BADGE)
        ).text
        return int(items_in_cart)

    def go_to_your_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SHOPPING_CART_BUTTON)
        ).click()

    def click_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()
