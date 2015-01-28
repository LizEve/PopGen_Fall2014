#!/usr/bin/env python

#Pop Gen Notes 9.10.2014

#will almost always use 
import random

# try? I can't get this to work. 
print(a, file = outfile)

#2 another way that is mostly just an example of what a def main looks like. still not sure what it does. 

def main():
#creating the file for writing	
	file=open("problem2.txt", "w")
#looping over the random number ten times
	for x in range(10):
		y=random.uniform(0,1)
		print(y)
#changing the values to strings so they can be written to a file
		file.write(str(y)+str("\n"))
#creating a new line for each
		file.write('\n')
	file.close()

main()

#make script executable
Chmod 777 Filename.py



>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> zipped
[(1, 4), (2, 5), (3, 6)]