from selenium import webdriver

#启动谷歌浏览器，开启对话
driver = webdriver.Chrome(service_log_path='D:\\chromedriver_service.log')

#访问百度网页
driver.get('https://www.baidu.com/')

#窗口最大化
driver.maximize_window()

#方式一
ele = driver.find_element_by_id('s_kw_wrap')
# print(ele)

#方式二 class
ele2 = driver.find_element_by_class_name('s_ipt_wr')
driver.find_elements_by_class_name('s_ipt_wr')

#方式三name
driver.find_element_by_name('wd')
driver.find_elements_by_name('wd')

#方式四 tag_name
driver.find_element_by_tag_name('input')
driver.find_elements_by_tag_name('input')

#方式五 六 针对连接
driver.find_element_by_link_text('aa')
driver.find_element_by_partial_link_text('ss')

#xpath
driver.find_element_by_xpath("//span[@id='s-usersetting-top']")
'''
//标签名[@属性=值 and/or @属性=值]
分层定位
//标签名[@属性=值 and/or @属性=值]/标签名[@属性=值 and/or @属性=值]
'''

#结束会话
driver.quit()