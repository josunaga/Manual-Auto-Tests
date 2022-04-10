import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class product_page():
    def __init__(self, driver):
        self.driver = driver

        self.loc_liv_electronica = "//*[@id='dept0']"

        self.loc_liv_closeLocation = "//*[@id='selectStore-modal']/div/div/div[1]/button/i"

        self.loc_liv_seeMore = "//*[@id='__next']/div[1]/div[1]/div/div[4]/aside/div/div/div[15]/div[2]/a"
        self.loc_liv_selectBrand = "//*[@id='__next']/div[1]/div[1]/div/div[4]/aside/div/div/div[15]/div[2]/div[2]/div[66]/label"
        self.loc_liv_clickBrand = "//*[@id='brand-LG']"

        self.loc_liv_resolutionTag = "//*[@id='__next']/div[1]/div[1]/div/div[4]/aside/div/div/div[16]/div[2]/div/div[1]/label"
        self.loc_liv_resolutionSelect = "//*[@id='dynamicFacets.resolucionvad-4K/Ultra HD']"

        self.loc_liv_sizeTag = "//*[@id='__next']/div[1]/div[1]/div/div[4]/aside/div/div/div[11]/div[2]/div/div[1]/label"
        self.loc_liv_sizeSelect = "//*[@id='variants.normalizedSize-65 pulgadas']"

    def close_location(self):
        try:
            time.sleep(1)
            elem = self.driver.find_element(By.XPATH, self.loc_liv_closeLocation)
            time.sleep(1)
            elem.click()
        except NoSuchElementException:
            pass

    def select_dep(self):
        self.driver.find_element(By.XPATH, self.loc_liv_electronica).click()

    def select_brand(self):
        self.driver.find_element(By.XPATH, self.loc_liv_seeMore).click()

        self.driver.find_element(By.XPATH, self.loc_liv_selectBrand)
        self.driver.find_element(By.XPATH, self.loc_liv_clickBrand).click()

    def select_resolution(self):
        self.driver.find_element(By.XPATH, self.loc_liv_resolutionTag)
        self.driver.find_element(By.XPATH, self.loc_liv_resolutionSelect).click()

    def select_size(self):
        self.driver.find_element(By.XPATH, self.loc_liv_sizeTag)
        self.driver.find_element(By.XPATH, self.loc_liv_sizeSelect).click()
