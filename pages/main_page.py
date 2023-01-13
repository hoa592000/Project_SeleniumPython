from pages.base_page import BasePage
from pages.alert_page import AlertPage
from selenium.webdriver.common.by import By


from utils.locators import *


class MainPage(BasePage):

    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)

    def click_alert_page(self):
        elm = self.find_element(
            By.XPATH, "//a[text()='JavaScript Alerts']")
        elm.click()
        return AlertPage(self.driver)
