#!/usr/bin/env python
import math
import numpy
import matplotlib.pyplot as plt


#making a class to store the data in called graphs
class graphs:
	def __init__(self,variable,pvalue):
		self.variable=variable
		self.pvalue=pvalue

#binomial eqn
def binomeqn (n,s,a):
	t=n-s
	b=1-a
	p=((math.factorial(n))/(math.factorial(s)*(math.factorial(t))))*(a**s)*(b**float(t))
	return p


#make a list with numbers 1-100
list=[]
for x in range(1,101):
	list.append(x) 
#make a list with varying sample sizes from 5-500
nlist=[float(i)*5 for i in list]
#adding user input
a=(input("Want to detect rare allele at least once? Enter you're estimated rare allele frequency to determine optimal sample size:"))

#calculating p-values while varying sample size
pvals_nlist=[]
for n in nlist:	
	pv=binomeqn(n,0,a) #prob of finding allele NEVER
	q=1-pv #prob of finding allele one or more times
	pvals_nlist.append(q)
#print len(pvals_nlist)
#storing info 
vary_n=graphs(nlist,pvals_nlist)

#print vary_n.variable
#print vary_n.pvalue
print "Please close graph window when you are done viewing"
plt.plot(vary_n.variable,vary_n.pvalue)
plt.ylabel('probability of detecting allele at least once')
plt.xlabel('number of samples')
plt.show()
#plt.savefig("plot_of_optimal_sample_size.png")

#make a list with varying allele frequences
alist=[float(i)/500 for i in list]
#print alist
#adding user input
n=(input("You've got samples. How rare of an allele can you detect? Please enter current sample size:"))
#calculating p-values while varying allele frequency from .002-.2
pvals_alist=[]
for a in alist:	
	pv=binomeqn(n,0,a)
	q=1-pv
	pvals_alist.append(q)
#print len(pvals_alist)
#storing info 	
vary_a=graphs(alist,pvals_alist)
#print vary_a.variable
#print vary_a.pvalue
print "Please close graph window when you are done viewing"
plt.plot(vary_a.variable,vary_a.pvalue)
plt.ylabel('probability of detecting allele at least once')
plt.xlabel('frequency of alleles')
plt.show()
#plt.savefig("plot_of_allele_freqs_you_can_detect.png")

