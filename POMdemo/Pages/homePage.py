import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class home_page():

    def __init__(self, driver):
        self.driver = driver

        self.loc_liv_searchBar = "//*[@id='mainSearchbar']"
        self.loc_liv_searchBarButton = "//button[contains(@class, 'input-group-text')]"

    def enter_search(self, product):
        self.driver.find_element(By.XPATH, self.loc_liv_searchBar).send_keys(product)

    def click_search(self):
        self.driver.find_element(By.XPATH, self.loc_liv_searchBarButton).click()


