from selenium.webdriver.common.by import By


class SelectFlight:

    def __init__(self, driver):
        self.driver = driver

    lowest_fare = (By.XPATH, "//button[@id='flight0-product1']")
    close_popup = (By.CSS_SELECTOR, "#closeToolTip")
    status_pref = (By.CSS_SELECTOR, "#btn-main-cabin")
    guest_login = (By.CSS_SELECTOR, "#continue-as-guest-btn")

    def lowestPricedFlight(self):
        return self.driver.find_element(*SelectFlight.lowest_fare)

    def closePopUp(self):
        return self.driver.find_element(*SelectFlight.close_popup)

    def statusPref(self):
        return self.driver.find_element(*SelectFlight.status_pref)

    def guestLogin(self):
        return self.driver.find_element(*SelectFlight.guest_login)