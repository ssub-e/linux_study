#!/usr/bin/python
import sys
f=open(sys.argv[1],'r')
r=open(sys.argv[1]+'_tab.txt','w')
check=1
for line in f:
	if check:
		r.write(line[:-1]+'\t')
	else:
		r.write(line)
	check=1-check

