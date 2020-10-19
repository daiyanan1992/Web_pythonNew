from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:

    #页面只需要传参即可，用例打开流量器就行
    def __init__(self,driver):
        self.driver = driver

    #登录
    def login(self,username,passwd):
        name_text = '//input[@id="username"]'
        pwd_text = '//input[@id="password"]'
        login_button = '//input[@id="loginBtn"]'
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,name_text)))
        self.driver.find_element_by_xpath(name_text).send_keys(username)
        self.driver.find_element_by_xpath(pwd_text).send_keys(passwd)
        self.driver.find_element_by_xpath(login_button).click()

    #登录空用户名
    def isUserNameLoginEle(self):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//em[text()="请输入正确格式的用户名!"]')))
            return True
        except:
            return False
    #错误用户名及密码
    def errorUserNameLoginEle(self):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//em[text()="登录失败,请确认账号和密码正确"]')))
            return True
        except:
            return False
    #注册
    def register(self):
        pass

    #忘记密码