from selenium import webdriver

#启动谷歌浏览器，开启对话
driver = webdriver.Chrome(service_log_path='D:\\chromedriver_service.log')

#访问百度网页
driver.get('https://www.baidu.com/')

#窗口最大化
driver.maximize_window()



#结束会话
driver.quit()