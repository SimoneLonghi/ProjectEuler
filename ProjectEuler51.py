from math import sqrt
from timeit import default_timer as timer
import re

def sieveOfEratosthenes(tillNumber):
    sieve = set([ i for i in range( 2, tillNumber)])
    for i in range(2, int(sqrt(tillNumber)) +1):
        j = 2
        while j*i < tillNumber :
            sieve.discard(j*i)
            j += 1
    return sieve

def findBrotherStructure(x):
    brothers = []
    brothers.append(x)
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            brothers.append( x[:i] + "*" + x[i+1:j] + "*" + x[j+1:] )
            for l in range(j+1,len(x)):
                brothers.append( x[:i] + "*" + x[i+1:j] + "*" + x[j+1:l] + "*" + x[l+1:] )
    return brothers

def pr51(): # execution time: 2.127935999999977
    start = timer()

    limit = 10**6
    primeTillLimit = sieveOfEratosthenes(limit)
    
    for i in primeTillLimit:
        if i > 10000:
            brothersStructure = findBrotherStructure(str(i))
            for n in brothersStructure:
                possibleBrothers = [ ( n.replace('*', str(k)) ) for k in range(10) if (n[0] != '*' or k != 0) and int(n.replace('*', str(k))) in primeTillLimit ]
                if len(possibleBrothers) == 8:
                    print(f'execution time: {timer()-start}')
                    return min(possibleBrothers)
    print(f'execution time: {timer()-start}')
    return "not find"

def pr51v2(): # execution time: 1.2353815000000168
    start = timer()

    limit = 10**6
    primeTillLimit = sieveOfEratosthenes(limit)
    brothers = []

    for i in primeTillLimit:
        prime = str(i)
        digitChecked = []
        for j in range(len(prime)):
            possibleBrother = prime
            for k in range(j+1,len(prime)):
                if prime[j] == prime[k] and prime[j] not in digitChecked:
                    possibleBrother = re.sub(prime[j], "*", possibleBrother)
                    digitChecked.append(prime[j])
                    brothers = [ ( possibleBrother.replace('*', str(k)) ) for k in range(10) if (possibleBrother[0] != '*' or k != 0) and int(possibleBrother.replace('*', str(k))) in primeTillLimit ]
                    if len(brothers) == 8:
                        print(f'execution time: {timer()-start}')
                        return min(brothers)
    print(f'execution time: {timer()-start}')
    return "not find"

print(f'result pr51  : {pr51()}')
print(f'result pr51v2: {pr51v2()}')
