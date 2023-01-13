from selenium.webdriver.common.by import By


class MainPageLocators(object):
    ALERTPAGE = (By.XPATH, "//a[text()='JavaScript Alerts']"),
    LOGO = (By.XPATH, "//div[@class='heading']/h2")


class AlertPageLocators(object):
    ALERT = (By.XPATH, "//button[text()='Click for JS Alert']"),
