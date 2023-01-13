from pages.base_page import BasePage
from selenium.webdriver.common.by import By


from utils.locators import *


class AlertPage(BasePage):
    def __init__(self, driver):
        self.locator = AlertPageLocators
        super().__init__(driver)

    def click_alert_button(self):
        self.find_element(
            By.XPATH, "//button[text()='Click for JS Alert']").click()

    def click_alert_popup(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            print("Unexpected alert present")

    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            print("Unexpected alert present")

    def get_result_text(self):
        return self.find_element(By.ID, 'result').text
