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
# from selenium.webdriver.common.by import By
#
# class LoginPageLocators:
#     name_text = (By.XPATH,'//input[@id="username"]')
# print(*LoginPageLocators.name_text)

# 截图方式二
# coding=utf-8
from selenium import webdriver
import time
from datetime import datetime
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
time.sleep(2)
try:
    # driver.save_screenshot('.\\baidu1.png')
    # print("%s ：截图成功！！！" % picture_url
# )
    file_name ='D:\\Web_pythonNew\\Web_Sz\\Outputs\\screenshots\\{0}_{1}.png'.format('daiy')
    print(file_name)
    str = datetime.now()
    print(str+type(str))

    driver.save_screenshot(file_name)
except BaseException as msg:
    print("%s ：截图失败！！！" % msg)
driver.quit()