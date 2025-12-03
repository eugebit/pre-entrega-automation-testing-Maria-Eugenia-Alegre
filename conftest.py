import logging
import pathlib
from fileinput import filename
import pytest_html
from selenium import webdriver
import pytest
from jinja2 import TemplateRuntimeError

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

path_dir = pathlib.Path('logs')
path_dir.mkdir(exist_ok=True)
logging.basicConfig(
    filename=path_dir / "historial.log",
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s - %(message)a',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger('talentolab')

# path_dir = pathlib.Path('Evidencias')
# path_dir.mkdir(exist_ok=True)


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytes_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     if report.when == 'call' and report.failed:
#         driver = item.funcargs.get('driver')
#         if driver:
#             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#             screenshot_name = f"{timestamp}.png"
#             filename = path_dir / screenshot_name
#             driver.save_screenshot(str(filename))
#             if hasattr(report, 'extra'):
#                 report.extra.append({
#                     'name': 'screenshot',
#                     'format': 'image',
#                     'content': str(filename),
#                 })
#
