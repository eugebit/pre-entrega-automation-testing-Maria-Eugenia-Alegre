from selenium.webdriver.common.by import By
from page.login_page import LoginPage
from utils.helpers import take_screenshot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_catalog(driver):
    test_name = 'test_catalog'
    loginpage = LoginPage(driver)
    loginpage.open()
    loginpage.login()
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')

    title = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'app_logo'))
    ).text
    menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'react-burger-menu-btn'))
    ).text
    take_screenshot(driver, test_name)
    assert title == 'Swag Labs'  # Verifico que el titulo este correcto
    assert len(products) > 0  # verifico que haya una lista de productos con al menos un producto
    assert menu == "Open Menu"  # verifico que exista el menu
