from selenium.webdriver.common.by import By
from page.login_page import LoginPage
from utils.helpers import take_screenshot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shopping_cart(driver):
    test_name = 'test_shopping_cart'
    loginpage = LoginPage(driver)
    loginpage.open()
    loginpage.login()
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    products[0].find_element(By.TAG_NAME, 'button').click()

    cant_items_carts = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_badge'))
    ).text

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'shopping_cart_container'))
    ).click()

    title = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'title'))
    ).text
    take_screenshot(driver, test_name)
    assert cant_items_carts == '1'
    assert title == 'Your Cart'

