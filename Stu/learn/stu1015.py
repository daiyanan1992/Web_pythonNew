from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




#启动谷歌浏览器，开启对话
driver = webdriver.Chrome(service_log_path='D:\\chromedriver_service.log')
#访问百度网页
driver.get('https://www.juhe.cn/login?ref=https://dashboard.juhe.cn/home')

#窗口最大化
driver.maximize_window()

#EC.visibility_of_element_located初始化函数需要传元祖数据
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//input[@id="username"]')))
driver.find_element_by_xpath('//input[@id="username"]').send_keys('18018039181')
#输入密码
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//input[@id="password"]')))
driver.find_element_by_xpath('//input[@id="password"]').send_keys('huahua1002')
driver.find_element_by_id('loginBtn').click()



# driver.quit()