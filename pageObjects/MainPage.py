from selenium.webdriver.common.by import By
from pageObjects.SearchPage import SearchPage


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    account = (By.XPATH, "//span[@class='v-p-right-xxs line-clamp']")
    sign_in = (By.CSS_SELECTOR, ".c-button.c-button-secondary.c-button-sm.sign-in-btn")
    search_txt = (By.XPATH, "//input[@id='gh-search-input']")
    search_bttn = (By.CSS_SELECTOR, ".header-search-button")



    def getAccount(self):
        return self.driver.find_element(*MainPage.account)



    def getSearchText(self):
        return self.driver.find_element(*MainPage.search_txt)



    def clickSearch(self):
        self.driver.find_element(*MainPage.search_bttn).click()
        searchPage = SearchPage(self.driver)
        return searchPage