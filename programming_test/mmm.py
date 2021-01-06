#!/usr/bin/python
import os
from colorama import init, Fore, Back, Style
import random
init()

print('='*10)
print 'Hello Maze'
print('='*10)

maze=[]
for i in range(20):
	maze.append([])
	for j in range(20):
		
		maze[i].append('x') if random.randint(1,3)==1 else maze[i].append('')

maze=[]⏎
for i in range(400):⏎
	if random.randint(1,5)==1:⏎
		maze.append('b')⏎
	else:⏎
		maze.append('w')

print(maze)

