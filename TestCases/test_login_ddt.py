import datetime
import time

import pytest

from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils

class Test002DDTLogin:
    base_url = ReadConfig.getApplicationurl()
    path='.//TestData/LoginData.xlsx'
    ##email and password not needed. Will be fetched form excel
    #email = ReadConfig.getemail()
    #password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    def timestamp_module(self):
        self.timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S-%f")

    @pytest.mark.regression
    def test_Login_ddt(self, setup):
        self.logger.info("***** Test002DDTLogin *****")
        self.logger.info("***** Verifying Login test-DDT *****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.clicksignup()

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in the excel:",self.rows)

        list_status=[]

        for r in range(2,self.rows+1):
            self.email=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp=XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setemail(self.email)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title='Automation Exercise'

            if act_title==exp_title:
                if self.exp=='Pass':
                    self.logger.info("***** Passed *****")
                    self.lp.clicklogout()
                    list_status.append("Pass")
                elif self.exp=='Fail':
                    self.logger.error("***** Failed *****")
                    self.lp.clicklogout()
                    list_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp=='Pass':
                    self.logger.error("***** Failed *****")
                    self.lp.clicklogout()
                    list_status.append("Fail")
                elif self.exp=='Fail':
                    self.logger.info("***** Passed *****")
                    self.lp.clicklogout()
                    list_status.append("Pass")

        if 'Fail' not in list_status:
            self.logger.info('*****Login DDT is passed *****')
            self.driver.close()
            assert True
        else:
            self.logger.error('*****Login DDT is failed *****')
            self.driver.close()
            assert False


        self.logger.info('******** End of Login DDT Test ********')
        self.logger.info('******** Completed Test002DDTLogin ******** ')
