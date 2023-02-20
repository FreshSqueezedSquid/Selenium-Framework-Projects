from selenium.webdriver.common.by import By
from pageObjects.CartPage import CartPage


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    item_sku = (By.XPATH, "//div[@class='sku-model']") #"//div[@class='sku-attribute-title'][2]")
    item_bttn = (By.XPATH, "//div[@class='sli-add-to-cart']")
    cart = (By.XPATH, "//div[@class='go-to-cart-button']")

    def getSKU(self):
        return self.driver.find_elements(*SearchPage.item_sku)

    def addToCart(self):
        return self.driver.find_elements(*SearchPage.item_bttn)

    def goToCart(self):
        self.driver.find_element(*SearchPage.cart).click()
        cartPage = CartPage(self.driver)
        return cartPage