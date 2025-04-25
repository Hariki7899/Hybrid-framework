from selenium.webdriver.common.by import By
class LoginPage:
    button_Signup_xpath='//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a'
    textbox_Email_xpath='//*[@id="form"]/div/div/div[1]/div/form/input[2]'
    textbox_Password_xpath='//*[@id="form"]/div/div/div[1]/div/form/input[3]'
    button_Login_xpath='//*[@id="form"]/div/div/div[1]/div/form/button'
    text_loginname_xpath='//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a/b'
    button_Logout_xpath='//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a'

    def __init__(self,driver):
        self.driver=driver

    def clicksignup(self):
        self.driver.find_element(By.XPATH,self.button_Signup_xpath).click()

    def setemail(self,email):
        self.driver.find_element(By.XPATH, self.textbox_Email_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_Email_xpath).send_keys(email)

    def setpassword(self,password):
        self.driver.find_element(By.XPATH, self.textbox_Password_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_Password_xpath).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.button_Login_xpath).click()

    def getusername(self):
        return self.driver.find_element(By.XPATH,self.text_loginname_xpath).text

    def clicklogout(self):
        self.driver.find_element(By.XPATH,self.button_Logout_xpath).click()

