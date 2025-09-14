################ TO REDO ################

from math import floor,sqrt
from timeit import default_timer as timer
import functools

@functools.cache
def isPrime(n):
    i=5
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    while i < floor(sqrt(n))+1:
        if n % i == 0:
            return False
        if n % (i+2) == 0:
            return False
        i+=6
    return True

def sieveOfEratosthenes(tillNumber):
    
    sieve = list([ i for i in range( 2, tillNumber)])
    for i in range(2, int(sqrt(tillNumber)) +1):
        j = 2
        while j*i < tillNumber :
            if j*i in sieve:
                sieve.remove(j*i)
            j += 1
    return sieve

def isConcatenationPrime( p ):

    zStr = str(p[len(p)-1])
    p = p[0:len(p)-1]

    for i in p:
        iStr = str(i)
        if not isPrime(int(iStr + zStr)) or not isPrime(int(zStr + iStr)):
            return False
    return True

# 26033
def pr60(): # execution time: 1.2456304000224918
    start = timer()

    primes = sieveOfEratosthenes(10000)
    
    for i in range( len(primes)-4 ) :
        x = primes[i]
        for j in range( i+1, len(primes)-3 ):
            y = primes[j]
            if isConcatenationPrime( [x,y] ):
                for k in range( j+1,len(primes)-2 ):
                    u = primes[k]
                    if isConcatenationPrime( [x,y,u] ):
                        for l in range( k+1,len(primes)-1 ):
                            w = primes[l]
                            if isConcatenationPrime( [x,y,u,w] ):
                                for m in range( l+1, len(primes) ):
                                    z = primes[m]
                                    if isConcatenationPrime( [x,y,u,w,z] ):
                                        print(f'{x}, {y}, {u}, {w}, {z}')
                                        print(f'execution time: {timer()-start}')
                                        return x+y+u+w+z
    return 0

print(f'result pr60: {pr60()}')