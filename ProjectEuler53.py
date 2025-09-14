from timeit import default_timer as timer
import functools

@functools.cache
def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    elif n == 1:
        return n
    else:
        return 0

def BinCoeff(n,k):
    if k == 0 or k == n:
        return 1
    return factorial(n)/(factorial(k)*(factorial(n-k)))

@functools.cache
def BinCoeffRec(n,k):
    if k == 0 or k == n:
        return 1
    return BinCoeffRec(n-1,k-1) + BinCoeffRec(n-1,k)
    
def pr53(): # execution time: 
    start = timer()
    count = 0
    for n in range(100+1):
        for k in range(n):
            if BinCoeff(n,k) > 1000000:
                count += 1 
    print(f'execution time: {timer()-start}')
    return count
 
def pr53v2(): # execution time: 
    start = timer()
    count = 0
    for n in range(100+1):
        for k in range(n):
            if BinCoeffRec(n,k) > 1000000:
                count += 1 
    print(f'execution time: {timer()-start}')
    return count

print(f'result pr53  : {pr53()}')
print(f'result pr53v2: {pr53v2()}')
