from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class InventoryPage:
    CURRENT_URL = '/inventory.html'

    def __init__(self, driver):
        self.driver = driver

    def is_at_inventory_page(self):
        return self.CURRENT_URL in self.driver.current_url

    def add_item_to_cart(self,cuantos):
        products = self.driver.find_elements(By.CLASS_NAME, 'inventory_item')
        for i in range(cuantos):
            products[i].find_element(By.TAG_NAME, 'button').click()

