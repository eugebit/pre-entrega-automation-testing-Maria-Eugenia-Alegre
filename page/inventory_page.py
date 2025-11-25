from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class InventoryPage:
    URL_current = '/inventory.html'

    def __init__(self, driver):
        self.driver = driver

    def is_at_page(self):
        return self.URL_current in self.driver.current_url

    def add_item_to_cart(self):
        products = self.driver.find_elements(By.CLASS_NAME, 'inventory_item')
        products[0].find_element(By.TAG_NAME, 'button').click()

