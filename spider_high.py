#-*- coding: utf-8 -*-
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


import json
import urllib
import urllib2
import json
from bs4 import BeautifulSoup
import jieba
import re
import requests
import time
import codecs

wonderful = []

fw =codecs.open('goodshop.txt','a',encoding='utf-8')
for i in xrange(1,51):
	shops = []
	url = 'http://www.dianping.com/shanghai/ch10/o2p'
	url = url + str(i)
	print url
	request = urllib2.Request(url = url)
	request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
	response = urllib2.urlopen(request,timeout = 20)
	result = response.read()
	html = BeautifulSoup(result)
	resultlist = html.find_all(name='a',attrs={'href':re.compile(('.'))})
	for x in xrange(0,len(resultlist)):
		cur = resultlist[x]['href'][0:38]
		if 'http://www.dianping.com/shop/' in cur:
			if cur not in shops:
				shops.append(cur)
	print len(shops)
	for url in shops:
		print url
		time.sleep(10)
		request = urllib2.Request(url = url)
		request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
		response = urllib2.urlopen(request,timeout = 20)
		print response
		result = response.read()
		print result
		# 使用BeautifulSoup解析html
		html = BeautifulSoup(result)
		print html
		
		shopname = []
		namelist = html.findAll('h1',{'class':'shop-name'})
		print 'namelist' + str(len(namelist))
		for x in namelist:
			s = x.get_text()
			s = s.strip()
			shopname.append(s[0:s.find(' ')])

		for x in shopname:
			print x
		resultlist = html.find_all(name='span', id = 'comment_score')
		for x in resultlist:
			print x
		scorelist = []
		flag = 0;
		for x in xrange(0,len(resultlist)):
			cur = resultlist[x].get_text()
			for i in xrange(0,3):
				score = float(cur[cur.find(':') + 1:cur.find(':') + 4])
				print score
				if score < 8.0:
					flag = 1
					break
				cur = cur[cur.find(':') + 4:]
			if flag == 0:
				if shopname[x] not in wonderful:
					fw.write(shopname[x] + '\n')
					wonderful.append(shopname[x])



	print len(wonderful)
