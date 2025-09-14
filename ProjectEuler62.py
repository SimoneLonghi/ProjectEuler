from timeit import default_timer as timer

def invertSortDigit(n):
    digitsCount = [ 0 for i in range(0,10)]
    len = -1

    while n > 0:
        digitsCount[ n%10 ] += 1
        len += 1
        n = n//10
    
    for digit in range( 9, -1, -1 ):
        for digitCount in range( 0, digitsCount[digit] ):
            n += digit * 10**len
            len -= 1
    
    return n

def pr62(): # execution time: 0.025604700000258163
    start = timer()

    cubes = { 100**3: [100, 1] }
    i = 100
    while True:
        i += 1
        cube = i**3
        sortedCube = invertSortDigit(cube)
        if sortedCube in cubes:
            cubes[sortedCube][1] += 1
            if cubes[sortedCube][1] == 5:
                print(f'execution time: {timer()-start}')
                return cubes[sortedCube][0]
        else:
            cubes[sortedCube] = [cube, 1]

print(f'result pr62: {pr62()}')