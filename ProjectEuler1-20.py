from math import floor,sqrt
from numpy import prod
from num2words import num2words
import os
import re
import datetime 
from timeit import default_timer as timer

def pr1(n):
    start = timer()
    sum = 0
    n = n - 1
    m = n // 3
    sum += 3*m*(m+1)//2
    m = n // 5
    sum += 5*m*(m+1)//2
    m = n // 15
    sum -= 15*m*(m+1)//2
    print(f'execution time: {timer()-start}')
    return sum

def pr2():
    sum = 2
    firstTerm = 1
    secondTerm = 2
    nextTerm = 3
    i=0
    while nextTerm < 4000000:
        i += 1
        nextTerm = firstTerm + secondTerm
        if i == 3:
            sum += nextTerm
            i=0
        firstTerm = secondTerm
        secondTerm = nextTerm 
    print(f'{sum}')

def pr3(n):
    x = list(range(0, floor(sqrt(n))+1))
    i = 2
    while i < floor(sqrt(n))+1:
        if x[i] != 0 and not n % i == 0:
            x[i] = 0 
        if x[i] != 0:
            j = 2
            while i*j < floor(sqrt(n))+1:
                x[i*j] = 0
                j+=1
        i += 1
    print(f'{max(x)}')

def pr4():
    maxPalindrome = 0
    tmp = 0
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            tmp = i*j
            if ( isPalindrome(tmp) and tmp > maxPalindrome ):
                maxPalindrome = tmp
    print(f'{maxPalindrome}')

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def pr5(n):
    x=list(range(1,n+1))
    primes = primeBefore(n)
    for i in range(2,n+1):
        for j in range(i+1,n+1):
            if x[i-1] in primes and x[j-1] % x[i-1] == 0:
                x[j-1] = int(x[j-1]/x[i-1])
    print(f'{prod(x)}')
    return prod(x)

def primeBefore(n):
    x = list(range(1,n+1))
    for i in range(1,n):
        if x[i] != 0:
            for j in range(i+1,n):
                if x[j] % x[i] == 0:
                    x[j] = 0
    return x

def pr6(n):
    sumOfSquare = 0
    squareOfSum = 0
    for i in range(0, n+1):
        sumOfSquare += i*i
        squareOfSum += i
    result = (squareOfSum*squareOfSum) - sumOfSquare
    print(f'{result}')

def pr7(n):
    count=0
    i = 2
    while count < n:
        if isprime(i):
            count += 1
        i += 1
    print(i-1)

def isprime(n):
    i=2
    while i < floor(sqrt(n))+1:
        if n % i == 0:
            return False
        i+=1
    return True

def pr8(n):
    with open(os.path.dirname(__file__)+'\\pr8_number.txt','r') as f:
        x = f.read()
        f.close()
    x = x.replace('\n','')
    max = 0
    for i in range(0, len(x)-n):
        j=0
        prod = 1
        while j < n: 
            prod *= int(x[i+j])
            j += 1
        if prod > max:
            max = prod
    print(max)

def pr9():
    for a in range(1, 1001):
        for b in range(a, 1001):
            c = 1000 - a - b
            if c > b and a*a + b*b == c*c:
                print(a*b*c)
    print('serch end')

def isprime2(n):
    i=5
    if n % 3 == 0:
        return False
    while i < floor(sqrt(n))+1:
        if n % i == 0:
            return False
        if n % (i+2) == 0:
            return False
        i+=6
    return True

def pr10(n):
    sum = 2+3+5+7
    for i in range(9, n+1,2):
        if isprime2(i):
            sum += i
    print(f'{sum}')

