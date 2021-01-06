#!/usr/bin/python
import random
alist=[]

for j in range(100):
	a=0
	for i in range(100):
		if random.randint(0,1):
			a+=1
		else:
			a-=1
	alist.append(a)
	print(a)

