test=int(input())
for t in range(test):
    [l, n]=input().split()
    l=int(l)
    n=int(n)
    total=[]
    laps=0
    for i in range(n):
        [d, c]=input.split()
        d=int(d)
        if(total[1]==c):
            total[0]+=d
            laps+=total[0]//l
            total[0]%=l
        elif(total[1]==None):
            total[1]=c
            total[0]=d
            laps+=total[0]//l
            total[0]%=l
        else:
            total[0]-=d
            if(-total[0]>l):
                total[0]=-total[0]
                laps+=total[0]//l
                total[0]%=l
                total[1]=c
    print(f"Case #{t}: {laps}")
            
            