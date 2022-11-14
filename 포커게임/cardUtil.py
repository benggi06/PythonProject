import random
SUIT_TUPLE=('Club','Diamond','Heart','Spade')
RANK_TUPLE=('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')

def createDeck():
    deck=[]
    for suit in SUIT_TUPLE:
        for value,rank in enumerate(RANK_TUPLE):
            card={'suit':suit,'rank':rank,'value':value+1}
            deck.append(card)
            
    return deck


def shuffleCards(deck):
    deck=random.shuffle(deck)
    return deck

def viewCardList(cardList):
    
    for i,card in enumerate(cardList):
        print(f"{i+1}. {card['suit']} {card['rank']}")
        
def getCard(deck,numCards):
    cardList=deck[-numCards:]
    del deck[-numCards:]
    
    return cardList

def sortCards(cardList):#숫자,모양순 정렬
    spade=[]
    diamond=[]
    heart=[]
    club=[]
    
    cardList=sorted(cardList,key=lambda x:(x['value']))
    
    for i,card in enumerate(cardList):
        if card['suit'] == 'Spade':
            spade.append(cardList[i])
            
        elif card['suit'] == 'Diamond':
            diamond.append(cardList[i])
            
        elif card['suit'] == 'Heart':
            heart.append(cardList[i])
            
        elif card['suit'] == 'Club':
            club.append(cardList[i])
            
    cardList=club+heart+diamond+spade
            
    return cardList

def handCards(deck,playerCards):
    plusCard=getCard(deck,1)
    
    playerCards=sortCards(playerCards+plusCard)
    
    return playerCards
