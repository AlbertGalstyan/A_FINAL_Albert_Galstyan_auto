import json
import pytest
import os
import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture()
def config(scope='session'):
    cwd = os.getcwd()
    files = os.listdir(cwd)
    print("Files in %r: %s" % (cwd, files))
    with open('config.json') as config_file:
        config = json.load(config_file)
    assert config['browser'] in ['Firefox', 'Chrome', 'Remote_Chrome', 'Remote_Firefox']
    return config


"""@pytest.fixture()
def driver(config):
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    else:
        raise Exception(f'browser "{config["browser"]}"is not supported')
    b.maximize_window()
    b.get(config["baseUrl"])
    yield b
    b.quit()"""


@pytest.fixture()
def driver(config):
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Remote_Chrome':
        b = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                             desired_capabilities=DesiredCapabilities.CHROME)
    elif config['browser'] == 'Remote_Firefox':
        b = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                             desired_capabilities=DesiredCapabilities.FIREFOX)
    else:
        raise Exception(f'browser "{config["browser"]}"is not supported')
    b.maximize_window()
    b.get(config["baseUrl"])

    yield b
    b.quit()



"""
@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()

    def quit():
        driver.quit()

    request.addfinalizer(quit)
    return driver"""
