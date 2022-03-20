t=int(input())
answerlist=list()
for m in range(t):
    input_string=input()
    output_string=input()
    if(input_string in output_string):
        answer=len(output_string) - len(input_string)
        #print(answer) 
        answer=str(answer)
        answerlist.append(answer)
    else:
        length=0
        repeated=0
        while(length<len(input_string)):

            if((length+repeated)<len(output_string)):
                #print(i+repeated)
                if(input_string[length]==output_string[length+repeated]):
                    if(length+repeated<len(output_string)-1):
                        if(input_string[length+1]!=output_string[length+repeated+1]):
                            if(input_string[length]==output_string[length+repeated+1]):
                                repeated+=1
            length+=1
        if(repeated==0):
            answer="IMPOSSIBLE"
            answerlist.append(answer)
        else:
            answer=str(repeated)
            answerlist.append(answer)
for ans in range(len(answerlist)):
    print(f"Case #{ans+1}: {answerlist[ans]}")
        


