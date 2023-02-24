import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.FlightFinderPage import FlightFinder
from TestData.TripData import TripData
from utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC


class TestAA(BaseClass):

    def test_flightBooking(self, getData):

        log = self.getLog()
        wait = WebDriverWait(self.driver, 7)
        time.sleep(1.5)

        # initializes driver clicks button to take us to login page
        flightFinderPage = FlightFinder(self.driver)
        flightFinderPage.cookieWarning().click()
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
        #wait.until(EC.element_to_be_clickable(selectFlightPage.closePopUp()))
        #selectFlightPage.closePopUp().click()
        self.scrollDown()
        wait.until(EC.element_to_be_clickable(selectFlightPage.lowestPricedFlight()))
        selectFlightPage.lowestPricedFlight().click()
        time.sleep(1.8)
        wait.until(EC.element_to_be_clickable(selectFlightPage.lowestPricedFlight()))
        self.scrollDown()
        time.sleep(2)
        selectFlightPage.lowestPricedFlight().click()
        #wait.until(EC.element_to_be_clickable(selectFlightPage.statusPref()))
        #selectFlightPage.statusPref().click()
        # ^^^^^may need to add an if statement here to accoutn for when this status check shows up??
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1.5)
        wait.until(EC.element_to_be_clickable(selectFlightPage.guestLogin()))
        time.sleep(3)
        selectFlightPage.guestLogin().click()

        # ^^^^still need to confirm/book the flight, adn then submit payment info!!!!!









    @pytest.fixture(params=TripData.test_trip_data)
    def getData(self, request):
        return request.param