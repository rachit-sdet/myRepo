import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def class_setup():
    opt_obj = Options()
    opt_obj.add_argument('----start-maximized')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.close()
