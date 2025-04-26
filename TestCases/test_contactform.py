import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from PageObjects.ContactForm import ContactForm
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import random
import string
from string import ascii_lowercase


def random_email(size=8, chars=ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class Test005Contactform:
    base_url = ReadConfig.getApplicationurl()
    path=ReadConfig.getuploadpath()
    logger = LogGen.loggen()

    def timestamp_module(self):
        self.timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S-%f")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_ContactForm(self,setup):
        self.logger.info("***** Test005Login *****")
        self.logger.info("***** Verifying Contact form *****")
        self.driver=setup
        self.driver.get(self.base_url)
        self.cf=ContactForm(self.driver)
        self.cf.clickcontactus()
        self.logger.info("***** Setting values for Contact form *****")
        self.cf.setname('Hariki')
        self.email = random_email() + '@gmail.com'
        self.cf.setemail(self.email)
        self.cf.setsubject('Enquiry')
        self.cf.setmessage('Need to enquire about the details in the file uploaded')
        self.cf.setfile(self.path)
        self.cf.clicksubmit()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.Simple_alert_window = self.driver.switch_to.alert
        self.Simple_alert_window.accept()
        act_conf=self.cf.submitconf()
        self.logger.info("***** Contact form validation starts *****")

        if act_conf=='Success! Your details have been submitted successfully.':
            self.logger.info("***** Contact form test passed successfully *****")
            self.cf.clickhome()
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(f".\\Screenshots\\test_Contactfrm_{self.timestamp}.png")
            self.logger.error("***** Contact form validation failed *****")
            self.cf.clickhome()
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_ContactFormwithoutemail(self, setup):
        self.logger.info("***** Verifying Contact form without email *****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.cf = ContactForm(self.driver)
        self.logger.info("***** setting Contact form without email *****")
        self.cf.clickcontactus()
        self.cf.clicksubmit()
        # Using Javascript to get the validation message as it's not a normal alert
        self.email_element=self.cf.getemailelement()
        validation_message = self.driver.execute_script("return arguments[0].validationMessage;", self.email_element)
        if 'Please fill' in validation_message:     ### Since the full alert message is different across browsers, checking the partial message here.
            assert True
            self.logger.info("***** Validation of Contact form without email completed successfully *****")
            self.driver.close()
        else:
            self.logger.error("***** Validation of Contact form without email failed *****")
            self.driver.save_screenshot(f".\\Screenshots\\test_Contactfrmwthoemail_{self.timestamp}.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_ContactFormwrongemail(self,setup):
        self.logger.info("***** Validating Contact form with incorrect email *****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.cf = ContactForm(self.driver)
        self.logger.info("***** Setting Contact form with incorrect email *****")
        self.cf.clickcontactus()
        #The below email is not having @gmail.com extension which is incorrect
        self.email = random_email()
        self.cf.setemail(self.email)
        self.cf.clicksubmit()
        # Using Javascript to get the validation message as it's not a normal alert
        self.email_element = self.cf.getemailelement()
        validation_message = self.driver.execute_script("return arguments[0].validationMessage;", self.email_element)
        if "Please include an '@'" in validation_message:  ### Since the full alert message is different across browsers, checking the partial message here.
            assert True
            self.logger.info("***** Validation of Contact form with incorrect email completed successfully *****")
            self.logger.info("***** Completing Test005Contactform ***** ")
            self.driver.close()
        else:
            self.logger.error("***** Validation of Contact form with wrong email failed *****")
            self.driver.save_screenshot(f".\\Screenshots\\test_Contactfrmwrngemail_{self.timestamp}.png")
            self.logger.error("***** Completing Test005Contactform ***** ")
            self.driver.close()
            assert False






