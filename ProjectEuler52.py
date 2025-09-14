import numpy as np
from collections import Counter
from timeit import default_timer as timer

def isPermutation(a, b):
    return Counter([int(j) for j in str(a)]) == Counter([int(j) for j in str(b)])

#142857
def pr52naive(): # execution time: 0.15129059995524585
    start = timer()

    x = 102345
    while x < 166667:  # 166667*6 = 1.000.002
        for i in range(2,7):
            if not isPermutation(x, x*i) :
                break
            elif i == 6:
                print(f'execution time: {timer()-start}')
                return x
        x += 1

def pr52(): # execution time: 0.012431199895218015
    start = timer()

    x = 100002
    while x < 166667:  # 166667*6 = 1.000.002
        for i in range(2,7,2):
            if not isPermutation(x, x*i) :
                break
            elif i == 6:
                print(f'execution time: {timer()-start}')
                return x
        #from the conditions 3*x, x has to be divisible by 3, and from 5*x, x has to contain 0 or 5
        x += 3
        xStr = str(x)
        while ( len(set(xStr)) != len(xStr) or not ( '0' in xStr or '5' in xStr ) ) and x < 166667: 
            x += 3
            xStr = str(x)


print(f'result pr52 : {pr52naive()}')
print(f'result pr52v2 : {pr52()}')