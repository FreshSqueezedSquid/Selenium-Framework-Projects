from selenium.webdriver.common.by import By


class GuestPage:

    def __init__(self, driver):
        self.driver = driver

    guest_login = (By.CSS_SELECTOR, ".button-wrap")
    first_name = (By.XPATH, "//input[@id='firstName']")
    lastname = (By.XPATH, "//input[@id='lastName']")
    address = (By.CSS_SELECTOR, "#street")
    city = (By.CSS_SELECTOR, "#city")
    zipcode = (By.CSS_SELECTOR, "#zipcode")
    email = (By.XPATH, "//input[@id='user.emailAddress']")
    phone_num = (By.XPATH, "//input[@id='user.phone']")
    apply_details = (By.XPATH, " //button[@class='c-button c-button-secondary c-button-md new-address-form__button']")
    continue_to_payment = (By.XPATH, "//button[@class='btn btn-lg btn-block btn-secondary']")

    def guestLogin(self):
        return self.driver.find_element(*GuestPage.guest_login)

    def firstName(self):
        return self.driver.find_element(*GuestPage.first_name)

    def lastName(self):
        return self.driver.find_element(*GuestPage.lastname)

    def getAddress(self):
        self.driver.find_element(GuestPage.address)

    def getCity(self):
        return self.driver.find_element(*GuestPage.city)
    # need to enter a way to access a dropdown menu to select correct state abbreviation (i.e. AZ)

    def zipCode(self):
        return self.driver.find_element(*GuestPage.zipcode)