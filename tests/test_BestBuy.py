import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestData.shippingData import ShippingData
from pageObjects.MainPage import MainPage
from utilities.BaseClass import BaseClass


class TestBestBuy(BaseClass):


    def test_printerPurchase(self, getData):
        wait = WebDriverWait(self.driver, 15)
        log = self.getLog()
        mainPage = MainPage(self.driver)
        mainPage.getSearchText().send_keys("epson ecotank")
        searchPage = mainPage.clickSearch()
        item_sku = searchPage.getSKU()
        i = -1
        for item in item_sku:
            i += 1
            sku_num = item.find_element(By.XPATH, "div[2]/span[2]").text
            log.info(sku_num)
            if sku_num == "6470013":
                log.info(sku_num)
                self.driver.execute_script("window.scrollTo(0, 250);")
                time.sleep(2)
                searchPage.addToCart()[i].click()
        time.sleep(3)
        cartPage = searchPage.goToCart()
        log.info(cartPage.cartItem().text)
        assert "ET-2850" in cartPage.cartItem().text
        log.info("Item is in the cart")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='checkout-buttons__checkout']")))
        guestPage = cartPage.goToGuest()
        time.sleep(1.7)
        guestPage.guestLogin().click()
        time.sleep(3)
        # enter shipping info before scrolling down to enter contact info
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='firstName']")))
        guestPage.firstName().send_keys(getData["firstname"])
        time.sleep(1.2)
        guestPage.lastName().send_keys(getData["lastname"])
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#street")))
        time.sleep(1)
        guestPage.getAddress().send_keys(getData["address"])
        guestPage.getCity().send_keys(getData["city"])
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @pytest.fixture(params=ShippingData.test_shipping_data)
    def getData(self, request):
        return request.param




