class gene:
	def __init__ (self, seq, chr):
		self.myseq=seq  #need to re-set variable to equal something within the class or whatever you are handing it will dissapear
		self.chr=chr 

#input further down the code

gene1=gene(ATTAGTGT,ch23) #gene1 is an object of class gene

print gene1.chr
	#will print ch23


#imagine this is in a file named popgen
def binomeqn (n,s,a):
	t=n-s
	b=1-a
	p=((math.factorial(n))/(math.factorial(s)*(math.factorial(t))))*(a**s)*(b**t)
	return p


#imagine this is a new file
#this is how you re-use a function while getting user input

import popgen.binomeqn

popsize= raw_input("what is your pop size?")
#etc

pval=binomeqn(popsize,etc) #assinging this to a variable is important, otherwise you can't get it back
print pval


#this adds a bunch of tuples to a list 
for x in range(10):
	name = "run_" +str(x)
	pval = binomeqn(x)
	tup=(name,pval)
	list.append(tup)



