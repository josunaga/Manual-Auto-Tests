from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from POMdemo.Pages.homePage import home_page
from POMdemo.Pages.productPage import product_page
import HtmlTestRunner


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\WebDrivers\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_advanced_search(self):
        driver = self.driver

        driver.get("https://www.liverpool.com.mx/tienda/home")  # URL

        homepage = home_page(driver)
        homepage.enter_search("Smart Tv")
        homepage.click_search()

        productpage = product_page(driver)
        productpage.close_location()
        time.sleep(1)
        productpage.select_dep()
        time.sleep(1)
        productpage.select_brand()
        time.sleep(1)
        productpage.select_resolution()
        time.sleep(1)
        productpage.select_size()

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/jesus/Desktop/AdvancedSearchSelinium/Reports'))