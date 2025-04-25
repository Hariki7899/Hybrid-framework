import pytest

from PageObjects.RegisterUser import RegisterUser
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import datetime
import random
import string
from string import ascii_letters, ascii_lowercase

## Creating random email for testing purpose.
def random_email(size=8,chars= ascii_lowercase+ string.digits):
    return ''.join(random.choice(chars) for x in range(size))

## Crating random password for testing purpose.
def random_password(size=10,chars= ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for x in range(size))

class Test004Logout:
    base_url = ReadConfig.getApplicationurl()
    logger = LogGen.loggen()


    def timestamp_module(self):
        self.timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S-%f")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_logout(self,setup):
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.timestamp_module()
        self.logger.info("***** Test004Logout *****")
        self.driver.get(self.base_url)
        self.reguser=RegisterUser(self.driver)
        ## Start filling form ##
        self.reguser.clicksignuplogin()
        self.logger.info("***** Starting user registration for logout validation *****")
        self.reguser.setname('Hariki')
        ## Generating random email and setting that email.
        self.email = random_email() + '@gmail.com'
        self.reguser.setemail(self.email)
        self.reguser.clicksignup()
        self.reguser.selectgender('Male')
        ## Generating random password and setting that password.
        self.password= random_password()
        self.reguser.setpassword(self.password)
        self.reguser.setdobdate('07')
        self.reguser.setdobmonth('August')
        self.reguser.setdobyear('1999')
        self.reguser.clicknewsletter()
        self.reguser.clickoffers()
        self.reguser.setfn('Hari')
        self.reguser.setln('Ki')
        self.reguser.setcompany('Aon')
        self.reguser.setaddress1('No9, Murugan nagar')
        self.reguser.setaddress2('Pozhichalur, Chennai.')
        self.reguser.selectcountry('India')
        self.reguser.setstate('Tamil Nadu')
        self.reguser.setcity('Chennai')
        self.reguser.setzipcode('600074')
        self.reguser.setmobile('6282586199')
        self.logger.info("***** Saving Customer details for logout validation *****")
        self.reguser.clickcreate()
        self.reguser.clickcontinue()
        self.reguser.clicklogout()
        self.logger.info("***** Starting Logout process *****")

        self.lp = LoginPage(self.driver)
        self.lp.setemail(self.email)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.reguser.clicklogout()
        act_title=self.driver.title

        if act_title=='Automation Exercise - Signup / Login':
            self.logger.info("***** User Logout passed successfully *****")
            self.logger.info("***** Ending Test004Logout *****")
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(f".\\Screenshots\\test_logout_{self.timestamp}.png")
            self.logger.error("******* User Logout Failed *******")
            self.logger.info("***** Ending Test004Logout *****")
            self.driver.close()
            assert False