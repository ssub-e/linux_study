#!/usr/bin/python
import sys
f=open(sys.argv[1],'r')

sams=[]
for item in f:
	try:
		sams.append(int(item))
	except ValueError:
		pass

sams.sort()
median= (sams[len(sams)/2] + sams[(len(sams)-1)/2] ) /2.00
print('median : '+str(median))

#normalize
norm=[]
mean=0
for item in sams:
	norm.append(item/median)
	mean+=item/median
mean/=len(norm)
print('mean : '+str(mean))

#standard deviation
std=0
for item in norm:
	std+=(item-mean)**2
std=(std/len(norm))**0.5

print('std : '+str(std))

