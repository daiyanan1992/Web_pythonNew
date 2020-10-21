from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#启动谷歌浏览器，开启对话
driver = webdriver.Chrome(service_log_path='D:\\chromedriver_service.log')
#访问百度网页
driver.get('https://www.baidu.com/')


#窗口最大化
driver.maximize_window()
#
# #找到鼠标要操作的元素
# ele = driver.find_element_by_id('s_kw_wrap')
# #实例化ActionChaina
# ac = ActionChains(driver)
# #将鼠标添加到action列表中
# ac.move_to_element(ele).perform()


from selenium.webdriver.support.ui import Select

#找到select元素
#实例化select类
#选择下拉列表值方式一：下标来选择  方式二：value值 方式三：文本值

from selenium.webdriver.common.keys import Keys

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//input[@id="kw"]')))
driver.find_element_by_id('kw').send_keys('python',Keys.ENTER)

# ele = driver.find_element_by_xpath('//*[@id="3002"]/div[1]/h3/a')
# print(ele)
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//a[contains(text()," 基础教程 | 菜鸟教程")]')))
# driver.find_element_by_xpath('//*[@id="3002"]/div[1]/h3/a').click()
# driver.execute_script('arguments[0].scrollIntoView(false);','//a[contains(text()," 基础教程 | 菜鸟教程")]')
driver.execute_script("arguments[0].scrollIntoView();", '//a[contains(text()," 基础教程 | 菜鸟教程")]')
driver.window_handles
driver.switch_to.window()
# driver.quit()