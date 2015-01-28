#!/usr/bin/env python

import math
import random
import numpy
import matplotlib.pyplot as plt

#1/p=(4N)/(k(k-1)) is the average coalescence time mean of an exponetial distribution
#p= 1/(4N)/(k(k-1))
#go back a number of generations drawn from an expoenetial distripution with the expectation was seen in the thingy above


def coal(n,k):
	#N=Effective population size
	#k=Number of gene copies sampled
	#c=coalescent even you are interested in
	genstocoal=[] #create list to put coalescent time between each node
	while k > 1: #while k is larger than zero 
		expmean=((4*n)/float(k*(k-1)))
		draw=random.expovariate(1/expmean) #draw a random number
		genstocoal.append(draw)
		k -= 1

	#print len(gentocoal) 
	#this is ALWAYS equal to k-1
	#total time to coalescence of all gene copies
	total=sum(genstocoal)
	average=numpy.mean(genstocoal)
	lastvalue=k-2 #last value in list of coalescent times will be k-2
	#assign the coalescent time of the last two gene copies to a variable
	lastcoal=genstocoal[lastvalue] 	
	#print lastcoaltime
	#time to coalesce all but the last two
	allbut2=total-lastcoal
	#print allbut2
	#print "Returns a list= [total time to MRCA of all k, avg time to each coal event, avg caol time to 2 remaining gene copies, and then time it takes for the tow copies to coal,  [list of all coal values]]"
	coalnums=[total, average, allbut2, lastcoal, genstocoal]
	return coalnums
	#print coalnums
	#return gentocoal

def fivekmiles(n,k,y):
	#n=pop size
	#k=gene copies
	#x= which part you want to estimate 
	#0=total coalescent time
	#1=average coal time per branch within tree
	#2=time to coal of all but 2 copies
	#3=time to coal of last 2 gene copies
	simuavgs=[]
	for x in range (5000):
		coaloutput=coal(n,k) #passing output of coal func to variable
		totalcoaltime=coaloutput[y] #picking out sum of total times, which is total time to MRCA
		simuavgs.append(totalcoaltime) #adding each of these times to a list
	mean=numpy.mean(simuavgs)
	avglist=[mean,simuavgs]
	return avglist

def calcs(meanlist): #you will need to input the above values of a mean and a list of average gens to coalescence 
	avglist=meanlist[1] # parse out the list of averages from the 5000 simulations
	mean=meanlist[0] #get the mean from the output
	numabove=0
	numbelow=0
#calculate the number of averages above and below the mean
	for z in avglist:
		if z<mean:
			numbelow +=1
		if z>mean:
			numabove +=1
	stats=[mean, numabove, numbelow]
	return stats

		
print
print "welcome..."
print
print "...to the coalescent model"
print
print "An average value will be calculated over 5000 simulations"
print
print "Your choices are:"
print
print "0 = total coalescence time of all gene copies"
print "1 = average coalescence time per branch within population"
print "2 = time to coalescence of all but 2 gene copies"
print "3 = time to coalescence of last 2 gene copies"
print 
y=(input("So which value would you like to calculate?"))
n=(input("Effective population size:"))
k=(input("Number of gene copies sampled:"))



meanlist=fivekmiles(n,k,y)
stats=calcs(meanlist)
if y == 0:
	print "Mean *total* coalescence time:"+str(stats[0])
elif y == 1:
	print "Mean *average* coalescence time:"+str(stats[0])
elif y == 2:
	print "Mean time to coalescence of all but two gene copies:"+str(stats[0])
elif y == 3:
	print "Mean time to coalescence of the last two gene copies:"+str(stats[0])
else:
	print "you did somethign wrong"
print "Number of samples above mean:"+str(stats[1])
print "Number of samples below mean:"+str(stats[2])




