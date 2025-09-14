from timeit import default_timer as timer
import os

def loadNames(url):
    with open( os.path.dirname(__file__) + '\\' + url, 'r') as f:
        contents = f.read()
        f.close()
    #contents = contents.replace('"','')
    return contents.split(',')

# check if the ascii value is a simbol used in english
def isEnglish(asciiValue):
    if 32 <= asciiValue <= 122 and asciiValue != 64: # from "Space" to "z", excluded "@"
        return True
    return False

# 129448
def pr59(): # execution time: 0.005990499979816377
    start = timer()

    crifer = [ int(i) for i in loadNames('pr59_number.txt') ]

    for x in range(97,122): # i.e. from "a" to "z" in ASCII
        for y in range(97,122):
            for z in range(97,122):
                decryptedText = ''
                asciiSum = 0
                asciiKey = [ x, y, z ]
                for i in range(len(crifer)):
                    asciiValue = crifer[i] ^ asciiKey[i%3]
                    if isEnglish(asciiValue):
                        decryptedText += chr(asciiValue)
                        asciiSum += asciiValue
                    else:
                        break
                if i + 1 == len(crifer):
                    #print(f'Decrypted Text: {decryptedText}')
                    print(f'execution time: {timer()-start}')
                    return asciiSum
    
    return 0

print(f'result pr59: {pr59()}')