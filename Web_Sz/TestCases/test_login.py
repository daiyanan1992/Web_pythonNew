import unittest
from selenium import webdriver
from Web_Sz.PageObjects.login_page import LoginPage
from Web_Sz.PageObjects.index_page import IndexPage

class TestLogin(unittest.TestCase):

    def setUp(self):
        #前置访问页面
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.juhe.cn/login')
        self.lg = LoginPage(self.driver)




    def tearDown(self):
        self.driver.quit()

    #正常登录
    def test_login_success(self):
        #前置 访问登录页面
        #步骤 输入用户名密码点击登录
        self.lg.login('18018039181','huahua1002')
        #断言 首页当中是否找到什么元素
        self.assertTrue(IndexPage(self.driver).isExist_logout_ele())

  # 错误登录
    def test_login_success(self):
        #前置 访问登录页面
        #步骤 输入用户名密码点击登录
        self.lg.login('18018039181','huahua10021')
        #断言 首页当中是否找到什么元素
        self.assertTrue(self.lg.errorUserNameLoginEle())

