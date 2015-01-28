#!/usr/bin/env python

import math
import numpy
import random

#import matplotlib.pyplot as plt
#1. Write a script that assigns allele frequencies to two loci in two separate populations. Write the script so that the user can enter the allele frequencies.
#returns samples
def hapsample(p1,q1,N):
	p2=1-p1
	q2=1-q1
	#print p2
	#print q2
	#calculate haplotype frequencies, want to redo by sampling from allele freqs, creating hap freq and then count from there. 
	x11=p1*q1
	x12=p1*q2
	x21=p2*q1
	x22=p2*q2
	#print "haplotype x11="+str(x11)
	#print "haplotype x12="+str(x12)
	#print "haplotype x21="+str(x21)
	#print "haplotype x22="+str(x22)
	#create allele frequency brackets for random generation of haplotypes
	a=x11
	b=x11+x12
	c=b+x21
	d=c+x22
	#could also write as a, b, c, d= x11, x11+x12
	#print a
	#print b
	#print c
	#print d
	#make lists to put hap freqs into. I could do this cleaner but will fix later
	Lx11=[]
	Lx12=[]
	Lx21=[]
	Lx22=[]
	ALL=[]
	#generating list of random numbers between 0-1
	for x in range (N):
			y=random.random()
			ALL.append(y)
	#assign random numbers to haplotype groups
	for y in ALL:
			if y <= a:
				Lx11.append(y)
			elif a < y <= b:
				Lx12.append(y)
			elif b < y <= c:
				Lx21.append(y)
			else:
				Lx22.append(y)
	#add up the number of individuals in each catagory
	Lx11=len(Lx11)
	Lx12=len(Lx12)
	Lx21=len(Lx21)
	Lx22=len(Lx22)
	samples=[Lx11,Lx12,Lx21,Lx22]
	#print "output is the number of individuals sampled per haplotype frequency, in the order x11,x12,x21,x22: "+str(samples)
	print "Indiv per haplotype- x11,x12,x21,x22: "+str(samples)
	return samples
#returns hapfreqs
def hapfreqs(samples,N):
	hapfreq=[float(i)/N for i in samples]
	#recalculate haplotype frequences from samples
	print "Haplotype Frequencies x11,x12,x21,x22: "+str(hapfreq)
	return hapfreq

def allelefreqs(hapfreq):
	x11=hapfreq[0]
	x12=hapfreq[1]
	x21=hapfreq[2]
	x22=hapfreq[3]
	a1=x11+x12
	a2=x21+x22
	b1=x11+x21
	b2=x12+x22
	#put allele freqs in a list
	allelefreq=[a1,a2,b1,b2]
	print "Allele Freqs- p1, p2, q1, q2: "+str(allelefreq)
	return allelefreq

def Dprime(hapfreq):
	#assign each item in list to a variable
	x11=hapfreq[0]
	x12=hapfreq[1]
	x21=hapfreq[2]
	x22=hapfreq[3]
	#print x11
	#print x12
	#print x21
	#print x22
	#calculate D value
	D=float(x11)*x22-x12*x21
	print "Your D value is: "+str(D)
	#calculate Dmax
	for x in hapfreq:
		if x==0:
			Dmax=1
		elif D > 0:
			Dmax=min(x12,x21)
		elif D < 0:
			Dmax=min(x11,x22)
		else:
			print "YO! Something's fucked up"

	print "Your Dmax value is: "+str(Dmax)
	#calculate Dprime
	Dprime=D/Dmax	
	#print "Your D' value for species A is: "+str(Dprime)	

	return Dprime,D

def rsqrd(allelefreq,D):
	#assign each item in list to a variable
	p1=allelefreq[0]
	p2=allelefreq[1]
	q1=allelefreq[2]
	q2=allelefreq[3]
	#calculate Pearson coefficient of correlation, aka r
	r=D/math.sqrt(p1*p2*q1*q2)
	rsqrd=r**2
	#print "Your r-squared value for species A is: "+str(rsqrd)
	return rsqrd

print "Assuming diploid species, if not the case, please go adjust the script"
#simulate for species A
print "Species A-"
A=(input('Sample Size='))
p1A=(input('Frequency of allele at loci 1:'))
print "Yo! "+str(p1A)+" Is this a decimal?"
q1A=(input('Frequency of allele at loci 2:'))
print "Yo! "+str(q1A)+" Is this a decimal?"

#run function to pull 40 individuals for given species and calculate hap, allel freq and return sample numbers that created those freqs
#create diploid indivs
Na=2*A
#create number of samples per haplotype based on user input allele freqs
samplesA=hapsample(p1A,q1A,Na)
#create haplotype frequencies from number of samples
hapfreqA=hapfreqs(samplesA,Na)
#create allele freqs from haplotype fregs
allelefreqA=allelefreqs(hapfreqA)
#calculate Dprime
DpA=Dprime(hapfreqA)
#this returns 2 values, Dprime then D
Da=DpA[1]
#define D to use in r-squared

print "Species A- D prime: "+str(DpA[0])

#calculate r-squared

r2A=rsqrd(allelefreqA,Da)

print "Species A- R-squared: "+str(r2A)

#simulate for species B
print "Species B"
B=(input('Sample Size='))
p1B=(input('Frequency of allele at loci 1:'))
print "Yo! "+str(p1B)+" Is this a decimal?"
q1B=(input('Frequency of allele at loci 2:'))
print "Yo! "+str(p1B)+" Is this a decimal?"


#run function to pull 40 individuals for given species and calculate hap, allel freq and return sample numbers that created those freqs
#create diploid indivs
Nb=2*B
samplesB=hapsample(p1B,q1B,Nb)

hapfreqB=hapfreqs(samplesB,Nb)
allelefreqB=allelefreqs(hapfreqB)

DpB=Dprime(hapfreqB)
#this returns 2 values, Dprime then D
print "Species B- D prime: "+str(DpB[0])
Db=DpB[1]
r2B=rsqrd(allelefreqB,Db)

print "Species B- R-squared: "+str(r2B)

#to observe wahlund effect
print "What if we combine the samples from both populations?"
print "samplesA is:"+str(samplesA)
print "samplesB is:"+str(samplesB)
samplesmix=[samplesAi+samplesBi for samplesAi,samplesBi in zip(samplesA,samplesB)]
print "samples mixed is:"+str(samplesmix)
Nmix=Na+Nb

sum=0
for x in samplesmix:
	sum += (x)

print sum

if sum == Nmix:
	print "Total individuals in mixed sample:"+str(Nmix)
else:
	print "Yo, some numbers are not adding up."


hapfreqmix=hapfreqs(samplesmix,Nmix)

allelefreqmix=allelefreqs(hapfreqmix)

Dpmix=Dprime(hapfreqmix)
#this returns 2 values, Dprime then D

print "Mix Sp A & Sp B- D prime: "+str(Dpmix[0])
Dmix=Dpmix[1]

r2mix=rsqrd(allelefreqmix,Dmix)

print "Mix Sp A & Sp B- R-Squared: "+str(r2mix)

print "Comparisons"
print "D'=1 means there is complete LD D'=0 means no LD"
print "D' for A:"+str(DpA[0])
print "D' for B:"+str(DpB[0])
print "D' after mixing A and B:"+str(Dpmix[0])