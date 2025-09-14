from timeit import default_timer as timer

# 972
def pr56(): # execution time: 0.004105999949388206
    start = timer()

    max = 0
    for a in range(90, 101):
        j = a
        for b in range(1, 101):
            jSumDigits = sum(map(int, str(j)))
            max = jSumDigits if jSumDigits > max else max
            j = j*a

    print(f'execution time: {timer()-start}')
    return max

print(f'result pr56: {pr56()}')