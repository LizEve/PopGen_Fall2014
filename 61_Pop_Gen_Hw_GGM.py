#!/usr/bin/env python

import math
import random
import matplotlib.pyplot as plt


#1/p=(4N)/(k(k-1)) is the average coalescence time mean of an exponetial distribution
#p= 1/(4N)/(k(k-1))
#go back a number of generations drawn from an expoenetial distripution with the expectation was seen in the thingy above


def create_prior_dist(N,k):
	#N=Effective population size
	#k=Number of gene copies sampled
	expmean=((4*N)/float(k*(k-1)))
	prior_dist=[]
	for x in range (5000):
		draw=random.expovariate(1/expmean)
		prior_dist.append(draw)
	return prior_dist

def make_hist(x):
	#x=prior distripution 
	#print "Please close graph window when you are done"
	plt.hist(x, bins = 50)
	#plt.show()
	plt.savefig("Nk.png")

N=(input("Effective population size:"))
k=(input("Number of gene copies sampled:"))

prior_dist=create_prior_dist(N,k)
make_hist(prior_dist)







