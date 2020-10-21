# import unittest
# from ddt import ddt,data,unpack
#
# phone_data = [
#     {'user':'180180391811','passwd':'huahua1002','check':'登录失败,请确认账号和密码正确'},
#     {'user':'1801803918','passwd':'huahua1002','check':'请输入正确格式的用户名!'},
#     {'user':'', 'passwd': 'huahua1002', 'check': '请输入正确格式的用户名!'},
#     {'user':'18018039181', 'passwd': 'huahua10021', 'check': '登录失败,请确认账号和密码正确'},
# ]
#
#
# @ddt
# class MyTesting(unittest.TestCase):
#     def setUp(self):
#         print('this is the setUp')
#
#
#     @data(*phone_data)
#     def test_1(self,value):
#         print(value['user']+value['passwd']+value['check'])
#
#
#
#
#
#     def tearDown(self):
#         print('this is tearDown')
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
from selenium.webdriver.common.by import By

class LoginPageLocators:
    name_text = (By.XPATH,'//input[@id="username"]')
print(*LoginPageLocators.name_text)