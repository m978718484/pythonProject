# -*- coding:utf-8 -*-

list_orgin = [
				[8,9],
				[8,7],
				[8,10],
				[10,11],
				[10,12],
				[7,6],
				[7,13],
				[6,5],
				[6,14],
				[6,15],
				[5,4],
				[5,16],
				[4,3],
				[3,2],
				[2,1],
				[1,0],
				[1,17],
			]
dict_leve_top = {}

def getNextLevel(temp_dict):
	for key in temp_dict.keys():
		for index,first_level in enumerate(temp_dict[key]):
			temp = {}
			for value in list_orgin:
				if first_level == value[0]:
					if value[0] not in temp.keys():
						temp[value[0]] = [value[1]]
					else:
						temp[value[0]].append(value[1])
			if temp:
				temp_dict[key][index] = temp
				getNextLevel(temp)

def getCount(item,key):
	if type(item) == dict:
		for key1 in item.keys():
			dict_count[key].append(len(item[key1]))
			for item1 in item[key1]:
				if type(item1) == dict:
					getCount(item1,key)


for _list in list_orgin:
	if _list[0] not in dict_leve_top.keys():
		dict_leve_top[_list[0]] = [_list[1]]
	else:
		dict_leve_top[_list[0]].append(_list[1])

getNextLevel(dict_leve_top)
# print dict_leve_top
# dict_count = {8:[3]}
# for item in dict_leve_top[8]:
# 	if type(item) == dict:
# 		getCount(item,8)

dict_count = {}

for key in dict_leve_top.keys():
	dict_count[key] = [len(dict_leve_top[key])]
	for item in dict_leve_top[key]:
		getCount(item,key)


print dict_count


# py273
# ------------------------------------------------------------------------------------------------------------------------
# import csv
# import pymssql

# #數據庫連接
# conn=pymssql.connect(host='10.134.158.111\MSSQL2008R',user='sa',password='Foxconn88',database='SharpScorecard')

# #打開游標
# cur=conn.cursor();

# if not cur:
#   raise Exception('數據庫連接失敗！')

# #4.修改數據

# reader=csv.reader(open(r'C:\Users\mayongfen\Desktop\test.csv','r'))
# for item in reader:
#   item = item[0].replace('\n','').split()[:5] # 獲取前五列
#   script = """insert into tb(T,P,SN,List,R) values ('{0}','{1}','{2}','{3}',{4})""".format(item[0],item[1],item[2],item[3],item[4])
#   print script
#   cur.execute(script)

# conn.commit() #修改數據後提交事務


# conn.close()

# ------------------------------------------------------------------------------------------------------------------------
# import math
# def checkNumber(number):
# 	b = number / 100
# 	y = number % 100
# 	s = y / 10
# 	g = y % 10

# 	if number == (pow(g,3)+pow(s,3) + pow(b,3)):
# 		return True
# 	else:
# 		return False


# for number in range(100,1000):
# 	if(checkNumber(number)):
# 		print number