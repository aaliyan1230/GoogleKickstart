t = int(input())
for m in range(t):
    citations=list()
    size=int(input())
    citations=input()
    citations=citations.split()
    for c in citations:
        c=int(c)
    count=0
    h_index=0
    def hindex(citations):
        size=len(citations)
        hashmap = list()
        for d in range(size+1):
            hashmap.append(0)
        for i in citations:
            i=int(i)
            if(int(i)>=size):
                if(hashmap[size]!=None):
                    hashmap[size]+=1
                else:
                    hashmap[size]=0
                    hashmap[size]+=1
            else:
                if(hashmap[i]!=None):
                    hashmap[i]+=1
                else:
                    hashmap[i]=0
                    hashmap[i]+=1
        counter=0
        i=size
        while i>0:
            if(hashmap[i]!=None):
                counter+=hashmap[i]
            if(counter>=i):
                return i
            i-=1
    
    citations2=list()
    print(f"Case #{m+1}: ", end="")
    for i in citations:
        citations2.append(i)
        print(hindex(citations2), end=" ")
    print("")
        
        
    