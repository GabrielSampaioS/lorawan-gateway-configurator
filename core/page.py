# core/page.py

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 30)

    def open(self, path):
        self.driver.get(self.base_url + path)

    def fill(self, locator, value):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.clear()
        element.send_keys(str(value))

        self.wait.until(
            lambda driver:
            element.get_attribute("value") == str(value)
        )

    def select(self, locator, value):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        Select(element).select_by_visible_text(value)

        self.wait.until(
            lambda driver:
            Select(
                driver.find_element(*locator)
            ).first_selected_option.text.strip() == str(value).strip()
        )

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def save(self, locator):
        self.click(locator)
