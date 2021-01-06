#!/usr/bin/python

f=open('listall','r')
h=open('header','w')
m=open('all_merged','w')
capture=[4,5,2,3,16,17]
for file in f:
	file=file[:-1]
	dbsc=open(file,'r')
	count=0
	for line in dbsc:
		data='' #will be written on merged file
		cols=line[:-1].split('\t')
		for c in capture:
			data+='\t'+cols[c]
		data=data[1:]+'\n'
		if cols[0]=="chr":
			print('header check')
			h.write('chr(38)\tpos(38)')
			for item in data.split('\t')[2:]:
				h.write('\t'+item)
		elif len(data.split('\t')[0])>2 or data[0]=='.':
			count+=1
			continue
		else:
			m.write(data)
	dbsc.close()
	print(file+' done writing')
	print(str(count)+' unexpected chr name\n')
