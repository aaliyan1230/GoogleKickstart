import math
pi=math.pi
testcases=int(input())
for t in range(testcases):
    strlist=input()
    strlist=strlist.split()
    strlist=[int(i) for i in strlist]
    radius=strlist[0]
    answer=0
    radius=int(radius)
    print(radius)
    answer+=pi*radius**2
    while(radius>0):
        radius=radius*strlist[1]
        answer+=pi*radius**2
        radius=radius//strlist[2]
        answer+=pi*radius**2
        print(answer)
    print(f"Case#{t+1}: {answer}")



        

