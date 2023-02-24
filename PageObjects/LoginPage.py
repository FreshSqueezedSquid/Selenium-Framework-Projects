from selenium.webdriver.common.by import By

from PageObjects.FlightFinderPage import FlightFinder


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    login = (By.CSS_SELECTOR, "#log-in-button")
    member_id = (By.CSS_SELECTOR, "#loginId")
    lastname = (By.CSS_SELECTOR, "#lastName")
    password = (By.CSS_SELECTOR, "#password")
    conf_login = (By.CSS_SELECTOR, "#button_login")

    def goToLogin(self):
        return self.driver.find_element(*LoginPage.login)

    def getMemeberId(self):
        return self.driver.find_element(*LoginPage.member_id)

    def getLastname(self):
        return self.driver.find_element(*LoginPage.lastname)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def confLogin(self):
        self.driver.find_element(*LoginPage.conf_login).click()
        flightFinderPage = FlightFinder(self.driver)
        return flightFinderPage