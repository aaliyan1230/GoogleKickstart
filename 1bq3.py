from posixpath import split


tests=int(input())
for t in range(tests):
    ND=input().split()
    N=int(ND[0])
    D=int(ND[1])
    lines=input().split()
    onecount=0
    for o in lines:
        if(o=="1"):
            onecount+=1
    print(f"Case #{t+1}: {onecount-1}")