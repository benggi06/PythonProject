import cardUtil as cu

def compareShape(pCard,dCard):
    psn=0 #클로버는 0 디폴트
    dsn=0 
    if pCard[-1]['suit']=='Spade':psn=4
    elif pCard[-1]['suit']=='Diamond':psn=3
    elif pCard[-1]['suit']=='Heart':psn=2
    
    if dCard[-1]['suit']=='Spade':dsn=4
    elif dCard[-1]['suit']=='Diamond':dsn=3
    elif dCard[-1]['suit']=='Heart':dsn=2
        
    if psn>dsn: return 'Player win'
    
    elif psn<dsn: return 'Dealer win'
    
def compareNum(pCard,dCard):
    #스트레이트일때
    if pCard[-1]['value']>dCard[-1]['value']: return 'Player win'
    elif pCard[-1]['value']>dCard[-1]['value']: return 'Dealer win'
    
def isFlush(cards):
    
    suit = cards[0]['suit']
    isFlush = True
    
    for card in cards:
        if card['suit'] != suit:
            isFlush = False
            break
            
    if isFlush:
        return True
    else:
        return 
    
def isStraight(cardList):
    sortNumcard=sorted(cardList,key=lambda x:(x['value']))#숫자순 배열
    
    isStraight=True
    count=0
    for i in range(sortNumcard[0]['value'],sortNumcard[-1]['value']):
        if i != sortNumcard[count]['value']:
            isStraight=False
            break
        
        count+=1
    if isStraight:
        return True
    else:
        return 

def is4Cards(cardList):
    numList=[]
    for i,card in enumerate(cardList):
        numList.append(card['value'])
        
    for i in numList:
        if numList.count(i)== 4:
            return True
    else:
        return 
    
def is3Cards(cardList):
    numList=[]
    for i,card in enumerate(cardList):
        numList.append(card['value'])
        
    for i in numList:
        if numList.count(i)== 3:
            return True
        else:
            return 
    
def is2Pair(cardList):
    numList=[]
    countList=[]
    for i,card in enumerate(cardList):
        numList.append(card['value'])
        
    for i in numList:
        countList.append(numList.count(i))
    
    if countList.count(2) == 4:
        return True
    
    else:
        return 
    
def is1Pair(cardList):
    numList=[]
    countList=[]
    for i,card in enumerate(cardList):
        numList.append(card['value'])
        
    for i in numList:
        countList.append(numList.count(i))
    
    if countList.count(2) == 2:
        return True
    
    else:
        return  
        
def isHigh(cardList):
    sortNumcard=sorted(cardList,key=lambda x:(x['value']))
    
    return cardList[-1]['value']


def rank(card):
    if isFlush(card):
        return 6
    
    elif isStraight(card):
        return 5
    
    elif is4Cards(card):
        return 4
    
    elif is3Cards(card):
        return 3
    
    elif is2Pair(card):
        return 2
    
    elif is1Pair(card):
        return 1
    
    else:#모양
        return 0

def compare(pRank,dRank,pCard,dCard):
    pCard=sorted(pCard,key=lambda x:(x['value']))
    dCard=sorted(dCard,key=lambda x:(x['value']))
    
    if pRank>dRank:
        print('사용자의 승리입니다.')
        
        return 'Player win'
        
    elif pRank<dRank:
        print('딜러의 승리입니다.')
        print(dRank)
        return 'Dealer win'
    
    else:
        
        if pRank+dRank==12: return compareShape(pCard,dCard)
        elif pRank+dRank==10: return compareNum(pCard,dCard)
        
        elif pRank+dRank==0:#하이 카드일때
            if pCard[-1]['value']>dCard[-1]['value']:
                print('사용자의 승리입니다.')

                return 'Player win'

            elif pCard[-1]['value']<dCard[-1]['value']:
                print('딜러의 승리입니다.')

                return 'Dealer win'
            
            else:#숫자동일시
                return compareShape(pCard,dCard)
        else:
            print('무승부입니다.')
            return 'Draw'
            
            
