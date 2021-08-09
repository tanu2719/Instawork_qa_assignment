import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser_fixture):
    if browser_fixture == "chrome":
        driver = webdriver.Chrome(executable_path="E:\Instawork\chromedriver.exe")
    else:
        driver = webdriver.Firefox(executable_path="E:\Instawork\geckodriver.exe")
    return driver


# get browser from CLI\Command line
def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser_fixture(request):
    return request.config.getoption("--browser")

