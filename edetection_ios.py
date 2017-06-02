# -*- coding: UTF-8 -*-

from time import sleep
from appium import webdriver
import random

desired_caps = {}

desired_caps['automationName'] = 'XCUITest'

desired_caps['platformName'] = 'iOS'

desired_caps['platformVersion'] = '10.3'

desired_caps['bundleId'] = 'com.sitop.edetection'

# desired_caps['app'] = os.path.abspath('/Users/xuzhen/edetection.app')

desired_caps['noReset'] = True

desired_caps['deviceName'] = 'iphone Simulator'

# desired_caps['deviceName'] = 'iPhone 6'

# desired_caps['udid'] = '64a226e1f1e8b3548688ebeee60fc51730ad4d54'

dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

sleep(3)

# 开始按钮
el = dr.find_element_by_id('nav start normal')
el.click()

sleep(3)
# 开始项目
el = dr.find_elements_by_id('开始')[0]
el.click()
sleep(3)
el = dr.find_element_by_id('确定')
el.click()

sleep(3)

# 下载
el = dr.find_elements_by_id('下载')[0]
el.click()
sleep(3)
el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[1]')
el.click()

sleep(3)
# 测试项
el = dr.find_element_by_id('1.红外精确测温')
el.click()

sleep(3)
# 点击开始检测
el = dr.find_element_by_id('点击开始检测')
el.click()
sleep(1)
el = dr.find_element_by_id('确定')
el.click()

# 图片编号原始值
a = 1

for i in range(2, 9, 3):

	sleep(3)
	# 间隔检测
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[3]//*[%s]' % i)

	el.click()

	sleep(1)

	# 添加数据
	# 本体
	el = dr.find_elements_by_id('editor icon normal')[0]
	el.click()
	sleep(3)

	# 红外图片编号
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[1]//*[3]')
	el.set_value(str(a))

	# 正常图片编号
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[1]//*[4]')
	el.set_value(str(a + 1))

	# # 最高温度
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[2]//*[2]')
	el.set_value(str(random.randrange(28, 38)))
	sleep(3)
	# 保存
	el = dr.find_element_by_id('保存')
	el.click()

	# noinspection PyBroadException
	try:
		sleep(3)
		el = dr.find_element_by_id('确定')
		el.click()

	except:
		print '温度异常'

	sleep(3)
	# 冷却器
	el = dr.find_elements_by_id('editor icon normal')[1]
	el.click()
	sleep(3)

	# 红外图片编号
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[1]//*[3]')
	el.set_value(str(a + 2))

	# 正常图片编号
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[1]//*[4]')
	el.set_value(str(a + 3))

	# 最高温度
	el = dr.find_element_by_xpath('//*[1]//*[1]//*[1]//*[1]//*[1]//*[1]//*[2]//*[1]//*[1]//*[2]//*[2]//*[2]//*[2]')
	el.set_value(str(random.randrange(28, 38)))

	sleep(3)
	# 保存
	el = dr.find_element_by_id('保存')
	el.click()

	# noinspection PyBroadException
	try:
		sleep(3)
		el = dr.find_element_by_id('确定')
		el.click()

	except:
		print '温度异常'

	# 返回上一界面
	sleep(3)
	el = dr.find_element_by_id('back icon normal')
	el.click()

	# 自增+4
	sleep(3)
	a = a + 4
	sleep(1)

sleep(3)
# 点击完成检测
el = dr.find_element_by_id('点击完成检测')
el.click()
sleep(1)
el = dr.find_element_by_id('确定')
el.click()

sleep(3)
# 上传数据
el = dr.find_element_by_id('上传')
el.click()

sleep(8)
dr.quit()
