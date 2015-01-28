#!/usr/bin/env python
import math
import numpy
import random
import pylab

#rafas script is below

zerolist=[]
onelist=[]
genstofixationlist=[]

for r in range (1000):
	n=1--
	a=0.1
	i=0 # number of indiv with allele A in the next generation
	g=0
	while 0<a<1:
		g +=1
		for x in range(n):	
			x=random.random()
			if x<a:
				i +=1
		a=i/n #divide i by pop size to obtain the actual allele freq of a
		
	if a==0:
		zerolist.append(a)
	if a==1:
		genstofizationlist.append(g)
		onelist.append(a)

number of times a was lost = len(zerolist)
number of times a was fixed = len(onelist)
average number of generations to fixation was numpy.mean(genstofixationlist)


belowavg=0
aboveavg=0

for n in (genstofixationlist):
		if n<(numpy.mean(genstofixationlist)):
			