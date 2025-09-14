from timeit import default_timer as timer

def generateCyclicalNumbers():
    triangle    = lambda n : ( n*n + n )//2
    square      = lambda n : n*n
    pentagonal  = lambda n : ( 3*n*n - n )//2
    hexagonal   = lambda n : ( 2*n*n - n )
    heptagonal  = lambda n : ( 5*n*n - 3*n )//2
    octagonal   = lambda n : ( 3*n*n - 2*n )

    cyclicalNumberFormula = [ triangle, square, pentagonal, hexagonal, heptagonal, octagonal]
    result =                [ [],       [],     [],         [],        [],         []       ]

    for f in cyclicalNumberFormula:
        index = cyclicalNumberFormula.index(f)
        cyclicalPindex = []
        n = 1
        while f(n) < 1000:
            n += 1
        while f(n) < 10000:
            cyclicalPindex.append(str(f(n)))
            n += 1
        result[index] = cyclicalPindex
    return result

def findNextCandidateRecursion( candidates, cyclicalNumbers, cyclicalPi ):
    canditateEnd = candidates[len(candidates)-1][2:4]
    cyclicalNumbers.remove(cyclicalPi)

    if len(cyclicalNumbers) == 0 and candidates[0][0:2] == candidates[len(candidates)-1][2:4]:
        return candidates
    
    # Searches in all the remaining Cyclical Arrays
    for cyclicalPi in cyclicalNumbers:
        for cyclicalPij in cyclicalPi:
            # When the next candidate is found, removes the corresponding Cyclical Arrays and iterates the search
            if canditateEnd == cyclicalPij[0:2]:
                candidatesCopy = candidates.copy()
                candidatesCopy.append(cyclicalPij)
                result = findNextCandidateRecursion( candidatesCopy, cyclicalNumbers.copy(), cyclicalPi )
                if result != None:
                    return result
                break

# 28684 sum of ['8256', '5625', '2512', '1281', '8128', '2882']
def pr61(): # execution time: 0.007534799980930984
    start = timer()
    
    cyclicalNumbers = generateCyclicalNumbers()

    # For the cyclical nature of the solution, makes no difference from which of the Cyclical Arrays is taken the first element of the sequence
    for cyclicalPij in cyclicalNumbers[0]:
        cyclicalNumbersCopy = cyclicalNumbers.copy()
        candidates = findNextCandidateRecursion( [cyclicalPij], cyclicalNumbersCopy, cyclicalNumbersCopy[0] )
        if candidates != None:
            #print(f'sum of {candidates}: {sum([ int(i) for i in candidates])}')
            print(f'execution time: {timer()-start}')
            return sum([ int(i) for i in candidates])

    print(f'execution time: {timer()-start}')
    return 0

print(f'result pr61: {pr61()}')