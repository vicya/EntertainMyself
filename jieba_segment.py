#-*- coding: utf-8 -*-
#coding:utf-8
##jieba
import sys
import json
import re
import jieba
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
	line = re.sub('[0-9a-zA-Z]','',line)
	seglist = jieba.lcut(line)
	for x in xrange(0,len(seglist)):
		if seglist[x] in ['　','\n','\t',',','》','《','—','（','）',':','.',' ','~','！','\'','?','。','…','`','&','(',')','：','～']:
			continue
		if seglist[x] not in characters:
			characters.append(seglist[x])
		if not count.has_key(seglist[x]):
			count[seglist[x]] = 0
		count[seglist[x]] += 1
print len(characters)
print len(count)

count = sorted(count.items(),key=lambda d:d[1],reverse = True)
fw = open('jiebaresult.txt','w')
for i in count:
	fw.write(i[0]+','+str(i[1])+'\n')

fp = open('jiebaresult.txt','r')
for lines in fp:
	print lines
