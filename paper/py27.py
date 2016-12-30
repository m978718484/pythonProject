#!/usr/bin/env python
#coding: utf-8

#https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver#required-configuration
import time
import csv

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.phantomjs.service import Service as IEDriverServer
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def	get_element_by_class_name(className):
	try:
		text = driver.find_element_by_class_name(className).text
		return text
	except:
		return ''


header = ['标题','作者','摘要','出版源','关键词','被引量']
with open("output.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerow(header)
lines = []
with open('test.txt','r') as f:
	lines = f.readlines()

for key in lines:	
	driver = driver=webdriver.Ie(executable_path=r'.\browser-driver\IEDriverServer')
	driver.get("http://xueshu.baidu.com/")
	time.sleep(3)

	driver.find_element_by_id("kw").send_keys(key)
	driver.find_element_by_id("su").click()
	author_text = get_element_by_class_name("author_text")
	if author_text  == '':
		time.sleep(5) #如果点查询没有直接跳到详情页，等待人为点选页面，这个时间你自己把控吧

	all_handles = driver.window_handles #获取窗口数
	author_text = None
	abstract = None
	kw_main = None
	sc_cite_cont = None
	if len(all_handles)>1:
		driver.switch_to_window(all_handles[1])#如果窗口数大于1,切换到新窗口

	span_more = driver.find_elements_by_tag_name("span")
	for span in span_more:
		if span.text == '更多':
			span.click()
			break
	title = driver.find_element_by_tag_name("h3").text
	author_text = get_element_by_class_name("author_text")
	abstract = get_element_by_class_name("abstract")
	publish_text = get_element_by_class_name("publish_text")
	kw_main = get_element_by_class_name("kw_main")
	try:
		sc_cite_cont = get_element_by_class_name("sc_cite_cont").text
	except:
		sc_cite_cont = 0	
	data = [[title,author_text,abstract,publish_text,kw_main,sc_cite_cont]]
	with open("output.csv", "a") as f:
		writer = csv.writer(f)
		writer.writerows(data)
	driver.quit()