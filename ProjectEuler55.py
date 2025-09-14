from timeit import default_timer as timer

def isPalindrome(n):
    return str(n) == str(n)[::-1]

#249
def pr55(): # execution time: 0.016931199934333563
    start = timer()

    count = 0
    for i in range(10, 10001):
        x = i
        y = int(str(i)[::-1])
        for j in range(1, 51):
            if isPalindrome(x + y):
                break
            elif j == 50:
                count += 1
            x = x + y
            y = int(str(x)[::-1])

    print(f'execution time: {timer()-start}')
    return count

print(f'result pr55: {pr55()}')