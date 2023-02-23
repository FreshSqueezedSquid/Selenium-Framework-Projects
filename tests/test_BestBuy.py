import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
        mainPage.getSearchText().send_keys("AirPods Pro (2nd generation)")
        searchPage = mainPage.clickSearch()
        item_sku = searchPage.getSKU()
        i = -1
        for item in item_sku:
            i += 1
            sku_num = item.find_element(By.XPATH, "div[2]/span[2]").text
            log.info(sku_num)
            if sku_num == "4900964":
                log.info(sku_num)
                self.driver.execute_script("window.scrollTo(0, 250);")
                time.sleep(2)
                searchPage.addToCart()[i].click()
        time.sleep(3)
        cartPage = searchPage.goToCart()
        log.info(cartPage.cartItem().text)
        assert "Apple - AirPods Pro (2nd generation) - White" in cartPage.cartItem().text
        log.info("Item is in the cart")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='checkout-buttons__checkout']")))
        guestPage = cartPage.goToGuest()
        time.sleep(1.7)
        guestPage.guestLogin().click()
        time.sleep(3)
        # entering shipping info before scrolling down to enter contact info
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='firstName']")))
        guestPage.firstName().send_keys(getData["firstname"])
        time.sleep(1.2)
        guestPage.lastName().send_keys(getData["lastname"])
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#street")))
        time.sleep(1)
        guestPage.getAddress().send_keys(getData["address"])
        guestPage.getCity().send_keys(getData["city"])
        # opens drop down and selects
        dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, "#state"))
        dropdown.select_by_visible_text("AZ")
        guestPage.zipCode().send_keys(getData["zip_code"])
        time.sleep(2)
        guestPage.applyDetails().click()
        time.sleep(2)
        # scrolls to bottom of page to access final inputs and button
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        guestPage.getEmail().send_keys(getData["email"])
        guestPage.phoneNumber().send_keys(getData["phone_num"])
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-lg btn-block btn-secondary']")))
        guestPage.continuePayment().click()

    @pytest.fixture(params=ShippingData.test_shipping_data)
    def getData(self, request):
        return request.param




