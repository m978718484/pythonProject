#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #需要引入keys包
import os,time

lines = []
with open('test.txt','r') as f:
	lines = f.readlines()

for line in lines:	
	driver = driver=webdriver.Ie()
	driver.get("http://xueshu.baidu.com/")
	time.sleep(3)
	driver.maximize_window() # 浏览器全屏显示

	driver.find_element_by_id("kw").send_keys('MultipleCorrelated   Antennas over Nakagami Fading Channel')
	driver.find_element_by_id("su").click()
	next_step = input('是否已经点选(y/n)')
	if next_step == 'y':
		all_handles = driver.window_handles
		if len(all_handles)>1:
			driver.switch_to_window(all_handles[1])
		author_text = driver.find_element_by_class_name("author_text")
		abstract = driver.find_element_by_class_name("abstract")
		span_more = driver.find_element_by_tag_name("span")
		print(author_text.text)

	driver.quit()
	# author_text = driver.find_element_by_class_name("author_text")

	# if author_text:
	# 	author_text.click()
	# else:
	# 	driver.quit()