import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.FlightFinderPage import FlightFinder
from TestData.TripData import TripData
from utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC


class TestAA(BaseClass):

    def test_flightBooking(self, getData):

        log = self.getLog()
        wait = WebDriverWait(self.driver, 100)

        flightFinderPage = FlightFinder(self.driver)
        time.sleep(3)
        # closes cookie warning banner so as not to block any inputs
        try:
            elem = self.driver.find_element(By.XPATH, "//button[@name='closeBannerButton']")
            if elem.is_displayed():
                elem.click()  # this will click the element if it is there
                log.info("Cookie warning encountered and closed")
        except NoSuchElementException:
            log.info("No warning encountered")

        wait.until(EC.element_to_be_clickable(flightFinderPage.getDestination()))
        flightFinderPage.getDestination().send_keys(getData["destination"])
        wait.until(EC.element_to_be_clickable(flightFinderPage.departDate()))
        time.sleep(2)
        flightFinderPage.departDate().send_keys(getData["depart_date"])
        wait.until(EC.element_to_be_clickable(flightFinderPage.returnDate()))
        flightFinderPage.returnDate().send_keys(getData["return_date"])
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='flightSearchForm.button.reSubmit']")))
        selectFlightPage = flightFinderPage.selectFlight()
        # checks to see if the page is taking extra time to load
        try:
            elem = self.driver.find_element(By.CSS_SELECTOR, ".message_text")
            if elem.text.is_displayed():
                log.info("Waiting for page to load")

        except NoSuchElementException:
            log.info("No pop-up detected")
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#aa-pageTitle")))

        # closes tool-tip/info pop-up so as not to block available flights to click
        try:
            elem = self.driver.find_element(By.XPATH, "(//button[@id='closeTooltip'])[1]")
            if elem.is_displayed():
                elem.click()  # this will click the element if it is there
                log.info("Tool-tip encountered and closed")
        except NoSuchElementException:
            log.info("No tool-tip encountered")

        time.sleep(3)

        # AA.com can give 2 different ways of identifying flight choices...this try/except block accounts for that
        try:
            elem = self.driver.find_element(By.CSS_SELECTOR, "#flight0-product1")
            if elem.is_displayed():
                elem.click()  # this will click the element if it is there
                log.info("Alt CSS id detected")

        except NoSuchElementException:
            log.info("No alt id detected")
            selectFlightPage.lowestDepartPrice().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='row flight-matrix'])[1]")))
        # scrolls down so cheapest return flight options are visible
        self.scrollDown()

        # AA.com can give 2 different ways of identifying flight choices...this try/except block accounts for that
        try:
            elem = self.driver.find_element(By.CSS_SELECTOR,  "#flight0-product0")
            if elem.is_displayed():
                elem.click()  # this will click the element if it is there
                log.info("Alt CSS id detected")

        except NoSuchElementException:
            log.info("No alt id detected")
            selectFlightPage.lowestReturnPrice().click()

        wait.until(EC.element_to_be_clickable(selectFlightPage.statusPref()))
        selectFlightPage.statusPref().click()
        # ^^^^^may need to add an if statement here to accoutn for when this status check shows up??
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#button_continue_guest")))
        bookFlight = selectFlightPage.guestLogin()

        self.scrollDown()
        bookFlight.firstName().send_keys(getData["firstname"])
        bookFlight.lastName().send_keys(getData["lastname"])
        self.scrollDown()
        bookFlight.monthDropdown().select_by_index(1)
        bookFlight.dayDropdown().select_by_index(27)
        bookFlight.yearDropdown().select_by_index(30)










    @pytest.fixture(params=TripData.test_trip_data)
    def getData(self, request):
        return request.param