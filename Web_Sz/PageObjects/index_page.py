from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Web_Sz.PageLocators.myapi_locators import MyApiLocators as mal


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

    #点击个人api
    def user_centor(self,men,women):
        #点击我的-个人中心
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(mal.user_centor))
        self.driver.find_element(*mal.user_centor).click()
        #点击我的api进入
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(mal.data_centor))
        self.driver.find_element(*mal.data_centor).click()
        self.driver.find_element(*mal.user_centor_api).click()
        #点击生肖配对接口
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(mal.shengxiao_but))
        self.driver.find_element(*mal.shengxiao_but).click()
        #获取窗口句柄
        handles = self.driver.window_handles
        #切换到最新的窗口句柄
        self.driver.switch_to.window(handles[-1])
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(mal.shengxiao_men_but))
        self.driver.find_element(*mal.shengxiao_men_but).send_keys(men)
        self.driver.find_element(*mal.shengxiao_women_but).send_keys(women)
        self.driver.find_element(*mal.ceshi_but).click()
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(mal.res_data))
        res = self.driver.find_element(*mal.res_data).text
        print(res)






