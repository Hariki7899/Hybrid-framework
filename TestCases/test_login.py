import datetime

import pytest

from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test001Login:
    base_url = ReadConfig.getApplicationurl()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    def timestamp_module(self):
        self.timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S-%f")

    @pytest.mark.sanity
    def test_HomePageTitle(self, setup):
        self.logger.info("***** Test001Login *****")
        self.logger.info("***** Verifying Home Page Title *****")

        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title

        if act_title == 'Automation Exercise':
            self.logger.info("***** Home Page title case passed *****")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(f".\\Screenshots\\test_HomePageTitle_{self.timestamp}.png")
            self.logger.error("******* Home Page title case failed *******")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("***** Verifying Login test *****")

        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.clicksignup()
        self.lp.setemail(self.email)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_username = self.lp.getusername()

        if act_username == 'Hari Krishnan V':
            self.logger.info("***** Login test passed successfully *****")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(f".\\Screenshots\\test_Login_{self.timestamp}.png")
            self.logger.error("******* Login test failed *******")
            self.driver.close()
            assert False
