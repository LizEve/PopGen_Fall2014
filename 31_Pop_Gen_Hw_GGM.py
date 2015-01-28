#!/usr/bin/env python
import math
import numpy
#p- prob of deceting 
#number of trials, so # of individuals (x2 for diploids)
n= float(input("Number of alleles sampled:"))
s= float(input("How many times do you want to detect your allele?:")) #number of successes of event 1, number of detections, so # of times you want to detect the allele in sample
t= float(n-s) # of the times you detect all other alleles
a= float(input("probability of event 1 occuring bases on a single trial(ie: pop freq of allele of interest):")) #true freq allele that you wanna detect
b= float(1-a) #the fequences of all other alleles in pop

p=((math.factorial(n))/(math.factorial(s)*(math.factorial(t))))*(a**s)*(b**t)

print "The probability of detecting your allele is:"+str(p)