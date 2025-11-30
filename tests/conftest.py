import pytest
from utils.helpers import get_driver

@pytest.fixture  # (scope='session')mantiene la sesion iniciada para ejecutar dos los test que se deben ejecutar
def driver():
    driver = get_driver()
    yield driver  # mantiene la sesion iniciada
    driver.quit()

@pytest.fixture
def api_url():
    return "https://jsonplaceholder.typicode.com/"