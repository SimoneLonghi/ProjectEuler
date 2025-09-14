from timeit import default_timer as timer
from functools import cmp_to_key
import os

cardOrder = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
handValueOrder = ['High Card','One Pair','Two Pairs','Three of a Kind','Straight','Flush','Full House','Four of a Kind','Straight Flush','Royal Flush']

def loadPokerHands():
    with open(os.path.dirname(__file__)+'\\pr54_poker.txt','r') as f:
        contents = f.read()
        f.close()
    return contents.split('\n')

def handValutation(hand):
    # Royal Flush
    if ( hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1] and 
        hand[0][0] == 'T' and hand[1][0] == 'J' and hand[2][0] == 'Q' and hand[3][0] == 'K' and hand[4][0] == 'A' ):
        return ['Royal Flush', '', '']
    
    # Straight Flush
    if ( hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1] and 
        cardOrder.index(hand[0][0]) == (cardOrder.index(hand[1][0]) - 1) == (cardOrder.index(hand[2][0]) - 2) == (cardOrder.index(hand[3][0]) - 3) == (cardOrder.index(hand[4][0]) - 4) ):
        return ['Straight Flush', hand[4][0], '']
    
    # Four of a Kind
    if ( hand[0][0] == hand[1][0] == hand[2][0] == hand[3][0] ):
        return ['Four of a Kind', hand[2][0], hand[4][0] ]
    if ( hand[1][0] == hand[2][0] == hand[3][0] == hand[4][0] ):
        return ['Four of a Kind', hand[2][0], hand[0][0] ]

    # Full House
    if ( ( hand[0][0] == hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0] ) or
         ( hand[2][0] == hand[3][0] == hand[4][0] and hand[0][0] == hand[1][0] ) ):
        return ['Full House', hand[2][0], '']
    
    # Flush
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        return ['Flush', hand[4][0], '']
    
    # Straight
    if cardOrder.index(hand[0][0]) == (cardOrder.index(hand[1][0]) - 1) == (cardOrder.index(hand[2][0]) - 2) == (cardOrder.index(hand[3][0]) - 3) == (cardOrder.index(hand[4][0]) - 4):
        return [ 'Straight', hand[4][0], '']
    
    # Three of a Kind
    for i in range(3):
        countThree = 0
        for j in range(i+1,i+2+1):
            if hand[i][0] == hand[j][0]:
                countThree += 1
                atCard = hand[i][0]
                if countThree == 2:
                    del hand[i:i+3]
                    return [ 'Three of a Kind', atCard, hand ]

    # Two Pairs
    for i in range(2):
        if hand[i][0] == hand[i+1][0]:
            for j in range(i+2,4):
                if hand[j][0] == hand[j+1][0]:
                    atCard = hand[j][0]
                    del hand[j:j+2]
                    del hand[i:i+2]
                    return [ 'Two Pairs', atCard, hand]

    # One Pair
    for i in range(4):
        if hand[i][0] == hand[i+1][0]:
            atCard = hand[i][0]
            del hand[i:i+2]
            return [ 'One Pair', atCard, hand ]
    
    return [ 'High Card', hand[4][0], hand[:4] ]

def pr53(): # execution time: 0.008302000002004206
    start = timer()

    pokerHands = loadPokerHands()
    playerOneWinCount = 0
    
    for hand in pokerHands:
        playerOne = sorted(hand[:14].split(' '), key = cmp_to_key(lambda item1, item2: cardOrder.index(item1[0]) - cardOrder.index(item2[0])))
        playerTwo = sorted(hand[15:].split(' '), key = cmp_to_key(lambda item1, item2: cardOrder.index(item1[0]) - cardOrder.index(item2[0])))
        playerOneRanks = handValutation(playerOne)
        playerTwoRanks = handValutation(playerTwo)
        
        # check the higher rank
        if handValueOrder.index(playerOneRanks[0]) > handValueOrder.index(playerTwoRanks[0]) :
            playerOneWinCount += 1
        elif handValueOrder.index(playerOneRanks[0]) == handValueOrder.index(playerTwoRanks[0]):
            # If two players have the same ranked hands then the rank made up of the highest value wins
            if cardOrder.index(playerOneRanks[1]) > cardOrder.index(playerTwoRanks[1]) :
                playerOneWinCount += 1
            # if the highest cards tie then the next highest cards are compared, and so on.
            elif cardOrder.index(playerOneRanks[1]) == cardOrder.index(playerTwoRanks[1]):
                for card in range(len(playerOneRanks[2])-1, -1, -1):
                    if cardOrder.index(playerOneRanks[2][card][0]) > cardOrder.index(playerTwoRanks[2][card][0]) :
                        playerOneWinCount += 1
                        break
                    elif cardOrder.index(playerOneRanks[2][card][0]) < cardOrder.index(playerTwoRanks[2][card][0]) :
                        break

    print(f'execution time: {timer()-start}')
    return playerOneWinCount

print(f'result pr53  : {pr53()}')