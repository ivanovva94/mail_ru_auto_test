from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, browser: Chrome, url="https://mail.ru/", timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait = timeout

    def open_url(self):
        return self.browser.get(self.url)

    def find_element(self, *locator):
        return self.browser.find_element(*locator)

    def find_elements(self, *locator):
        return self.browser.find_elements(*locator)

    def is_element_present(self, *locator):
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def wait_element(self, *locator):
        try:
            return WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"\n * ЭЛЕМЕНТ НЕ НАЙДЕН В ТЕЧЕНИЕ ОТДАННОГО ВРЕМЕНИ! --> {locator[1]}")
            self.browser.quit()

    def wait_element_clickable(self, *locator):
        try:
            return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print(f"\n * ЭЛЕМЕНТ НЕ НАЙДЕН В ТЕЧЕНИЕ ОТДАННОГО ВРЕМЕНИ! --> {locator}")
            self.browser.quit()
