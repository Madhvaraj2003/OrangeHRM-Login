# Imported pytest module
import pytest
from selenium import webdriver

@pytest.fixture
# Sets up the Browser
def browser():
# Sets up the chrome driver before a test and quits it after the test completes    
    driver = webdriver.Chrome()
# Maximize the browser window for better visibility during test
    driver.maximize_window()
# Provides the driver for test    
    yield driver
# Quits browser after test completion    
    driver.quit()