from math import floor,sqrt
from timeit import default_timer as timer
import re
import os

def charValue(c):
    alphabet = ['null','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return alphabet.index(c)

def loadNames(url):
    with open( os.path.dirname(__file__) + '\\' + url, 'r') as f:
        contents = f.read()
        f.close()
    contents = contents.replace('"','')
    return contents.split(',')

def isPrime(n):
    i=2
    if n <= 0 or n != floor(n):
        return False
    while i < floor(sqrt(n))+1:
        if n % i == 0:
            return False
        i+=1
    return True

def isSquared(n):
    for i in range(1, floor(n/2)+1):
        if i**2 == n:
            return True
    return False

def countConsecutivePrime(a,b):
    count = 0
    n=0
    while isPrime(n*n+a*n+b):
        n = n+1
        count = count + 1
    return count

def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    elif n == 1:
        return n
    else:
        return 0
    
def countDivisors(n):
    count = 0
    for i in range(1, floor(sqrt(n))+1):
        if n % i == 0:
            if (n / i == i):
                count += 1
            else:
                count += 2
    return count

def isAbundant(n):
    count = 0
    for i in range(1, floor(n/2)+1):
        if n % i == 0:
            count += i
    return ( n < count )

def sieveOfEratosthenes(tillNumber):
    sieve = set([ i for i in range( 2, tillNumber)])
    for i in range(2, int(sqrt(tillNumber)) +1):
        j = 2
        while j*i < tillNumber :
            sieve.discard(j*i)
            j += 1
    return sieve

def sieveOfEratosthenesForCircular(tillNumber):
    sieve = set([ i for i in range( 2, tillNumber)])
    #toEliminate = list({'0','2','4','5','6','8'})
    for i in range(2, int(sqrt(tillNumber)) +1):
        j = 2
        while j*i < tillNumber :
            sieve.discard(j*i)
            j += 1
    for i in range( 10, tillNumber):
        if '0' in str(i) or '2' in str(i) or '4' in str(i) or '5' in str(i) or '6' in str(i) or '8' in str(i):
        #for j in range(len(toEliminate)):
            #if toEliminate[j] in str(i): 
            # solution discarded, less efficient
            sieve.discard(i)
    return sieve

def findCircular(n):
    nStr = str(n)
    primeCircularing = set()
    for i in range(0, len(nStr)):
        newnumber = ''
        for j in range(len(nStr)):
            newnumber += nStr[j-i]
        primeCircularing.add(int(newnumber))
    return primeCircularing

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def toBinary(decimal):
    return int(toBinaryRecursion(decimal, ''))

def toBinaryRecursion(decimal, binaryStr):
    if decimal == 1:
        return '1' + binaryStr
    elif decimal < 1:
        return '0' + binaryStr
    elif decimal > 1:
        if decimal % 2 == 0:
            return toBinaryRecursion( decimal // 2, '0' + binaryStr)
        else:
            return toBinaryRecursion( decimal // 2, '1' + binaryStr)

def isLeftTruncatablePrime(n):
    nstr = str(n)
    for i in range(1,len(nstr)):
        if not isPrime(int(nstr[i:])) or nstr[i:] == '1':
            return False
    return True

def isRightTruncatablePrime(n):
    nstr = str(n)
    for i in range(1,len(nstr)+1):
        if not isPrime(int(nstr[:i])) or nstr[:i] == '1':
            return False
    return True

def pr21():
    n = 10000
    d = [ 0 for i in range(n+1) ]
    amicable = []

    for i in range(2,n+1):
        for j in range(1,floor(i/2)+1):
            if i % j == 0:
                d[i] += j

    for i in range(2,n+1):
        if d[i] <= n and i != d[i] and i == d[d[i]]:
            amicable.append(i)
            amicable.append(d[i])

    amicable = list(dict.fromkeys(amicable)) #remove duplicates
    return sum(amicable)

def pr22():
    names = loadNames('p022_names.txt')
    names = sorted(names)
    
    totScore = 0 
    for i in range(len(names)):
        nameScore = 0
        for j in range(len(names[i])):
            nameScore += charValue(names[i][j].casefold())
        totScore += nameScore*(names.index(names[i])+1)
    return totScore

def pr23():
    n = 28123
    abundantSum = set([])
    abundant = [i for i in range(12,28124) if isAbundant(i)]

    for a in abundant:
        for b in abundant:
            sumAb = a + b
            if sumAb <= n:
                abundantSum.add(sumAb)
            else:
                break

    return sum([i for i in range(n+1) if i not in abundantSum])

def pr24( nOfDigits, nToGet):
    #0123
    nToGet = nToGet - 1
    digits = [ i for i in range(nOfDigits) ]
    result = ''
    return pr24recursion(digits, nToGet, result )

def pr24recursion( digits, nToGet, result):
    if len(digits) > 0 :
        steps = factorial(len(digits)) / len(digits)
        k = digits[floor( nToGet / steps ) % len(digits)]
        digits.remove(k)
        #print(f'call: {digits},{nToGet - steps}, {result + str(k)}')
        return pr24recursion( digits, nToGet - steps, result + str(k))
    else:
        return result

def pr25():
    phi = 1.618034
    rad5 = sqrt(5)
    n1 = 1473
    f1 = floor( ( phi**n1 - (1-phi)**n1 ) / rad5 )
    n2 = 1474
    f2 = floor( ( phi**n2 - (1-phi)**n2 ) / rad5 )

    n = 1475
    fn = f1 + f2
    while len(str(fn)) < 1000:
        f1 = fn
        fn = fn + f2
        f2 = f1
        n = n + 1
    return n

def pr26():
    limit = 1000
    longestRecurringCycle = 0
    longestValue = 0
    primeNumbers = []

    for i in range(2, limit):
        if isPrime(i):
            primeNumbers.append(i)

    for d in primeNumbers:
        fraction = str(1/d)
        count = 1
        if len(fraction) > 15:
            for index, recurringCycle in enumerate(fraction[3:10]):
                if recurringCycle == fraction[2] and recurringCycle == fraction[index + 3 + count]:
                    break
                elif count >= longestRecurringCycle:
                    longestRecurringCycle = count
                    longestValue = d
                count += 1
    return longestValue

def pr27():
    maxProd = 0
    maxCount = 0
    for a in range(-1000, 1000):
        for b in range(0, 1000):
            delta = a*a - 4*b
            if isPrime(b):
                countForAnB = countConsecutivePrime(a,b)
                if countForAnB > maxCount:
                    maxCount = countForAnB
                    maxProd = a*b
    return maxProd

def pr28():
    sum = 1
    n = 1
    for s in range(3, 1001+1, 2):
        while n < s*s:
            n += s-1
            sum += n
    return sum

def pr29():
    n = 100
    sequence = set([])

    for a in range( 2, n + 1 ):
        i = a
        b = 2
        while b < n + 1 :
            a = a*i
            sequence.add(a)
            b += 1
    return len(sequence)

def toFifth(i):
  return i ** 5

def pr30():
    power = list( map( toFifth, range(0,10) ))
    sum = 0
    i = 2
    upperBound = (9**5)*6
    while i < upperBound:
        iChar = str(i)
        sumOfpowers = 0
        for j in range(len(iChar)):
            sumOfpowers += power[int(iChar[j])]
        if i == sumOfpowers:
            sum += i
        i += 1

# To rebuild
def pr31(): # execution time: 1.3960900999954902
    #1,2,5,10,20,50,100,200
    start = timer()
    nOfWays = 1
    toAmount = 200
    for onep in range(0, toAmount +1):
        coins = [0] * 5
        coins[0] = onep
        for twop in range(0, toAmount +1, 2):
            coins[1] = twop
            if onep + twop == toAmount:
                nOfWays += 1
                break
            elif onep + twop > toAmount:
                break
            for fivep in range(0, toAmount+1, 5): 
                if onep + twop + fivep == toAmount:
                    nOfWays += 1
                    break
                elif onep + twop + fivep > toAmount:
                    break
                for tenp in range(0,toAmount+1, 10):
                    if onep + twop + fivep + tenp == toAmount:
                        nOfWays += 1
                        break
                    elif onep + twop + fivep + tenp > toAmount:
                        break
                    for twentyp in range(0,toAmount+1, 20):
                        if onep + twop + fivep + tenp + twentyp == toAmount:
                            nOfWays += 1
                            break
                        elif onep + twop + fivep + tenp  + twentyp > toAmount:
                            break
                        for fiftyp in range(0,toAmount+1, 50):
                            if onep + twop + fivep + tenp + twentyp + fiftyp == toAmount:
                                nOfWays += 1
                                break
                            elif onep + twop + fivep + tenp  + twentyp + fiftyp > toAmount:
                                break
                            for onePence in range(0,toAmount+1, 100):
                                sumOfCoins = onep + twop + fivep + tenp + twentyp + fiftyp + onePence
                                if sumOfCoins == toAmount:
                                    nOfWays += 1
                                elif sumOfCoins > toAmount:
                                    break
    end = timer()
    print(f'execution time: {end-start}')
    return nOfWays

def pr31v2(): # 7.329997606575489e-05
    start = timer()
    toAmount = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    nOfWays = [1] + [0]*toAmount

    for coin in coins:
        for i in range( coin, toAmount + 1 ):
            nOfWays[i] += nOfWays[i-coin]
            # print( 'i: ', i, ', coin: ',coin, ', ways: ',ways )

    print(f'execution time: {timer()-start}')
    return nOfWays[toAmount]

def pr32():
    #max 1-through-9 pandigital: 7852 = 1963 x 4
    #found through number manipulation and a bit of brute force
    start = timer()

    totSum = 0
    alreadyFind = set()
    isPandigital = re.compile(r'^(?!.*([1-9]).*\1)[1-9]{9}$')

    for i in range(4, 1964):
        for j in range(i, 1964):
            prod = i*j
            if prod > 7852 or prod in alreadyFind:
                break
            totDigits = len(str(i)) + len(str(j)) + len(str(prod))
            allDigits = str(i) + str(j) + str(prod)
            if totDigits == 9 and isPandigital.match(allDigits) != None:
                alreadyFind.add(prod)
                totSum += prod 
                #print(f'{prod} = {i} x {j}')
    
    print(f'execution time: {timer()-start}')
    return totSum

def pr33():
    start = timer()
    numOfProd = 1
    denOfProd = 1
    for i in range(10, 100):
        for j in range(i, 100):
            istr = str(i)
            jstr = str(j)
            if i != j and i % 10 != 0 and j % 10 != 0:
                for k in range(0, 2):
                    for l in range(0, 2):
                        if i*int(jstr[k]) == j*int(istr[l]) and int(jstr[1-k]) == int(istr[1-l]):
                            #print(f'{i}/{j} = {istr[l]}/{jstr[k]}')
                            numOfProd *= int(istr[l])
                            denOfProd *= int(jstr[k])
    #print(f'{numOfProd}/{denOfProd}')
    i = 1
    while i < min(numOfProd,denOfProd):
        i += 1
        if numOfProd % i == 0 and denOfProd % i == 0:
            numOfProd = numOfProd // i
            denOfProd = denOfProd // i
            i = 1
    #print(f'{numOfProd}/{denOfProd}')
    print(f'execution time: {timer()-start}')
    return denOfProd

def pr34():
    factorialList = [1] * 10
    fct = 1
    for i in range(2,10):
        fct *= i
        factorialList[i] = fct

    totSum = 0
    upperBound = factorialList[9] * 7
    for i in range(10, upperBound):
        sumOfFactorial = sum(factorialList[int(c)] for c in str(i))
        if i == sumOfFactorial:
            totSum += i
    return totSum

def pr35(tillNumber):
    start = timer()
    primeNumbers = sieveOfEratosthenesForCircular(tillNumber)
    i = 1
    maxPrime = max(primeNumbers)
    while i < maxPrime:
        i += 1
        if i in primeNumbers:
            circularNumbers = findCircular(i)
            if not circularNumbers.issubset(primeNumbers):
                primeNumbers = primeNumbers - circularNumbers
    print(f'execution time: {timer()-start}')
    #print(f'{sorted(primeNumbers)}')
    return len(primeNumbers)

def pr36(tillNumber):
    start = timer()

    totSum = 0
    decimal = [ i for i in range(1, tillNumber+1)]
    #binary = [ int(str(bin(i))[2:]) for i in range(1, tillNumber+1)] #execution time: 0.38091170002007857
    binary = [ toBinary(i) for i in range(1, tillNumber+1)] #execution time: 1.9470856999978423
    #print(f'{binary}')
    for i in range(tillNumber):
        if isPalindrome(decimal[i]) and isPalindrome(binary[i]):
            totSum += decimal[i]

    print(f'execution time: {timer()-start}')
    return totSum

def pr37(): #[23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
    totSum = 0
    count = 0
    digitsToAdd = set({1,2,3,5,7,9})
    currentNumbers = set({2,3,5,7})

    while count < 11:
        nextNumbers = set()
        for i in currentNumbers:
            for j in digitsToAdd:
                nToCheck = int(str(i)+str(j))
                nextNumbers.add(nToCheck)
                if isRightTruncatablePrime(nToCheck) and isLeftTruncatablePrime(nToCheck):
                    #print(nToCheck)
                    totSum += nToCheck
                    count += 1
                    """ if count == 11:
                        return totSum """
        currentNumbers = nextNumbers
    #print(count)
    return totSum

def pr38():
    start = timer()

    isPandigital = re.compile(r'^(?!.*([1-9]).*\1)[1-9]{9}$')
    
    candidateFactor = 99999
    while candidateFactor > 8:
        factor = str(candidateFactor)
        n = 1
        while len(factor) < 10:
            n += 1
            factor += str(candidateFactor*n)
            if isPandigital.match(factor) != None:
                print(f'execution time: {timer()-start}')
                return factor
        candidateFactor -= 1

    print(f'execution time: {timer()-start}')
    return 0

def pr39(): # execution time: 1.1758025999879465
    start = timer()

    solution = [1 for i in range(0,1000+1)]

    for a in range(2,334):
        for b in range(a,667):
            for c in range(b,b+a+1): #triangle inequality
                p = a + b + c
                if p <= 1000 and a*a + b*b == c*c:
                    solution[p] += 1 

    print(f'execution time: {timer()-start}')
    return solution.index(max(solution))

def pr39v2(): # execution time: 0.5696505000232719
    start = timer()

    squared = [ i*i for i in range(0,1000+1)]
    solution = [1 for i in range(0,1000+1)]

    for a in range(2,334):
        for b in range(a,667):
            csquared = a*a + b*b
            if csquared in squared:
                p = a + b + squared.index(csquared)
                if p <= 1000:
                    solution[p] += 1 

    print(f'execution time: {timer()-start}')
    return solution.index(max(solution))

def champernowneConstantDigit(positionToFind):
    # 9 th                      -> 9
    # 9*2*10 th                 -> 99
    # 9 + 9*2*10 + 9*3*100 th   -> 999
    # Start from the nearest known number
    firstOfThDigits = 0
    nDigits = 0
    while positionToFind > firstOfThDigits + 9*(nDigits+1)*(10**(nDigits)):
        firstOfThDigits += 9*(nDigits+1)*(10**(nDigits))
        nDigits += 1
        firstNumberOfThDigits = 10**(nDigits)
    nDigits += 1

    positionToFindFromNearestKnownNumber = positionToFind - firstOfThDigits - 1
    numberInPositionToFind = (( positionToFindFromNearestKnownNumber ) // nDigits ) + firstNumberOfThDigits
    digitDesidered = ( positionToFind - firstOfThDigits - 1 ) % nDigits
    
    return int(str(numberInPositionToFind)[digitDesidered])

def pr40():
    start = timer()
    
    prod = 1
    i = 1
    while i < 7:
        prod *= champernowneConstantDigit(10**i)
        i += 1
    
    print(f'execution time: {timer()-start}')
    return prod

# print(f'pr40: {pr40()}')