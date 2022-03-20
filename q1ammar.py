# import collections

# t = int(input())
# final_data = []
# diff = 0
# ansEach = 0
# ans = []
# countEachInInput = 0
# countEachInOutput = 0
# for x in range(1, t+1):
#     each = [input(), input()]
#     final_data.append(each)
# print(final_data)
# dupRemBoth = ""
# both = ""
# inp = ""
# output = ""
# final = []
# asc = []
# inpDict = {}
# eachCaseAnswer = []
# outDict = {}
# dup = []

# for i in range(len(final_data)):
#     ans = []
#     inp = final_data[i][0]
#     output = final_data[i][1]
#     inpDict = collections.Counter(inp)
#     outDict = collections.Counter(output)
#     both = inp + output
#     s = set(both)
#     s = "".join(s)
#     dupRemBoth = s
#     for j in range(len(both)):
#         asc.append(ord(both[j]))
#     seen = set()
#     dupes = []
#     for x in asc:
#         if x in seen:
#             dupes.append(x)
#         else:
#             seen.add(x)
#     check = any(item in asc for item in dupes)
#     print(both)
#     print(inpDict, outDict)
#     for charNum in range(len(dupRemBoth)):
#         if inpDict[dupRemBoth[charNum]] == outDict[dupRemBoth[charNum]]:
#             inpDict.pop(dupRemBoth[charNum])
#             outDict.pop(dupRemBoth[charNum])

#         elif inpDict[dupRemBoth[charNum]] < outDict[dupRemBoth[charNum]] and check:
#             diff = outDict[dupRemBoth[charNum]] - inpDict[dupRemBoth[charNum]]
#             ans.append(diff)
#         else:
#             break
#     eachCaseAnswer.append(ans)
# print(eachCaseAnswer)
# for i in eachCaseAnswer:
#     if len(i) >= 1:
#         final.append(sum(i))
#     else:
#         final.append("IMPOSSIBLE")

# print(final)

# for i in range(len(final)):
#     print("Case #{}: {}".format(i+1, final[i]))

# #loop over final
binarynum=bin(int('101001',2)-int('1',2))
print(binarynum)