from timeit import default_timer as timer
# a,b,c Pythagorean triple if a = m**2 - n**2, b = 2*m*n and c = m**2 + n**2, with m > n > 0
# a,b,c primiteve Pythagorean triple if and only if a,b,c Pythagorean triple, m,n are coprime and exatly one of them is even 

def coprime(a, b):
    while b:
        a, b = b, a % b
    return a == 1

def pr75(): # execution time: 0.1668814000004204
    start = timer()

    maxL = 1_500_000
    lengthTriangleCount = [0] * (maxL + 1)

    n,m = 1,2
    maxM = maxL // 2    
    while m*(m + 1) < maxM:
        while n < m:
            if coprime(n,m) and (m-n) % 2 == 1:
                primitiveL = 2*m*(m+n) # m and n generate a primiteve Pythagorean triple (a,b,c)
                l = primitiveL
                while l <= maxL:
                    lengthTriangleCount[l] += 1
                    l += primitiveL # search for non-primitive triples k*(a,b,c)
            n += 1
        n = 1
        m += 1

    print(f'execution time: {timer()-start}')
    return  sum(count == 1 for count in lengthTriangleCount)

print(f'result pr75: {pr75()}')