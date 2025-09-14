from timeit import default_timer as timer

def pr57(): # execution time: 0.0014522999990731478
    start = timer()
    
    # let's do some maths
    # f(i) = n(i)/d(i)
    #      = 1 + 1/( 1 + f(i-1) )
    #      = 1 + 1/( 1 + n(i-1)/d(i-1) )
    #      = ( 2*d(i-1) + n(i-1) )/( d(i-1) + n(i-1) )

    count = 0
    previousNumerator, previousDenominator = 3, 2

    for i in range(1,1000):
        numerator = 2*previousDenominator + previousNumerator
        denominator = previousDenominator + previousNumerator
        if len(str(numerator)) > len(str(denominator)):
            count += 1     
        previousNumerator, previousDenominator = numerator, denominator

    print(f'execution time: {timer()-start}')
    return count

print(f'result pr57: {pr57()}')