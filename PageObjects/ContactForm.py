from selenium.webdriver.common.by import By

class ContactForm:
    button_contactus_xpath='//*[@id="header"]/div/div/div/div[2]/div/ul/li[8]/a'
    textbox_name_xpath='//*[@id="contact-us-form"]/div[1]/input'
    textbox_email_xpath='//*[@id="contact-us-form"]/div[2]/input'
    textbox_subject_xpath='//*[@id="contact-us-form"]/div[3]/input'
    textbox_message_xpath='//*[@id="message"]'
    button_fileupload_xpath='//*[@id="contact-us-form"]/div[5]/input'
    button_submit_xpath='//*[@id="contact-us-form"]/div[6]/input'
    text_submitconf_xpath='//*[@id="contact-page"]/div[2]/div[1]/div/div[2]'
    button_home_xpath='//*[@id="form-section"]/a'

    def __init__(self,driver):
        self.driver=driver

    def clickcontactus(self):
        self.driver.find_element(By.XPATH,self.button_contactus_xpath).click()

    def setname(self,name):
        self.driver.find_element(By.XPATH,self.textbox_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_name_xpath).send_keys(name)

    def setemail(self,email):
        self.driver.find_element(By.XPATH,self.textbox_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)

    def getemailelement(self):
        return self.driver.find_element(By.XPATH, self.textbox_email_xpath)

    def setsubject(self,subject):
        self.driver.find_element(By.XPATH,self.textbox_subject_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_subject_xpath).send_keys(subject)

    def setmessage(self,message):
        self.driver.find_element(By.XPATH,self.textbox_message_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_message_xpath).send_keys(message)

    def setfile(self,path):
        self.driver.find_element(By.XPATH, self.button_fileupload_xpath).send_keys(path)

    def clicksubmit(self):
        self.driver.find_element(By.XPATH,self.button_submit_xpath).click()

    def submitconf(self):
        return self.driver.find_element(By.XPATH,self.text_submitconf_xpath).text

    def clickhome(self):
        self.driver.find_element(By.XPATH,self.button_home_xpath).click()
