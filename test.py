#!/usr/bin/python3
import random
numbers=[i+1 for i in range(45)]
for i in range(5):
	random.shuffle(numbers)
	print(sorted(numbers[:6]))
input()
