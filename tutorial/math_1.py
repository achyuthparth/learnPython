import copy


listOfCards = []
dictOfCards = {}

dictOfSuits = { #[spade, clover, diamond, heart]
    "2" : [False, False, False, False],
    "3" : [False, False, False, False], 
    "4" : [False, False, False, False], 
    "5" : [False, False, False, False], 
    "6" : [False, False, False, False],
    "7" : [False, False, False, False],
    "8" : [False, False, False, False],
    "9" : [False, False, False, False],
    "J" : [False, False, False, False],
    "Q" : [False, False, False, False],
    "K" : [False, False, False, False],
    "A": [False, False, False, False]
}

rankOrder = ("2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A")
suits = ("spade", "clover", "diamond", "heart")

class Card:
    def __init__(self):
        self.cardRank = None
        self.suit = None
    
    def __init__(self, cardRank, suit):
        self.cardRank = cardRank
        self.suit = str(suit)    
    def getSuit(self):
        return str(self.suit)
        
def RankCounter(cardDict, cardList):
    cardDict = copy.deepcopy(dictOfCards)
    for i in cardList:
        if i.cardRank in cardDict:
            cardDict[i.cardRank] += 1
        if i.cardRank not in cardDict:
            cardDict[i.cardRank] = 1
    return cardDict


def TwoKind(cardDict, cardList):
    for rank in cardDict:
        if cardDict[rank] >= 2:
            return 1.0
        
    Sigma = sum((4-cardDict[rank]) for rank in cardDict if cardDict[rank] == 1)

    return (
        float(Sigma)
        / float(52 - len(cardList))
    )
    
def ThreeKind(dictOfCards, listOfCards):
    for rank in dictOfCards:
        if cardDict[rank] >= 3:
            return 1.0
        
    Sigma = sum((4-cardDict[rank]) for rank in dictOfCards if cardDict[rank] == 2)
    return (
        float(Sigma)
        / float(52 - len(listOfCards))
    )
    
def FourKind(dictOfCards, listOfCards):
    for rank in dictOfCards:
        if dictOfCards[rank] >= 4:
            return 1.0
        
    Sigma = sum((4-dictOfCards[rank]) for rank in dictOfCards if dictOfCards[rank] == 3)
    return (
        float(Sigma)
        / float(52 - len(listOfCards))
    )

def TwoPair(dictOfCards, listOfCards):
    pairCounter = 0
    for rank in dictOfCards:
        if dictOfCards[rank] >= 2:
            pairCounter += 1
        if pairCounter >= 2:
            return 1.0
    if pairCounter == 0:
        return 0.0


    Sigma = sum((4-dictOfCards[rank]) for rank in dictOfCards if dictOfCards[rank] == 1)
    chance = (
        float(Sigma)
        / float(52 - len(listOfCards))
    )

    returnValue = chance + FourKind(dictOfCards, listOfCards)
    return min(returnValue, 1.0)
    
def FullHouse(dictOfCards, listOfCards):
    if len(listOfCards) < 4:
        return 0.0

    if FourKind(dictOfCards, listOfCards) != 1.0:
        if ThreeKind(dictOfCards, listOfCards) == 1.0:
            return TwoPair(dictOfCards, listOfCards)
        if TwoPair(dictOfCards, listOfCards) == 1.0:
            return ThreeKind(dictOfCards, listOfCards)
    if FourKind(dictOfCards, listOfCards) == 1.0:
        Sigma = sum((4-cardDict[rank]) for rank in dictOfCards if cardDict[rank] == 1)
        Sigma2 = sum((4-cardDict[rank]) for rank in dictOfCards if cardDict[rank] == 2)
        return (
            1.0
            if Sigma2 >= 1
            else (float(Sigma) / float(52 - len(listOfCards)))
        )
    return 0.0            
    
def Straight(dictOfCards, listOfCards, rankOrder):
    seqCount = 0
    for i in range(len(rankOrder) - 1):
        if rankOrder[i] in dictOfCards:
            seqCount += 1
        if rankOrder[i] not in dictOfCards:
            seqCount = 0
        if seqCount == 4:
            if rankOrder[i+1] in dictOfCards:
                return 1.0
            break
    if seqCount < 4:
        return 0.0

    if rankOrder[0] in dictOfCards and rankOrder[1] in dictOfCards and rankOrder[2] in dictOfCards and rankOrder[3] in dictOfCards:
        return (
        float(4)
        / float(52 - len(listOfCards))
    )
    if  rankOrder[len(rankOrder) - 1] in dictOfCards and rankOrder[len(rankOrder) - 2] in dictOfCards and rankOrder[len(rankOrder) - 3] in dictOfCards and rankOrder[len(rankOrder) - 4] in dictOfCards:
        return (
        float(4)
        / float(52 - len(listOfCards))
    )
    return (
        float(8)
        / float(52 - len(listOfCards))
    )



cardList = copy.deepcopy(listOfCards)
cardDict = copy.deepcopy(dictOfCards)
suitDict = copy.deepcopy(dictOfSuits)
while True:
    
    print(f"enter rank: {rankOrder}")
    cardRank = input()
    print(f"enter suit: {suits}")
    suit = input()

    cardList.append(Card(cardRank, suit))
    for x in range(len(cardList)):
        print(f"{cardList[x].cardRank} of {cardList[x].suit}")

    cardDict = RankCounter(cardDict, cardList)
    print(cardDict)

    print(f"Probability of two of a kind on next turn: {TwoKind(cardDict, cardList)}")
    print(f"Probability of three of a kind on next turn: {ThreeKind(cardDict, cardList)}")
    print(f"Probability of four of a kind on next turn: {FourKind(cardDict, cardList)}")
    print(f"Probability of two pair on next turn: {TwoPair(cardDict, cardList)}")
    print(f"Probability of full house on next turn: {FullHouse(cardDict, cardList)}")
    print(f"Probability of straight on next turn: {Straight(cardDict, cardList, rankOrder)}")
    

    if len(cardList) >= 7:
        break