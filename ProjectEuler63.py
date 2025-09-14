from timeit import default_timer as timer
from math import log
''' find all the n-digit number cn s.t. cm - a^n for a positive integer
    i.e. cn s.t. 10^(n-1) < a^n < 10^n
    i.e. a < 10 and n < log(10) / ( log(10) - log(a) ) '''

def countDigit(a):
    return len(str(a))

def pr63(): # execution time: 2.6900001103058457e-05
    start = timer()
    
    log10 = log(10)
    count = 0

    for a in range(1,10):
        n_max = int( log10 // ( log10 - log(a) ) )
        for n in range(1, n_max + 1):
            if n == countDigit(a**n):
                count += 1

    print(f'execution time: {timer()-start}')
    return count

print(f'result pr63: {pr63()}')