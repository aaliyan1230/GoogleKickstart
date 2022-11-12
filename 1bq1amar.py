final_data = []
t = int(input())
for x in range(t):
    each = input()
    final_data.append(each)
ans = []
final_ans = []


def factors(x):
    for i in range(1, x + 1):
        if x % i == 0:
            i = str(i)
            if i == i[::-1]:
                ans.append(i)
    return len(ans)

for i in final_data:
    ans = []
    each = factors(int(i))
    final_ans.append(each)

for i in range(len(final_ans)):
    print("Case #{}: {}".format(i+1, final_ans[i])