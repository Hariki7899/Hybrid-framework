import pytest

from PageObjects.RegisterUser import RegisterUser
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

class Test003Registeruser:
    base_url = ReadConfig.getApplicationurl()
    logger = LogGen.loggen()
    email=ReadConfig.getemail()

    def timestamp_module(self):
        self.timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S-%f")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_adduser(self,setup):
        self.timestamp_module()
        self.logger.info("***** Test003Registeruser *****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.reguser=RegisterUser(self.driver)
        ## Start filling form ##
        self.reguser.clicksignuplogin()
        self.logger.info("***** Starting user registration *****")
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
        self.logger.info("***** Saving Customer details *****")
        self.reguser.clickcreate()
        self.logger.info("***** Registration validation starts *****")
        act_title=self.driver.title

        if act_title=='Automation Exercise - Account Created':
            self.logger.info("***** User Registration passed successfully *****")
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(f".\\Screenshots\\test_adduser_{self.timestamp}.png")
            self.logger.error("******* User Registration Failed *******")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_dltuser(self,setup):
        self.timestamp_module()
        self.logger.info("***** User deletion process *****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.reguser=RegisterUser(self.driver)
        ## Start filling form ##
        self.reguser.clicksignuplogin()
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
        self.reguser.clickcreate()
        self.logger.info("***** Saving Customer details *****")
        self.reguser.clickcontinue()
        self.logger.info("***** User deletion process starts *****")
        self.reguser.clickdelete()
        act_status=self.reguser.getdeletestatus()

        if act_status == 'ACCOUNT DELETED!':
            self.logger.info('***** Deletion of user completed successfully *****')
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(f".\\Screenshots\\test_dltuser_{self.timestamp}.png")
            self.logger.error('***** Deletion of user Failed *****')
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_regexuser(self,setup):
        self.timestamp_module()
        self.logger.info("***** User deletion process *****")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.base_url)
        self.reguser = RegisterUser(self.driver)
        ## Start filling form ##
        self.reguser.clicksignuplogin()
        self.reguser.setname('Hariki')
        ##Using the already existing registered email form read config file
        self.reguser.setemail(self.email)
        self.reguser.clicksignup()
        act_status=self.reguser.getemailexistingstatus()

        if act_status=='Email Address already exist!':
            self.logger.info('***** Validation with existing email completed successfully *****')
            self.logger.info("***** Ending Test003Registeruser *****")
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(f".\\Screenshots\\test_refexuser_{self.timestamp}.png")
            self.logger.error('***** Validation with existing email failed *****')
            self.logger.info("***** Ending Test003Registeruser *****")
            self.driver.close()
            assert False




