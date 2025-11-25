from selenium.webdriver.common.by import By
from page.login_page import LoginPage
from utils.helpers import take_screenshot


def test_login(driver):
    test_name = 'test_login'
    loginpage = LoginPage(driver)
    loginpage.open()
    loginpage.login()
    take_screenshot(driver, test_name)
    assert '/inventory.html' in driver.current_url
    # por medio de Css_selector,dentro de este div padre va a ir a buscar una clase llamada título
    title = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert title == 'Products'
    loginpage.logout()
