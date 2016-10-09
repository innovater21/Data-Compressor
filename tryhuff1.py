import sys,os,string
codes={}
str=input("enter the values:")
def frequencycount (str) :
	freqs = {}
	for ch in str :
		freqs[ch] = freqs.get(ch,0) + 1
		
		
	return freqs

def sortFrequency (freqs) :
	data= freqs.keys()
	tuples = []
	for let in data :
		tuples.append((freqs[let],let))
	tuples.sort()
	return tuples

def buildmainTree(tuples) :
	while len(tuples) > 1 :
		leastTwo = tuple(tuples[0:2])                  
		theRest  = tuples[2:]                          
		combFreq = leastTwo[0][0] + leastTwo[1][0]     
		tuples   = theRest + [(combFreq,leastTwo)]     
		tuples.sort()                                
	return tuples[0]  

def finalTree (tree) :
	 
	p = tree[1]                                    
	if type(p) == type("") : return p              
	else : return (trimTree(p[0]), trimTree(p[1]))    

def assignCodes (node, pat='') :
	global codes
	if type(node) == type("") :
		codes[node] = pat                
	else  :                              
		assignCodes(node[0], pat+"0")    
		assignCodes(node[1], pat+"1")   

def encode (str) :
	global codes
	output = ""
	for ch in str : output += codes[ch]
	return output

'''def decode (tree, str) :
    output = ""
    p = tree
    for bit in str :
        if bit == '0' : p = p[0]    
        else          : p = p[1] 
        if type(p) == type("") :
            output += p              
            p = tree                
    return output'''




def main(str):
	freqs=frequencycount(str)
	tuple1=sortFrequency(freqs)
	tree=buildmainTree(tuple1)
	tree=finalTree(tree)
	assignCodes(tree)
	output=encode(str)
	#decodeddata=decode(output,str)
	
	print(output)
	print ("Previous text length", len(str))
	print ("Requires %d bits. (%d bytes)" % (len(output), (len(output)+7)/8))
	#print ("Restored matches original", str == decodeddata)
	#print(decodeddata)
main(str)

