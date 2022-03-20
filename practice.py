hashmap = dict()
citations = [5, 1, 2]

def H_index():
    for j in hashmap.keys():
        if(j==hashmap[j]):
            pass
count=0
for i in citations:
    count+=1
    try:
        hashmap[i]+=1
    except KeyError:
        hashmap[i]=0
    if(hashmap[i]>=count):
        H_index=hashmap[i]
        
        print(H_index)
        
    