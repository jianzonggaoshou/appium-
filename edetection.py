# -*- coding: utf-8 -*-

from appium import webdriver
from time import sleep
import random

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0.2'
#desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.sito.edetection'
desired_caps['appActivity'] = '.view.login.LoginActivity'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# sleep(5)
# driver.find_element_by_id('edit_username').set_value('caishoujun')
# driver.find_element_by_id('edit_password').set_value('123456')
# driver.find_element_by_id('btn_signin').click()
# sleep(5)


# 开始项目
driver.find_element_by_id('menu').click()
sleep(1)
driver.find_element_by_id('downloadTaskIv').click()
sleep(1)
driver.find_element_by_id('md_buttonDefaultPositive').click()
sleep(1)

# driver.find_element_by_id('downloadTaskIv').click()
# sleep(1)
sleep(3)
driver.find_element_by_id('downloadTaskIv').click()

# 红外精确测温
sleep(1)
driver.find_element_by_id('text_name').click()

#检测记时开始按钮
sleep(1)
driver.find_element_by_id('off_report_tv').click()
sleep(1)
driver.find_element_by_id('md_buttonDefaultPositive').click()
sleep(1)

# 图片编号原始值
a = 1

for i in range(1, 6, 2):

	# ******************************************************************************************

	# 1* 设备数据输入
	sleep(1)
	el = driver.find_elements_by_id('layout_item')[i]
	el.click()

	# 第一条数据-本体
	sleep(1)
	el = driver.find_elements_by_id('editBtn')[0]
	el.click()

	# 红外图片编号
	sleep(1)
	el = driver.find_elements_by_id('edit')[1]
	el.set_value(a)

	# 正常图片编号
	sleep(1)
	el = driver.find_elements_by_id('edit')[2]
	el.set_value(a+1)

	# 最高温度
	sleep(1)
	el = driver.find_elements_by_id('edit')[3]
	el.set_value(random.randrange(10, 29))

	sleep(1)
	driver.find_element_by_id('saveTv').click()
	sleep(1)

	# (x,y, x,y, time)
	driver.swipe(500, 1500, 500, 500, 1000)
	sleep(3)

	# 第二条数据-冷却器
	sleep(1)
	el = driver.find_elements_by_id('editBtn')[1]
	el.click()

	# 红外图片编号
	sleep(1)
	el = driver.find_elements_by_id('edit')[1]
	el.set_value(a+2)

	# 正常图片编号
	sleep(1)
	el = driver.find_elements_by_id('edit')[2]
	el.set_value(a+3)

	# 最高温度
	sleep(1)
	el = driver.find_elements_by_id('edit')[3]
	el.set_value(random.randrange(30, 60))

	sleep(1)
	driver.find_element_by_id('saveTv').click()
	sleep(1)

	# 返回按键
	driver.find_element_by_class_name('android.widget.ImageButton').click()
	sleep(1)

	# 图片编号自增
	a = a + 4

#检测记时结束按钮
sleep(1)
driver.find_element_by_id('off_report_tv').click()
sleep(1)
driver.find_element_by_id('md_buttonDefaultPositive').click()
sleep(1)

# 上传数据
sleep(1)
driver.find_element_by_id('menu').click()
sleep(1)
driver.find_element_by_id('md_buttonDefaultPositive').click()
sleep(5)

# # (x,y, x,y, time)
# driver.swipe(500, 1500, 500, 500, 1000)
# sleep(3)

sleep(1)
driver.quit()