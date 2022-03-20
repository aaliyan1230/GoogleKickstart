import sys
# def is_palindrome(string):
#     if(string==string[::-1]):
#         return True
#     return False
    
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


t=int(input())
answerlist=list()
for m in range(t):
    length=int(input())
    input_string=input()
    answer="IMPOSSIBLE"
    if(len(input_string)>=5):
        qcount=input_string.count('?')
        indexlist=list()
        input_string_copy_q=input_string.replace('1','1',1)
        for i in range(qcount):
            indexlist.append(input_string_copy_q.find('?'))
            input_string_copy_q=input_string.replace('?',f"?{qcount}",1)
        #input_string_copy=input_string.replace('?','0')
        input_string_copy=input_string.replace('?','0')
        l = longestPalSubstr(input_string_copy)
        #print("Length is:", l)
        if(l<5):
            answer="POSSIBLE"
        c=0
        while(answer!="POSSIBLE" and c<len(indexlist)):
            input_string_copy=list(input_string_copy)
            input_string_copy[indexlist[c]]='1'
            instring=""
            for e in input_string_copy:
                instring+=e
            input_string_copy=instring
            l = longestPalSubstr(input_string_copy)
            #print("Length is:", l)
            if(l<5):
                answer="POSSIBLE"
            c+=1
        input_string_copy=input_string.replace('?','1')
        l = longestPalSubstr(input_string_copy)
        #print("Length is:", l)
        if(l<5):
            answer="POSSIBLE"
        c=0
        while(answer!="POSSIBLE" and c<len(indexlist)):
            input_string_copy=list(input_string_copy)
            input_string_copy[indexlist[c]]='0'
            instring=""
            for e in input_string_copy:
                instring+=e
            input_string_copy=instring
            l = longestPalSubstr(input_string_copy)
            #print("Length is:", l)
            if(l<5):
                answer="POSSIBLE"
            c+=1
        
    print(f"Case #{m+1}: {answer}")



