from selenium.webdriver.common.by import By
from page.login_page import LoginPage
from utils.helpers import take_screenshot
# from data.data_login import CASOS_LOGIN
from utils.example_csv import get_login_csv, get_login_json
import pytest
from utils.faker import get_login_faker

@pytest.mark.parametrize("username,password,login_bool",get_login_faker())
def test_login_con_faker  (driver, username,password,login_bool):
    test_name = 'test_login'
    loginpage = LoginPage(driver)
    loginpage.open()
    loginpage.login(username,password)
    if login_bool:
        take_screenshot(driver, test_name)
        assert '/inventory.html' in driver.current_url
        # por medio de Css_selector,dentro de este div padre va a ir a buscar una clase llamada título
        title = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
        assert title == 'Products'
        loginpage.logout()
        assert loginpage.is_in_login_page()
    else:
        assert 'https://www.saucedemo.com' in driver.current_url

@pytest.mark.parametrize("username,password,login_bool",get_login_csv())
def test_login_con_csv(driver, username,password,login_bool):
    test_name = 'test_login'
    loginpage = LoginPage(driver)
    loginpage.open()
    loginpage.login(username,password)
    if login_bool:
        take_screenshot(driver, test_name)
        assert '/inventory.html' in driver.current_url
        # por medio de Css_selector,dentro de este div padre va a ir a buscar una clase llamada título
        title = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
        assert title == 'Products'
        loginpage.logout()
        assert loginpage.is_in_login_page()
    else:
        assert 'https://www.saucedemo.com' in driver.current_url

@pytest.mark.parametrize("username,password,login_bool",get_login_json())
def test_login_con_json(driver, username,password,login_bool):
    test_name = 'test_login'
    loginpage = LoginPage(driver)
    loginpage.open()
    loginpage.login(username,password)
    if login_bool:
        take_screenshot(driver, test_name)
        assert '/inventory.html' in driver.current_url
        # por medio de Css_selector,dentro de este div padre va a ir a buscar una clase llamada título
        title = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
        assert title == 'Products'
        loginpage.logout()
        assert loginpage.is_in_login_page()
    else:
        assert 'https://www.saucedemo.com' in driver.current_url



