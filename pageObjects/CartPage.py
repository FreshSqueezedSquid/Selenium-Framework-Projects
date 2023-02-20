from selenium.webdriver.common.by import By
from pageObjects.GuestPage import GuestPage


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    cart_item = (By.CSS_SELECTOR, ".item-title")
    checkout_button = (By.XPATH, "//div[@class='checkout-buttons__checkout']")

    def cartItem(self):
        return self.driver.find_element(*CartPage.cart_item)

    def goToGuest(self):
        self.driver.find_element(*CartPage.checkout_button).click()
        guestPage = GuestPage(self.driver)
        return guestPage