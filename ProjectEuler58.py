from math import floor,sqrt
from timeit import default_timer as timer

def isPrime(n):
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

def pr58(): # execution time: 1.6567981999833137
    start = timer()

    numerator = 1
    denominator = 1
    side = 0
    diagonalElement = 1
    #ratio = 100
    while 10*numerator > denominator :
        side += 2
        for j in range(0, 3): # excluded the numbers at the botton right corner of the square, they are squares of odd numbers (2n+1)**2 (-1 sec of running time)
            diagonalElement += side
            if isPrime(diagonalElement):
                numerator += 1
        diagonalElement += side
        denominator += 4
        #ratio = (100*numerator) / denominator  #slight optimization
    print(f'execution time: {timer()-start}')
    return side + 1

print(f'result pr58: {pr58()}')