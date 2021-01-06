#!/usr/bin/python
import os
import sys
import random
import time
from colorama import init, Fore, Back, Style
init()

maze=[]
visit=[]
culist=[]

for y in range(400):
	if random.randint(1,4)==1:
		maze.append('b')
	else:
		maze.append('w')
	visit.append(0)

maze[0]='g'
maze[-1]='g'
visit[0]=1
try:
	if sys.argv[1]=="-c":
		text=sys.argv[2]
	maze=[]
	for item in text:
		maze.append(item)
except IndexError:
	pass

def draw_maze(msg):
	final=''
	for i in range(len(msg)):
		if msg[i]=='w':
			bgcol="WHITE"
		elif msg[i]=='b':
			bgcol="BLACK"
		elif msg[i]=='r':
			bgcol="RED"
		elif msg[i]=='g':
			bgcol="GREEN"
		final+=getattr(Back,bgcol) + '  ' + Style.RESET_ALL
	print final

def draw_all(maze,culist):
	for x in range(20):
		s=''
		for i in range(x*20,x*20+20):
			if i in culist:
				color='r'
			else:
				color=maze[i]
			s+=color
		draw_maze(s)

def move(maze,culist,visit):
	nextlist=[]
	ulrd=[-20,-1,1,20]
	for current in culist:
		for direction in ulrd:
			n=current+direction
			try:
				if current%20==0 and direction==-1:
					continue
				elif current%20==19 and direction==1:
					continue
				elif n<0:
					continue
				elif maze[n]=='w' and visit[n]==0:
					nextlist.append(n)
					visit[n]=1
				elif maze[n]=='g' and visit[n]==0:
					nextlist.append(n)
					visit[n]=1
			except IndexError:
				pass
	culist=[]
	for nn in nextlist:
		culist.append(nn)
	return culist

movecount=0
culist.append(0)
while visit[399]==0:
	os.system('clear')
#	time.sleep(0.1)
	culist=move(maze,culist,visit)
	print('='*15+'MazeRunner'+'='*15)
	draw_all(maze,culist)
	print('culist:',culist)
	movecount+=1
	print('Moves : '+ str(movecount))
	time.sleep(0.3)
	if visit[-1]==1:
		print('Done!')
		exit()
	if len(culist)==0:
		print('Stuck!')
		exit()
