from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class IndexPage:

    def __init__(self,driver):
        self.driver = driver

    def isExist_logout_ele(self):
        #找到退出按钮就返回TRue
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//a[@class="account-logout"]')))
            return True
        except:
            return False



