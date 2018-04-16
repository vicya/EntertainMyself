#-*- coding: utf-8 -*-
#coding:utf-8
import sys
import json
import re

reload(sys)
sys.setdefaultencoding("utf-8")

fr = open('jayzhou.txt','r')

characters = []
count = {}


for line in fr:
	line = line.strip()
	if len(line) == 0:
		continue
	line = unicode(line)
	line = re.sub('[a-zA-Z]','',line)
	for x in xrange(0,len(line)):
		if line[x] in ['　','\n','\t',',','1','2','3','4','5','6','7','8','9','0','》','《','—','（','）',':','.',' ','~','！','\'','?','。','…','`','&','(',')','：','～']:
			continue
		if line[x] not in characters:
			characters.append(line[x])
		if not count.has_key(line[x]):
			count[line[x]] = 0
		count[line[x]] += 1
print len(characters)
print len(count)

count = sorted(count.items(),key=lambda d:d[1],reverse = True)
fw = open('result.txt','w')
for i in count:
	fw.write(i[0]+','+str(i[1])+'\n')

fp = open('result.txt','r')
for lines in fp:
	print lines