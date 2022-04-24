from functools import reduce
# from sympy import factorint

# factorint()
tests=int(input())
#memoize=dict()
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
for t in range(tests):
    number=int(input())
    count=0
    numbers=factors(number)
    for i in numbers:
        temp=str(i)
        if number % i== 0:
            # if(memoize.get(i)==True):
            #     count+=1
            # el
            if(temp==temp[::-1]):
                count+=1
                # memoize[i]=True
    print(f"Case #{t+1}: {count}")