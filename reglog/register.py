from selenium.webdriver.support.ui import Select

class Register1():
    def __init__(self, driver):
        self.driver = driver


        self.Gender_xpath = "/html[1]/body[1]/div[1]/div[3]/form[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/input[1]"
        self.firstname_xpath = "//input[@name='firstname']"
        self.lastname_xpath = " //input[@name='lastname']"
        self.dob_xpath = "//input[@id='dob']"
        self.input_email_xpath = "//input[@name='email_address']"

        self.company_xpath = "//input[@name='company']"
        self.Address_xpath = "//input[@name='street_address']"
        self.suburb_xpath = "//input[@name='suburb']"
        self.postcode_xpath = "//input[@name='postcode']"
        self.city_xpath = "//input[@name='city']"
        self.state_xpath = "//input[@name='state']"
        self.Countries_xpath = "//select[@name='country']"
        self.PhoneNumber_xpath = "//input[@name='telephone']"


        self.Password_xpath = "//input[@name='password']"
        self.Confirm_Password_xpath = "//input[@name='confirmation']"
        self.Continue_xpath = "//span[contains(text(),'Continue')]"



    def details1(self, firstname, lastname, dob, email, company, address, suburb, postcode, city, state):
        self.driver.find_element_by_xpath(self.Gender_xpath).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.firstname_xpath).clear()
        self.driver.find_element_by_xpath(self.firstname_xpath).send_keys(firstname)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.lastname_xpath).clear()
        self.driver.find_element_by_xpath(self.lastname_xpath).send_keys(lastname)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.dob_xpath).clear()
        self.driver.find_element_by_xpath(self.dob_xpath).send_keys(dob)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.input_email_xpath).clear()
        self.driver.find_element_by_xpath(self.input_email_xpath).send_keys(email)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.company_xpath).clear()
        self.driver.find_element_by_xpath(self.company_xpath).send_keys(company)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.Address_xpath).clear()
        self.driver.find_element_by_xpath(self.Address_xpath).send_keys(address)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.suburb_xpath).clear()
        self.driver.find_element_by_xpath(self.suburb_xpath).send_keys(suburb)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.postcode_xpath).clear()
        self.driver.find_element_by_xpath(self.postcode_xpath).send_keys(postcode)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.city_xpath).clear()
        self.driver.find_element_by_xpath(self.city_xpath).send_keys(city)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.state_xpath).clear()
        self.driver.find_element_by_xpath(self.state_xpath).send_keys(state)

    def details2 (self, country, phone):
        self.driver.implicitly_wait(5)
        Select(self.driver.find_element_by_xpath(self.Countries_xpath)).select_by_value(country)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.PhoneNumber_xpath).clear()
        self.driver.find_element_by_xpath(self.PhoneNumber_xpath).send_keys(phone)


    def enter_password(self, password, confirm_password):

        self.driver.find_element_by_xpath(self.Password_xpath).clear()
        self.driver.find_element_by_xpath(self.Password_xpath).send_keys(password)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.Confirm_Password_xpath).clear()
        self.driver.find_element_by_xpath(self.Confirm_Password_xpath).send_keys(confirm_password)

    def submit(self):

        self.driver.find_element_by_xpath(self.Continue_xpath).click()