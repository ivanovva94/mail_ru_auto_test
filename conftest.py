import pytest
from selenium import webdriver

from page.login_page import LoginPage
from page.mail_box_page import MailBoxPage


@pytest.fixture(scope='class')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.binary_location = r"C:\chrome-win64\chrome.exe"
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture
def login_page(browser):
    return LoginPage(browser)


@pytest.fixture
def mailbox_page(browser):
    return MailBoxPage(browser)
