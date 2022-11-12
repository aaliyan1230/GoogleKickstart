def run(inputFile, outputFile):
    inputFile=str(inputFile)
    outputFile=str(outputFile)
    with open(inputFile, "r") as file:
        file_liness=file.readlines()
        file_lines=list()
        for i in file_liness:
            file_lines.append(i.split())
        print(file_lines)
        for i in range(int(file_lines[0][0])):
            answercount=0
            start=int(file_lines[i+1][0])
            end=int(file_lines[i+1][1])
            for num in range(start,end+1):
                numstr=str(num)
                numproduct=1
                numsum=0
                for n in numstr:
                    numproduct = numproduct*int(n)
                    numsum+=int(n)
                if(numproduct%numsum==0):
                    answercount+=1
            print(answercount)

run("interesting_integers_sample_ts1_input.txt"," ")
