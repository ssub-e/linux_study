#!/usr/bin/python
f=open('result730.txt','r')
numdict={}
for line in f:
	col=line[:-1].split('\t')
	for item in col:
		try:
			numdict[item]+=1
		except KeyError:
			numdict[item]=1
for i in range(45):
	print i+1,numdict[str(i+1)]

