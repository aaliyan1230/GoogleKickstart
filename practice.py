# hashmap = dict()
# citations = [5, 1, 2]

# def H_index():
#     for j in hashmap.keys():
#         if(j==hashmap[j]):
#             pass
# count=0
# for i in citations:
#     count+=1
#     try:
#         hashmap[i]+=1
#     except KeyError:
#         hashmap[i]=0
#     if(hashmap[i]>=count):
#         H_index=hashmap[i]
        
#         print(H_index)
# testcases=int(input())
# answerlist=list()
# for t in range(testcases):
#     L=int(input())
#     array=input()
#     array=array.split()
#     array=[int(a) for a in array]
#     cost=0
#     for i in range(L-1):
#         minn=min(array[i:])
#         j=array.index(minn)
#         arr_portion1=array[i:j+1]
#         arr_portion1.reverse()
#         arr_portion2=array[j+1:]
#         array=array[:i]
#         array.extend(arr_portion1)
#         array.extend(arr_portion2)
#         cost+=j-i+1
#     answerlist.append(cost)

# for t in range(testcases):
#     print(f"Case #{t+1}: {answerlist[t]}")
# array=[1,2,3]
# for i in array:
#     for j in array:
#         array[i-1],array[j-1]=array[j-1],array[i-1]
#         print(array)
testcases=int(input())
answerlist=list()
for t in range(testcases):
    inp=input()
    inp=inp.split()
    N=int(inp[0])
    C=int(inp[1])
    array=[int(a) for a in range(1,N+1)]
    possibility=False
    for k in range(1,N+1):
        if(possibility==False):
            for m in range(1,N+1):
                array[k-1],array[m-1]=array[m-1],array[k-1]
                cost=0
                for i in range(N-1):
                    minn=min(array[i:])
                    j=array.index(minn)
                    arr_portion1=array[i:j+1]
                    arr_portion1.reverse()
                    arr_portion2=array[j+1:]
                    array=array[:i]
                    array.extend(arr_portion1)
                    array.extend(arr_portion2)
                    cost+=j-i+1
                print(array, " has cost ", cost)
                if(cost==C):
                    answerlist.append(array)
                    possibility=True
                    break
    if(possibility==False):
        answerlist.append("IMPOSSIBLE")
for t in range(testcases):
    print(f"Case #{t+1}: {answerlist[t]}")
    print(answerlist)
