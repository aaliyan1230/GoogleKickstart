import sys

from django.forms import NullBooleanField
def is_palindrome(string):
    if(string==string[::-1]):
        return True
    return False
    
# Python program

# A utility function to print a
# substring str[low..high]
def printSubStr(st, low, high) :
	sys.stdout.write(st[low : high + 1])
	sys.stdout.flush()
	return ''

# This function prints the longest palindrome
# substring of st[]. It also returns the length
# of the longest palindrome
def longestPalSubstr(st) :
	n = len(st) # get length of input string

	# table[i][j] will be false if substring
	# str[i..j] is not palindrome. Else
	# table[i][j] will be true
	table = [[0 for x in range(n)] for y
						in range(n)]
	
	# All substrings of length 1 are
	# palindromes
	maxLength = 1
	i = 0
	while (i < n) :
		table[i][i] = True
		i = i + 1
	
	# check for sub-string of length 2.
	start = 0
	i = 0
	while i < n - 1 :
		if (st[i] == st[i + 1]) :
			table[i][i + 1] = True
			start = i
			maxLength = 2
		i = i + 1
	
	# Check for lengths greater than 2.
	# k is length of substring
	k = 3
	while k <= n :
		# Fix the starting index
		i = 0
		while i < (n - k + 1) :
			
			# Get the ending index of
			# substring from starting
			# index i and length k
			j = i + k - 1
	
			# checking for sub-string from
			# ith index to jth index iff
			# st[i + 1] to st[(j-1)] is a
			# palindrome
			if (table[i + 1][j - 1] and
					st[i] == st[j]) :
				table[i][j] = True
	
				if (k > maxLength) :
					start = i
					maxLength = k
			i = i + 1
		k = k + 1
	#print(" is the longest palindrome substring ", printSubStr(st, start,start + maxLength - 1))

	return maxLength # return length of LPS

class palindromechecking:
    def __init__(self):
        self.hashmap=dict()
        self.answerlist=list()
        self.t=int()

    def recursivePalindromeOfFive(self,string=str()):
        result="IMPOSSIBLE"
        if(self.hashmap.get(string)!=None):
            return self.hashmap.get(string)
        elif(len(string)<5):
            result="POSSIBLE"
            self.hashmap[string]=result
        else:
            if(is_palindrome(string)):
                result="IMPOSSIBLE"
                self.hashmap[string]=result
            else:
                result=self.recursivePalindromeOfFive(string[:-1])
                self.hashmap[string]=result
        return result


    def inputdata(self):
        answer="IMPOSSIBLE"
        self.t=int(input())
        for m in range(self.t):
            length=int(input())
            input_string=input()
            if('?' in input_string):
                qcount=input_string.count('?')
                binarynum="0"*qcount
                indexlist=list()
                for i in range(qcount):
                    indexlist.append(input_string.find('?'))
                    input_string=input_string.replace('?',"d",1)
                qcount=2**qcount
                q=0
                while(answer!="POSSIBLE" and q<qcount):
                    binaryn=str(bin(int(binarynum,2)+int("1",2)))
                    binaryn=binaryn[2:]
                    binarynumlist=list()
                    for g in binarynum:
                        binarynumlist.append(g)
                    if(len(binaryn)<=len(binarynumlist)):
                        for b in range(1,len(binaryn)+1):
                            binarynumlist[-b]=binaryn[-b]
                    binarynum=""
                    for b in binarynumlist:
                        binarynum+=b
                    #print(binaryn)
                    #print(binarynum)
                    stringlist=list()
                    for l in input_string:
                        stringlist.append(l)
                # print(stringlist)
                    
                    for ind in range(len(indexlist)):
                        stringlist[indexlist[ind]]=binarynum[ind]
                    input_string=""
                    for string in stringlist:
                        input_string+=string
                    answer=self.recursivePalindromeOfFive(input_string)
                    q+=1
            else:
                answer=self.recursivePalindromeOfFive(input_string)
        self.answerlist.append(answer)
        
    def outputdata(self):
        #for e in range(self.t):    
        print(self.answerlist)    
    

answerobject=palindromechecking()
answerobject.inputdata()
answerobject.outputdata()

# t=int(input())
# answerlist=list()
# for m in range(t):
#     length=int(input())
#     input_string=input()
#     answer="IMPOSSIBLE"
#     if('?' in input_string):
#         qcount=input_string.count('?')
#         binarynum="0"*qcount
#         indexlist=list()
#         #input_string_copy=input_string#made a copy essentially
#         #print(input_string_copy)
#         for i in range(qcount):
#             indexlist.append(input_string.find('?'))
#             input_string=input_string.replace('?',"d",1)
#         #print(input_string_copy)
#         #input_string_copy=input_string.replace('?','0')
#         #print(indexlist)
#         qcount=2**qcount
#         q=0
#         while(answer!="POSSIBLE" and q<qcount):
#             binaryn=str(bin(int(binarynum,2)+int("1",2)))
#             binaryn=binaryn[2:]
#             binarynumlist=list()
#             for g in binarynum:
#                 binarynumlist.append(g)
#             #print(binarynumlist)
#             #print(binaryn)
#             if(len(binaryn)<=len(binarynumlist)):
#                 for b in range(1,len(binaryn)+1):
#                     binarynumlist[-b]=binaryn[-b]
#             binarynum=""
#             for b in binarynumlist:
#                 binarynum+=b
#             #print(binaryn)
#             #print(binarynum)
#             stringlist=list()
#             for l in input_string:
#                 stringlist.append(l)
#            # print(stringlist)
            
#             for ind in range(len(indexlist)):
#                 stringlist[indexlist[ind]]=binarynum[ind]
#             input_string=""
#             for string in stringlist:
#                 input_string+=string
#             l = longestPalSubstr(input_string)
#             #print(l)
#             #print("Length is:", l)
#             if(l<5):
#                 answer="POSSIBLE"
#             q+=1
#     else:
#         l = longestPalSubstr(input_string)
#         #print(l)
#         #print("Length is:", l)
#         if(l<5):
#             answer="POSSIBLE"  
#     answerlist.append(answer)
# #outputfile = open("test_set_1\\ts1_output.txt","r")

# for e in range(t):    
#     print(f"Case #{e+1}: {answerlist[e]}")