def pr11():
    #data preparation
    with open(os.path.dirname(__file__)+'\\pr11_number.txt','r') as f:
        x = f.read()
        f.close()
    x = x.replace('\n',' ')
    x = list(x.split(' '))
    y = [[int(x[ j*20 + i ]) for i in range(20)] for j in range(20)]
    k = 0
    #compute 
    max = 0
    for i in range(0,20):
        for j in range(0,20):
            if j <= 16:
                k = y[i][j]*y[i][j+1]*y[i][j+2]*y[i][j+3] # search in col
                if k > max:
                    max = k
            if i <= 16:
                k = y[i][j]*y[i+1][j]*y[i+2][j]*y[i+3][j] # search in row
                if k > max:
                    max = k
            if j <= 16 and i <= 16:                       # search diagonally
                k = y[i][j]*y[i+1][j+1]*y[i+2][j+2]*y[i+3][j+3]
                if k > max:
                    max = k
                k = y[i][j+3]*y[i+1][j+2]*y[i+2][j+1]*y[i+3][j]
                if k > max:
                    max = k
    print(f'{max}')

def pr12(n):
    i = 1
    triangle = 1
    while True:
        count = countDivisors(triangle)
        if count > n:
            return triangle
        i += 1
        triangle += i

def countDivisors(n):
    count = 0
    for i in range(1, floor(sqrt(n))+1):
        if n % i == 0:
            if (n / i == i):
                count += 1
            else:
                count += 2
    return count

def pr13():
    #data preparation
    with open(os.path.dirname(__file__)+'\\pr13_number.txt','r') as f:
        x = f.read()
        f.close()
    x = x.split('\n')
    
    return str(sum( [ int(i) for i in x ] ))[0:10]

def nextTerm(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return 3*n + 1

def pr14():
    chainCounts = {'startTerm': 'chainCount' }
    result = 0
    max = 0
    for i in range(3,(10**6)+1):
        count = 1
        chainTerm = nextTerm(i)
        if chainCounts.get(chainTerm):
            chainCounts[i] = chainCounts.get(chainTerm)
        else:
            j = chainTerm
            while j > 1:
                count += 1
                j = nextTerm(j)
                if chainCounts.get(j):
                    count += chainCounts.get(j)
                    j = 1
            chainCounts[chainTerm] = count
        if count > max:
            max = count
            result = i
    return result

def pr15(n):
    return int( prod( [ (2*n+1-i)/i for i in range(1,n+1) ] ) )

def binomialCoeff(n,k):
    if k == 0 or k == n:
        return 1
    else:
        return binomialCoeff(n-1,k) + binomialCoeff(n-1,k-1)

def pr16():
    x = 2**1000
    x = str(x)
    summy = 0
    for i in range(len(x)):
        summy += int(x[i])
    return summy
 
def pr17(n):
    inWords = ''
    for i in range(1, n+1):
        inWords += num2words(i) #cheating? Maybe.
    return len( re.findall( "[a-z]", inWords ) ) # removing spaces or hyphens

def pathFinder(x):
    rowNum = 0
    while rowNum*(rowNum + 1)/2 != len(x):
        rowNum += 1
    #print(f'row number: {rowNum}')

    y = [[ 0 for i in range(j) ] for j in range(1,rowNum+1)]

    k = 0
    for j in range(0,rowNum):
        for i in range(j+1):
            y[j][i] = int(x[k])
            k += 1

    #path search
    for j in reversed(range(rowNum-1)):
        for i in range(j+1):
            y[j][i] += max(y[j+1][i],y[j+1][i+1])
            #print(f'j: {j}, i: {i}')

    return y[0][0]

def pr18():
    #data preparation
    with open(os.path.dirname(__file__)+'\\pr18_number.txt','r') as f:
        x = f.read()
        f.close()
    x = x.split()
    x = [ int(i) for i in x ]
    return pathFinder(x)

def pr67():    
    #data preparation
    with open(os.path.dirname(__file__)+'\\pr67_number.txt','r') as f:
        x = f.read()
        f.close()
    x = x.split()
    x = [ int(i) for i in x ]
    return pathFinder(x)

def pr19():
    count = 0
    for y in range(1901, 2000 +1):
        for m in range(1, 12 +1):
            if datetime.datetime(y, m, 1).weekday() == 6:
                count += 1
    return count

def pr20(n):
    p = 1
    s = 0
    for i in reversed(range(n)):
        p *= i+1
    p = str(p)
    for i in range(len(p)):
        s += int(p[i])
    return s

#print(f'{pr20(100)}')