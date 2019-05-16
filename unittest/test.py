import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from selenium.webdriver.support.ui import Select
import HtmlTestRunner
#from HTMLTestRunner import HTMLTestRunner

from reglog.Login import login1
from reglog.register import Register1

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/khan/Downloads/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_Register(self):
        driver = self.driver
        driver.get("http://www.gcrit.com/build3/create_account.php")

        reg = Register1(driver)
        reg.details1("Muhammad", "khan", "05-01-1990", "mymann@tutanota.com", "abc", "146, FORT YORK BLVD", "toronto", "M5V0E3", "Toronto", "ON")
        reg.details2("Canada", "6476560118")
        reg.enter_password("5190@MNABILK", "5190@MNABILK")
        reg.submit()

        log = login1(driver)
        log.Login("mymann@tutanota.com", "5190@MNABILK")
        log.sign_in()
        log.logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/khan/Desktop/run"),verbosity=2)


