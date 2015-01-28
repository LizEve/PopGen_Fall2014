#!/usr/bin/env python

import math
import numpy
import random
import matplotlib.pyplot as plt
gstats=[]
for x in range (5000):
#PART ONE: pull 400 indiv and assign to genotypes
#defining all my lists
	AAlist=[]
	AGlist=[]
	GGlist=[]
	ALL=[]
	#generating list of random numbers between 0-1
	for x in range (400):
		y=random.random()
		ALL.append(y)

	#print len(ALL)
	#add numbers to allele frequencies, I would like to do this within the above loop but can't figure out how. 
	#confusing shit happens with the allele frequences. so that...
	for y in ALL:
		if y <= 0.0625:
			AAlist.append(y)
		elif 0.0625 < y <= 0.4375:
			AGlist.append(y)
		else:
			GGlist.append(y)

	AA= len(AAlist)
	AG= len(AGlist)
	GG= len(GGlist)
	#if AA or AG or GG == 0:
	#	print "you drew no samples for one genotype, try again. your script will die"
	#print AA
	#print AG
	#print GG

	#Here are our "true" genotypes from the second round of random mating. 
	#and the observed numbers of genotypes from the random sample of 400 indiv from the popuation
	#the genotypes and frequencies are listed in order [AA,AG,GG]
	freq=[0.0625,0.375,0.5625] 
	#use genotypes picked in random sampling
	f=[AA,AG,GG]
	#print "f="+str(f)
	#calculate the expected number given frequencies
	f1=[float(i)*400 for i in freq]
	#print "f1="+str(f1)
	#calculate the ratio of f/f1
	ratio = [float(fi)/f1i for fi,f1i in zip(f,f1)] 
	#print "ratio="+str(ratio)
	#take the natural log
	ln = numpy.log(ratio)
	#print "ln="+str(ln)
	#multiple by the f stat, you could probably do this in the numpy command to tighten it up
	lnxf = [float(fi)*lni for fi,lni in zip(f,ln)]
	#print "lnxf="+str(lnxf)
	#GSTAT!
	gstat=2*sum(lnxf)
	#print "drumroll please.... and your gstat is... "+str(gstat)
	#degrees of freedom is 2

	gstats.append(gstat)

#print "did you get 5000 g-stats?"+str(len(gstats))

#Was having problems with g-stats all being below one, this was my test to see if they were all under 1
#test= []
#for x in gstats:
#	if x <= 1:
#		test.append(x)

#print len(test)

#numpy.histogram(gstats,bins=17)
#outfile= "gstats.csv" 
#x = open(outfile, 'w') # you can also use a to append and then instead of x.write do x.append
#for y in gstats:
#	x.write(str(y)) #for every item in list print item
#	x.write("\r") #after every item print a line break
#x.close() 
print "Please close graph windo when you are done"

plt.hist(gstats, bins = 50)
plt.show()


#you coud then go on and indicate where the 95%tile is

gstats.sort()
