
import unittest
from tests.base_test import BaseTest
from pages.main_page import *
from utils.test_cases import test_cases
from utils.locators import *


class TestAlertPage(BaseTest):
    def test_redirect_url(self):
        print("\n" + str(test_cases(1)))
        page = MainPage(self.driver)
        alert_page = page.click_alert_page()

        self.assertEqual(alert_page.get_url(), "https://the-internet.herokuapp.com/javascript_alerts")

    def test_alert_button(self):
        print("\n" + str(test_cases(2)))
        page = MainPage(self.driver)
        alert_page = page.click_alert_page()
        alert_page.click_alert_button()
        alert_page.click_alert_popup()
        result = alert_page.get_result_text()
        final = self.assertEqual(result, "You successfully clicked an alert")
        print("Test result: " + str(final))
