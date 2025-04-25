from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class RegisterUser:
    button_Signup_login_xpath = '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a'
    textbox_Name_xpath='//*[@id="form"]/div/div/div[3]/div/form/input[2]'
    textbox_email_xpath='//*[@id="form"]/div/div/div[3]/div/form/input[3]'
    button_Signup_xpath='//*[@id="form"]/div/div/div[3]/div/form/button'
    radio_title_Mr_xpath='//*[@id="id_gender1"]'
    radio_title_Mrs_xpath = '//*[@id="id_gender2"]'
    textbox_password_xpath='//*[@id="password"]'
    textbox_DOB_Date_xpath='//*[@id="days"]'
    textbox_DOB_Month_xpath = '//*[@id="months"]'
    textbox_DOB_Year_xpath = '//*[@id="years"]'
    checkbox_newsletter_xpath='//*[@id="newsletter"]'
    checkbox_offers_xpath='//*[@id="optin"]'
    textbox_Man_FN_xpath='//*[@id="first_name"]'
    textbox_Man_LN_xpath = '//*[@id="last_name"]'
    textbox_NonMan_Comp_xpath = '//*[@id="company"]'
    textbox_Man_Add1_xpath='//*[@id="address1"]'
    textbox_NonMan_Add2_xpath='//*[@id="address2"]'
    dropdown_country_xpath='//*[@id="country"]'
    textbox_Man_State_xpath='//*[@id="state"]'
    textbox_Man_City_xpath = '//*[@id="city"]'
    textbox_Man_Zipcode_xpath = '//*[@id="zipcode"]'
    textbox_Man_Mobile_xpath = '//*[@id="mobile_number"]'
    button_Create_xpath='//*[@id="form"]/div/div/div/div/form/button'
    button_Continue_xpath='//*[@id="form"]/div/div/div/div/a'
    button_Delete_xpath='//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a'
    button_logout_xpath='//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a'
    text_account_deleted_xpath='//*[@id="form"]/div/div/div/h2/b'

    def __init__(self,driver):
        self.driver=driver

    def clicksignuplogin(self):
        self.driver.find_element(By.XPATH,self.button_Signup_login_xpath).click()

    def setname(self,name):
        self.driver.find_element(By.XPATH,self.textbox_Name_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_Name_xpath).send_keys(name)

    def setemail(self,email):
        self.driver.find_element(By.XPATH,self.textbox_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)

    def clicksignup(self):
        self.driver.find_element(By.XPATH,self.button_Signup_xpath).click()

    def selectgender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.XPATH,self.radio_title_Mr_xpath).click()
        elif gender=='Female':
            self.driver.find_element(By.XPATH, self.radio_title_Mrs_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.radio_title_Mr_xpath).click()

    def setpassword(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def setdobdate(self,date):
        #self.driver.find_element(By.XPATH,self.textbox_DOB_Date_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_DOB_Date_xpath).send_keys(date)

    def setdobmonth(self,month):
        #self.driver.find_element(By.XPATH,self.textbox_DOB_Month_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_DOB_Month_xpath).send_keys(month)

    def setdobyear(self,year):
        #self.driver.find_element(By.XPATH,self.textbox_DOB_Year_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_DOB_Year_xpath).send_keys(year)

    def clicknewsletter(self):
        self.driver.find_element(By.XPATH, self.checkbox_newsletter_xpath).click()

    def clickoffers(self):
        self.driver.find_element(By.XPATH, self.checkbox_offers_xpath).click()

    def setfn(self,firstname):
        self.driver.find_element(By.XPATH,self.textbox_Man_FN_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_Man_FN_xpath).send_keys(firstname)

    def setln(self,lastname):
        self.driver.find_element(By.XPATH,self.textbox_Man_LN_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_Man_LN_xpath).send_keys(lastname)

    def setcompany(self,company):
        self.driver.find_element(By.XPATH,self.textbox_NonMan_Comp_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_NonMan_Comp_xpath).send_keys(company)

    def setaddress1(self,address1):
        self.driver.find_element(By.XPATH,self.textbox_Man_Add1_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_Man_Add1_xpath).send_keys(address1)

    def setaddress2(self,address2):
        self.driver.find_element(By.XPATH,self.textbox_NonMan_Add2_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_NonMan_Add2_xpath).send_keys(address2)

    def selectcountry(self,country):
        self.countries=Select(self.driver.find_element(By.XPATH,self.dropdown_country_xpath))
        self.countries.select_by_visible_text(country)

    def setstate(self,state):
        self.driver.find_element(By.XPATH,self.textbox_Man_State_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_Man_State_xpath).send_keys(state)

    def setcity(self,city):
        self.driver.find_element(By.XPATH,self.textbox_Man_City_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_Man_City_xpath).send_keys(city)

    def setzipcode(self,zipcode):
        self.driver.find_element(By.XPATH,self.textbox_Man_Zipcode_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_Man_Zipcode_xpath).send_keys(zipcode)

    def setmobile(self,mobile):
        self.driver.find_element(By.XPATH,self.textbox_Man_Mobile_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_Man_Mobile_xpath).send_keys(mobile)

    def clickcreate(self):
        self.driver.find_element(By.XPATH,self.button_Create_xpath).click()

    def clickcontinue(self):
        self.driver.find_element(By.XPATH,self.button_Continue_xpath).click()

    def clickdelete(self):
        self.driver.find_element(By.XPATH,self.button_Delete_xpath).click()

    def clicklogout(self):
        self.driver.find_element(By.XPATH,self.button_logout_xpath).click()

    def getdeletestatus(self):
        return self.driver.find_element(By.XPATH,self.text_account_deleted_xpath).text




