import unittest
from selenium import webdriver
from Web_Sz.PageObjects.login_page import LoginPage
from Web_Sz.PageObjects.index_page import IndexPage
from Web_Sz.TestDatas import Common_Datas as CD
from Web_Sz.TestDatas import login_datas as LD
from ddt import ddt,data,unpack


@ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        #前置访问页面
        self.driver = webdriver.Chrome()
        self.driver.get(CD.web_login_url)
        self.driver.maximize_window()
        self.lg = LoginPage(self.driver)




    def tearDown(self):
        self.driver.quit()

    #正常登录
    def test_login_success(self):
        #前置 访问登录页面
        #步骤 输入用户名密码点击登录
        self.lg.login(LD.success_data['user'],LD.success_data['passwd'])
        #断言 首页当中是否找到什么元素
        self.assertTrue(IndexPage(self.driver).isExist_logout_ele())

  # 错误登录
    @data(*LD.phone_data)
    def test_login_success(self,data):
        #前置 访问登录页面
        #步骤 输入用户名密码点击登录
        self.lg.login(data['user'],data['passwd'])
        #断言 首页当中是否找到什么元素
        # self.assertTrue(self.lg.errorUserNameLoginEle())
        self.assertEqual(self.lg.errorUserNameLoginEle(),data['check'])
