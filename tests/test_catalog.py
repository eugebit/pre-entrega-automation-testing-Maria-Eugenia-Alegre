from selenium.webdriver.common.by import By
from page.login_page import LoginPage
from utils.helpers import URL, USERNAME,PASSWORD

from utils.helpers import take_screenshot
from page.inventory_page import InventoryPage

def test_catalog(driver):
    test_name = 'test_catalog'
    loginpage = LoginPage(driver)
    loginpage.open()
    loginpage.login(USERNAME,PASSWORD)
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    inventory = InventoryPage(driver)
    inventory.is_at_inventory_page()
    take_screenshot(driver, test_name)
    loginpage.logout()

    assert len(products) > 0  # verifico que haya una lista de productos con al menos un producto
    assert loginpage.is_in_login_page()


    """
    despues ver si puedo agregar estas validaciones como funciones que devuelvan el título el menu etc 
    """
    # title = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME, 'app_logo'))
    # ).text
    # menu = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.ID, 'react-burger-menu-btn'))
    # ).text
    # assert title == 'Swag Labs'  # Verifico que el titulo este correcto
    # assert menu == "Open Menu"  # verifico que exista el menu
