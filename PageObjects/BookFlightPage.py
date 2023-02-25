from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BookFlight:

    def __init__(self, driver):
        self.driver = driver

    firstname = (By.XPATH, "//div/input[@id='passengers0.personalInformationForm.firstName']")
    lastname = (By.XPATH, "//div/input[@id='passengers0.personalInformationForm.lastName']")
    month_dropdown = (By.XPATH, "//select[@id='passengers0.dateComponentForm.month']")
    day_dropdown = (By.XPATH, "//select[@id='passengers0.dateComponentForm.day']")
    year_dropdown = (By.XPATH, "//select[@id='passengers0.dateComponentForm.year']")
    gender_dropdown = (By.XPATH, "//select[@id='passengers0.personalInformationForm.gender']")
    region_dropdown = (By.XPATH, "//select[@id='passengers0.residencyInfo.country']")
    email = (By.XPATH, "//input[@id='tripContact.email']")
    conf_email = (By.XPATH, "//input[@id='confirmEmail']")
    country_code_dropdown = (By.XPATH, "//div[@class='selectbox-overlay']")
    phone_num = (By.XPATH, "//input[@id='tripContact.phones0.number']")
    passenger_button = (By.XPATH, "//button[@id='passenger_button']")

    def firstName(self):
        return self.driver.find_element(*BookFlight.firstname)

    def lastName(self):
        return self.driver.find_element(*BookFlight.lastname)

    def monthDropdown(self):
        return Select(self.driver.find_element(*BookFlight.month_dropdown))

    def dayDropdown(self):
        return Select(self.driver.find_element(*BookFlight.day_dropdown))

    def monthDropdown(self):
        return Select(self.driver.find_element(*BookFlight.month_dropdown))

    def yearDropdown(self):
        return Select(self.driver.find_element(*BookFlight.year_dropdown))

    def genderDropdown(self):
        return Select(self.driver.find_element(*BookFlight.gender_dropdown))

    def regionDropdown(self):
        return Select(self.driver.find_element(*BookFlight.region_dropdown))

    def getEmail(self):
        return self.driver.find_element(*BookFlight.email)

    def codeDropdown(self):
        return Select(self.driver.find_element(*BookFlight.country_code_dropdown))

    def phoneNum(self):
        return self.driver.find_element(*BookFlight.phone_num)

    def passengerButton(self):
        return self.driver.find_element(*BookFlight.passenger_button)