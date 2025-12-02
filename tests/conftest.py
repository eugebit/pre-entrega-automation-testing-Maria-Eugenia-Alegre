import logging
import pathlib
import pytest
from utils.helpers import get_driver
from datetime import datetime


@pytest.fixture  # (scope='session')mantiene la sesion iniciada para ejecutar dos los test que se deben ejecutar
def driver():
    driver = get_driver()
    yield driver  # mantiene la sesion iniciada
    driver.quit()


@pytest.fixture
def api_url():
    return "https://jsonplaceholder.typicode.com/"

path_dir = pathlib.Path('../logs')
path_dir.mkdir(exist_ok=True)
logging.basicConfig(
    filename=path_dir / "historial.log",
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s - %(message)a',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger('talentolab')

path_dir = pathlib.Path('../../Evidencias')
path_dir.mkdir(exist_ok=True)
