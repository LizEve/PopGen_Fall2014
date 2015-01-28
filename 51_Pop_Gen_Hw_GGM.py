#!/usr/bin/env python

import math
import random



def drift(a,p):
	a=a #starting allele freq
	pop=p #pop size
	n= 0 #this is my counter
	gen= 0 #start counting generations to fixation
	while 0<a<1:
		gen +=1
		for x in range(pop):
			x=random.random()
			#print x
			if float(x) <= a: #if random number is less than or equal to current allele freq
				n += 1 #add a number to your count
			#print n
		a = float(n)/pop 
		#print a
		n=0
	return gen


a= input("allele freq:")
p= input("popsize:")
s= input("number of simulations to run:")

#a=0.45
#p=100
#s=1000


genstofix=[]
for r in range(s):
	x=drift(a,p)
	genstofix.append(x)
print genstofix

avggen=(float(sum(genstofix)))/(len(genstofix))
max=max(genstofix)
min=min(genstofix)

numabove=0
numbelow=0


for z in genstofix:
	if z<avggen:
		numbelow +=1
	if z>avggen:
		numabove +=1

print numabove
print numbelow
		

