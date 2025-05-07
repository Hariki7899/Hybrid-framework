from selenium.webdriver.common.by import By
class search:
    button_product_xpath='//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a'
    text_search_xpath='//*[@id="search_product"]'
    button_search_xpath='//*[@id="submit_search"]'
    text_searchtext_xpath='//div[@class="productinfo text-center"]//p'

    def __init__(self,driver):
        self.driver=driver

    def clickproduct(self):
        self.driver.find_element(By.XPATH,self.button_product_xpath).click()

    def setsearch(self,product):
        self.driver.find_element(By.XPATH,self.text_search_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_search_xpath).send_keys(product)

    def clicksearch(self):
        self.driver.find_element(By.XPATH, self.button_search_xpath).click()

    def getsearchtextelements(self):
        return self.driver.find_elements(By.XPATH,self.text_searchtext_xpath)
