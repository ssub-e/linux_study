#!/usr/bin/python3
import random
rsp=['가위','바위','보']
wdl=[0,0,0]
wdlres=['Player win','Draw','Player lose']

while sum(wdl)<10:
<······>print('Round : '+str(sum(wdl)+1))
<······>player=''
<······>while len(player)==0:
<······><······>try:
<······><······><······>player=str(input('가위? 바위? 보? '))
<······><······><······>print('selected rsp : '+ player)
<······><······><······>ind=rsp.index(player)
<······><······>except:
<······><······><······>print('Input Error! Please enter proper value.')
<······><······><······>exit()
<······>c=random.randrange(0,3)
#<·····>ind=rsp.index(player)
<······>if c-ind==0:
<······><······>i=1

<······>elif abs(c-ind)==1:
<······><······>if c>ind:
<······><······><······>i=2
<······><······>else:
<······><······><······>i=0

<······>else:
<······><······>if c > ind:
<······><······><······>i = 2
<······><······>else:
<······><······><······>i = 0

<······>wdl[i] += 1
<······>print(wdlres[i])
<······>print('comp : ' + rsp[c])
<······>print('win : ' + str(wdl[0]) + ', draw : ' + str(wdl[1]) + ', lose : ' + str(wdl[2]) + '\n')

if wdl[0]>wdl[2]:
<······>result=wdlres[0]
elif wdl[0]==wdl[2]:
<······>result=wdlres[1]
else:
<······>result=wdlres[2]
print('Result : '+result)
