# s=input()
# stack=list()
# open_complement=dict()
# open_complement["("]=")"
# open_complement["{"]="}"
# open_complement["["]="]"
# close_complement=dict()
# close_complement[")"]="("
# close_complement["}"]="{"
# close_complement["]"]="["
# result=False
# for i in s:
#     if(open_complement.get(i)!=None):
#         stack.append(i)
#     else:
#         if(stack[-1]==close_complement[i]):
#             stack=stack[:-1]

# if(len(stack)==0):
#     result=True
# else:
#     result=False

testcases=int(input())
for t in range(testcases):
    answer=0
    answerlist=list()
    L=int(input())
    array=input()
    array=array.split()
    array=[int(n) for n in array]
    for i in range(L-1):
        j=min(array[i:])
        answer=j+i-1
        answerlist.append(answer)
    
for a in range(testcases):
    print(f"Case#{a+1}: {answerlist[a]}")
