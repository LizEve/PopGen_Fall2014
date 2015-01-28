#!/usr/bin/env python

import math
import random




pop=100
n= 0 #this is my counter
g= 0 
a=0.5

while 0<a<1:
	for x in range(pop):
		x=random.random()
		#print x
		if float(x) <= a: #if random number is less than or equal to current allele freq
			n += 1 #add a number to your count
		#print n
	a = float(n)/pop 
	print a
	n=0
	#print g
