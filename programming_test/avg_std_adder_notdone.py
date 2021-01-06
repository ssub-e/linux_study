#!/usr/bin/python
import sys
f=open(sys.argv[1],'r')
r=open(sys.argv[1]+'_result.txt','w')

region=[]

for line in f:
	col=line[:-1].split('\t')
	if line[0]=='#':
		region=[[]for i in range(len(col))]
		r.write(line+'\n')
	else:
		for i in range(len(col)):
			try:
				region[i].append(int(col[i]))
			except ValueError:
				region[i].append(col[i])

medians=[]
std=[]
for i in range(4,len(col)):
	sample=[]
	for j in range(len(region[i])):
		sample.append(region[i][j])
	sample.sort()
	median=(sample[len(sample)/2] + sample[(len(sample)-1/2]) /2.00
	medians.append(median)

r.write('#chr\tstart\tend\tgene')
for i in range(len(col)-4):
	r.write('\tsample'+str(i+1)
r.write('\tavg\n')

for i in range(

#print(region)
