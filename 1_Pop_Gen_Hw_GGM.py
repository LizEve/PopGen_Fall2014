#!/usr/bin/env python

import random

#1a_random number between 0-1 to a file

randnuma=random.random() 
outfile= "randnum0_1.txt" 
x = open(outfile, 'w') # you can also use a to append and then instead of x.write do x.append
x.write(str(randnuma)) # you need to tell it that it is a string or it will be angry
x.close() # this speeds things up a lot

#1b_random number between 0-10 to a file

randnumb=random.randint(0,10) 
outfile= "randnum0_10.txt" 
x = open(outfile, 'w') # you can also use a to append and then instead of x.write do x.append
x.write(str(randnumb)) # you need to tell it that it is a string or it will be angry
x.close() # this speeds things up a lot

#2 use a loop to print 10 random numbers btw 0-1

for x in range (10): #range command counts over a range of numbers 10 goes from 0-9
	y=(random.random())
	print y #print automatically prints one number per line if in a loop

#3 use a loop to fill a list with random numbers

list=[]

for x in range (10): 
	y=(random.random())
	list.append(y)	#this adds to list

#print to seperate lines
for x in list:
	print x

#4 using the if function tally the number of items in the list that are < 0.5

#the lazy way
sum(i < 0.5 for i in list)

###another lazy way to populate a list of the numbers
answer = [y for y in list if y < 0.5]
#you can only print two of the same type of stuff at once, so you have to make answer a string
print "All of your numbers under 0.5 are:" +str(answer)

###with an if loop
#start a counter
n=0
#for the variables in list
for x in list:
	if x < 0.5:
		n += 1
		print n

#5

outfile= "problem4.csv" 
x = open(outfile, 'w') # you can also use a to append and then instead of x.write do x.append
for y in list:
	x.write(str(y)) # add comma so that each value is on the same line
	x.write(",") #add commas so that its read as a csv file 
	#you could do this more simply with w.write(str(list)) however this gives you brackets around your first and last numbers which is annoying. 
x.close() # this speeds things up a lot

#6 pick a random student from a list

names=["bill","rafa","rob","zach","subir","david","oscar","genevieve","cody","jasmine","vallmer","kristin","mark","joanna","brandon","viv","duhon","ryan"]
print names[random.randint(0,17)]



