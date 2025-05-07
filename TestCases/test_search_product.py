import datetime
import pytest
from PageObjects.search import search
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test006Search:
    base_url = ReadConfig.getApplicationurl()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()
    product='pink'

    def timestamp_module(self):
        self.timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S-%f")

    @pytest.mark.sanity
    def test_search_without_login(self,setup):
        self.logger.info("***** Test006Search *****")
        self.logger.info("***** Searching product without login *****")

        self.driver=setup
        self.driver.get(self.base_url)
        self.ps=search(self.driver)
        self.ps.clickproduct()
        self.ps.setsearch(self.product)
        self.ps.clicksearch()
        search_text_elements=self.ps.getsearchtextelements()
        search_text=[]
        for ele in search_text_elements:
            search_text.append(ele.text)
        self.count = 0
        for txt in search_text:
            if self.product in txt.lower():
                self.count+=1
            else:
                break

        if self.count==len(search_text):
            self.logger.info("***** Search without login Passed *****")
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(f".\\Screenshots\\test_Searchwithoutlogin_{self.timestamp}.png")
            self.logger.error("***** Search without login Failed *****")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_after_login(self, setup):
        self.logger.info("***** Searching product after login *****")
        self.driver = setup
        self.driver.get(self.base_url)
        #Login setup
        self.lp = LoginPage(self.driver)
        self.lp.clicksignup()
        self.lp.setemail(self.email)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.ps = search(self.driver)
        self.ps.clickproduct()
        self.ps.setsearch(self.product)
        self.ps.clicksearch()
        search_text_elements = self.ps.getsearchtextelements()
        search_text = []
        for ele in search_text_elements:
            search_text.append(ele.text)
        self.count = 0
        for txt in search_text:
            if self.product in txt.lower():
                self.count += 1
            else:
                break

        if self.count == len(search_text):
            self.logger.info("***** Search after login Passed *****")
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(f".\\Screenshots\\test_Searchafterlogin_{self.timestamp}.png")
            self.logger.error("***** Search after login Failed *****")
            self.driver.close()
            assert False




