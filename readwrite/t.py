#!/usr/bin/env python
#coding: utf-8
import os
import os.path
rootdir = 'a'
f = open('out.txt','w')
for parent,dirnames,filenames in os.walk(rootdir):
	for filename in filenames:
		print "the full name of the file is:" + os.path.join(parent,filename)
		fopen = open(os.path.join(parent,filename), 'r')
		for eachLine in fopen:
			f.write('%s\n'%eachLine)
		fopen.close()
f.close()