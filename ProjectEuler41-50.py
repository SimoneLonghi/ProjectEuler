from math import floor,sqrt
from timeit import default_timer as timer
import string
import os

def loadNames(url):
    with open( os.path.dirname(__file__) + '\\' + url,'r') as f:
        contents = f.read()
        f.close()
    contents = contents.replace('"','')
    return contents.split(',')

def findAllPermutations(s):
    if len(s) == 1:
        return [s]
    else:
        perms = []
        for i, c in enumerate(s):
            for perm in findAllPermutations(s[:i] + s[i+1:]):
                perms.append(c + perm)
        return perms

def sieveOfEratosthenes(tillNumber):
    sieve = set([ i for i in range( 2, tillNumber)])
    for i in range(2, int(sqrt(tillNumber)) +1):
        j = 2
        while j*i < tillNumber :
            sieve.discard(j*i)
            j += 1
    return sieve

def isPrime(n):
    i=2
    if n <= 0 or n != floor(n):
        return False
    while i < floor(sqrt(n))+1:
        if n % i == 0:
            return False
        i+=1
    return True

def findDistintPrimeFactors( n, distinctPrimeFactors, primes ):
    foundFactors = 0
    if n not in primes:
        i = 0
        while i < len(primes) - 1 and primes[i] < ( n // 2 ) + 1 and foundFactors < distinctPrimeFactors: # TODO add hard break if i < len(primes) - 1
            if n % primes[i] == 0:
                foundFactors += 1
            i += 1
    return foundFactors == distinctPrimeFactors

def selfPower( base ):
    result = base
    for times in range( 1, base ):
        result = ( result*base ) % (10**10)
    return result

def selfPowerRecursion( base, times, result ): # RecursionError: maximum recursion depth exceeded
    if times == 1:
        return result
    else:
        result = (result*base) % (10**10)
        return selfPowerRecursion( base, times-1, result )
    
def constantDiff(permutations):
    for i in range( len(permutations)-2 ):
        for j in range( i + 1, len(permutations)-1 ):
            diff = int(permutations[j]) - int(permutations[i])
            for k in range( j + 1, len(permutations) ):
                if diff != 0 and int(permutations[k]) - int(permutations[j]) == diff:
                    return permutations[i] + permutations[j] + permutations[k]
    return ''


def pr41():
    start = timer()
    
    nPandigital = '1234567890'

    for i in range(len(nPandigital)):
        permutations = sorted( set( [ i for i in findAllPermutations(nPandigital[:-i]) ] ))

        p = len(permutations)
        while p > 0:
            p -= 1
            if isPrime( int(permutations[p]) ):
                print(f'execution time: {timer()-start}')
                return permutations[p]

    print(f'execution time: {timer()-start}')
    return 0

def pr42():
    start = timer()

    nOfTriangleWord = 0
    limits = 26*7   # ='ZZZZZZZ'
    triangleNumbers = [ ( i*(i+1) ) // 2 for i in range( 0, limits ) ]
    charToNumber = dict(zip(string.ascii_uppercase, range(1,27)))
    words = loadNames('pr42_words.txt')

    for word in words:
        sumOfChar = 0
        for char in word:
            sumOfChar += charToNumber[char]
        if sumOfChar in triangleNumbers:
            nOfTriangleWord += 1

    print(f'execution time: {timer()-start}')
    return nOfTriangleWord

def pr43():
    start = timer()

    totSum = 0
    permutations = findAllPermutations('0123456789')
    prime = list({1,1,2,3,5,7,11,13,17})

    for pandigital in permutations:
        isConditionSatisfied = True
        i = 1
        while i < len(prime):
            if not int(pandigital[i:i+3]) % prime[i] == 0:
                isConditionSatisfied = False
            i += 1
        if isConditionSatisfied:
            totSum += int(pandigital)

    print(f'execution time: {timer()-start}')
    return totSum

def pr44():
    start = timer()
    #from math, a number x in a pentagon numbers if sqrt(1+24x) is a natural number and 1 + sqrt(1+24x) is divisible 6

    i = 2
    while True:
        a = i*( 3*i - 1 ) // 2
        for j in range(1,i):
            b = j *( 3*j - 1 ) // 2
            sum = (a + b)
            diff = (a - b)
            if ( 1 + 24*sum )**0.5 % 6 == 5 and ( 1 + 24*diff )**0.5 % 6 == 5 :
                print(f'execution time: {timer()-start}')
                return diff
        i += 1

def pr45():
    start = timer()
    i = 144
    while True:
        hexagonal = 2*i*i - i
        #print(f'{i}:{hexagonal}')
        if ( 1 + 8*hexagonal )**0.5 % 2 == 1 and ( 1 + 24*hexagonal )**0.5 % 6 == 5 : # check Tringular, Pentagonal # and ( 1 + 8*hexagonal )**0.5 % 4 == 3 
            break
        i += 1
    print(f'execution time: {timer()-start}')
    return hexagonal

def pr46(): # execution time: 0.624419700121507
    start = timer()

    limit = 10000
    primes = list(sieveOfEratosthenes(limit))
    square = [ 2*i*i for i in range( 1, limit + 1 ) ]
    
    i = 0
    isOddSumOf = True
    while isOddSumOf:
        i += 1
        oddComposite = 2*i + 1
        if oddComposite not in primes:
            isOddSumOf = False
            j = 0
            while j < len(primes) and primes[j] < oddComposite and not isOddSumOf:
                k = 0
                while k < len(square) and primes[j] + square[k] <= oddComposite and not isOddSumOf:
                    if primes[j] + square[k] == oddComposite:
                        isOddSumOf = True
                    k += 1
                j += 1

    print(f'execution time: {timer()-start}')
    return oddComposite

def pr46v2(): # execution time: 0.5417319999542087
    start = timer()

    primes = list({1})
    
    i = 0
    isOddSumOf = True
    while isOddSumOf:
        i += 1
        oddComposite = 2*i + 1
        if isPrime(oddComposite):
            primes.append(oddComposite)
        else:
            isOddSumOf = False
            j = 0
            while j < len(primes) and primes[j] < oddComposite and not isOddSumOf:
                k = 1
                while primes[j] + 2*k*k <= oddComposite and not isOddSumOf:
                    if primes[j] + 2*k*k == oddComposite:
                        isOddSumOf = True
                    k += 1
                j += 1

    print(f'execution time: {timer()-start}')
    return oddComposite

def pr47(): # execution time: 1.8016996998339891
    start = timer()

    distinctPrimeFactors = 4
    
    limit = 1000
    primes = list(sieveOfEratosthenes(limit))
    i = 1
    consecutiveNumber = 0
    while consecutiveNumber < distinctPrimeFactors:
        i += 1
        if findDistintPrimeFactors( i, distinctPrimeFactors, primes ):
            consecutiveNumber += 1
        else:
            consecutiveNumber = 0

    print(f'execution time: {timer()-start}')
    return i - distinctPrimeFactors + 1

def pr48():
    start = timer()

    totSum = 1
    for i in range(2,1000):
        totSum += selfPower(i)

    print(f'execution time: {timer()-start}')
    return totSum % (10**10)

def pr49(): # execution time: 0.008548300014808774
    start = timer()

    primes = [ i for i in sieveOfEratosthenes(10000) if i > 1487 ]

    result = ''
    p = 0
    while p < len(primes) and result == '':
        permutations = sorted( set( [ i for i in findAllPermutations(str(primes[p])) if int(i) in primes] )) # filter for primes with prime permutations
        if len(permutations) > 2:
            result = constantDiff(permutations)
        for perm in permutations:
            primes.remove(int(perm))
        p += 1

    print(f'execution time: {timer()-start}')
    return result

def pr50(): # execution time: 4.094686399912462
    start = timer()

    limit = 1000000
    primes = list(sieveOfEratosthenes(limit))
    limit = primes[-1]
    lenPrimes = len(primes)-1

    maxLength = 0
    sumStart = 0
    while sumStart < lenPrimes:
        p = sumStart
        totSum = 0
        while p < lenPrimes:
            totSum += primes[p]
            currentLength = p - sumStart
            if maxLength > currentLength:
                p += 1
                continue 
            if totSum > limit:
                break
            if totSum in primes and currentLength > maxLength:
                result = totSum
                maxLength = currentLength
            p += 1
        sumStart += 1

    print(f'execution time: {timer()-start}')
    return result


print(f'execution time: {pr50()}')