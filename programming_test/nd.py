#!/usr/bin/python
import random
alist=[]
for i in range(1000):
	a=0
	for j in range(100):
		if random.randint(0,1):
			a+=1
		else:
			a-=1
	alist.append(a)
	#print(a)
itemlist=[]
for item in alist:
	for l in range(1000):
		b=item+24
		c=item-24
		for k in range(100):
			if random.randint(0,1):
				b+=1
			else:
				b-=1
		for m in range(100):
			if random.randint(0,1):
				c+=1
			else:
				c-=1
		itemlist.append(b)
		itemlist.append(c)
		print(b)
		print(c)

