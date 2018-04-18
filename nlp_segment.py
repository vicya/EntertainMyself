#-*- coding: utf-8 -*-
#coding:utf-8
import sys
import json
import re

reload(sys)
sys.setdefaultencoding("utf-8")

fr = open('nlpzhoujay.txt','r')

characters = []
count = {}


for line in fr:
	line = line.strip()
	if len(line) == 0:
		continue
	line = unicode(line)
	line = re.sub('[0-9a-zA-Z]','',line)
	word = line.split('"')
	for x in xrange(0,len(word)):
		word[x] = word[x].strip()
		if word[x] in ['\n','\t',',','》','《','—','（','）',':','.',' ','~','！','\'','?','。','…','`','&','(',')','：','～',', ','',': ',' (']:
			continue
		if word[x] not in characters:
			characters.append(word[x])
		if not count.has_key(word[x]):
			count[word[x]] = 0
		count[word[x]] += 1
print len(characters)
print len(count)
count = sorted(count.items(),key=lambda d:d[1],reverse = True)
fw = open('result.txt','w')
for i in count:
	fw.write(i[0]+','+str(i[1])+'\n')

fp = open('result.txt','r')
for lines in fp:
	print lines