#!/usr/bin/env python
import math
import numpy
import matplotlib.pyplot as plt

#n= float(input("Number of alleles sampled:"))
#s= float(input("How many times do you want to detect your allele?:")) #number of successes of event 1, number of detections, so # of times you want to detect the allele in sample
#t= float(n-s) # of the times you detect all other alleles
#a= float(input("probability of event 1 occuring bases on a single trial(ie: pop freq of allele of interest):")) #true freq allele that you wanna detect
#b= float(1-a) #the fequences of all other alleles in pop


class qv:
	def __init__(self,samplesize,qvalue):
		self.n=samplesize
		self.q=qvalue


#binomial eqn
def binomeqn (n,s,a):
	t=n-s
	b=1-a
	p=((math.factorial(n))/(math.factorial(s)*(math.factorial(t))))*(a**s)*(b**float(t))
	return p

switch=False #made a switch so that you only print stuff once later on
#make lists to put pvalue 
q_values=[]
samplesize=[]
for n in range(1,200):
	p=binomeqn(n,0,0.05) #the probability of NOT finding the allele #everything cancles out except for b which is 1-.05= .95^t t= n-s, s is 0 so t=n. so 1-b^n
	q=1-p #probability of finding the allele at least once = 1-b^n
	q_values.append(q)
	samplesize.append(n)
	#now we want to 
	if q >= .95 and switch==False:
		idealn=n/2
		exactq=q
		print "Given an allele frequency of 0.05. your ideal sample size is:"+str(idealn)
		print "and the p value is:"+str(exactq)
		switch=True 

#n=log((1-p))/(log(1-b))
#would be nice to plot idealn on graph
print "Please close graph when you are done"
plt.plot(samplesize,q_values)
plt.ylabel('probability of detecting allele at least once')
plt.xlabel('number of diploid samples')
plt.show()
#plt.savefig("plot_of_sample_needed_for_p95.png")

#qvtest=qv(samplesize,q_values)


#plt.plot(samplesize,qvalue)
#plt.ylabel('p-values')
#plt.xlabel('number of samples')


#for n in range(500,1000):
#	p=binomeqn(n,1,0.05)

#	if p >= 0.95:
#		print p
#		print n
#	else:
#		print "nope"