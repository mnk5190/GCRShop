class login1():
    def __init__(self, driver):
        self.driver = driver

        # These are the three locators on this page
        self.email_address_xpath = "//input[@name='email_address']"
        self.enter_password_xpath = "//input[@name='password']"
        self.sign_in_xpath = "//span[contains(text(),'Sign In')]"
        self.logout_xpath = "//span[contains(text(),'Log Off')]"
        self.continue_xpath = "/span[contains(text(),'Continue')]"

    def Login (self, ea, password):
        self.driver.find_element_by_xpath(self.email_address_xpath).clear()
        self.driver.find_element_by_xpath(self.email_address_xpath).send_keys(ea)

        self.driver.find_element_by_xpath(self.enter_password_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_password_xpath).send_keys(password)

    def sign_in(self):

        self.driver.find_element_by_xpath(self.sign_in_xpath).click()

    def logout (self):

        self.driver.find_element_by_xpath(self.sign_in_xpath).click()
        self.driver.find_element_by_xpath(self.logout_xpath).click()
        self.driver.find_element_by_xpath(self.continue_xpath).click()