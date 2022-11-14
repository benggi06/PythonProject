import GameUtil as gu
import cardUtil as cd
import Ranking as rk
         
def pokerGame(dealer,player,money):
    SUIT_TUPLE=('Club','Diamond','Heart','Spade')
    RANK_TUPLE=('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')
    pMoney,dMoney=money,money
    
    gameCount=1
    
    
    #시작멘트
    print('곧 포커 게임이 시작됩니다.')
    gu.stopTime(3)
    print(f'모양은 다음과 같습니다.{SUIT_TUPLE}')
    print(f'숫자는 다음과 같습니다.{RANK_TUPLE}')
    print(f'사용자: {player}, 상대: {dealer}')
    print(f'서로에게 지급된 돈은 다음과 같습니다. {money}')
    
    print()
    
    #족보 설명
    print('족보는 다음과 같습니다.')
    print('''
    Flush : 모든 카드 모양이 동일
    Straight: 카드가 모두 연속적일 때 ex) 1,2,3,4,5
    Four Card: 숫자 4개가 동일할 때
    Triple: 숫자 3개가 동일할 때
    Two Pair: 같은 숫자를 가진것이 두 개일 때 ex) 2,2,4,4,5
    One Pair: 같은 숫자를 가진것이 한 개일 때 ex) 2,2,3,4,5
    High Card: 가장 높은 숫자
    
    [주의1]: 같은 족보가 나왔을 시 Spade<- Diamond<- Heart<- Club 순으로 우위를 점합니다.
    [주의2]: 3번째 카드부터는 상대에게 공개되지 않습니다.''')
    
    
    print()
    nextTo=input('다음으로 넘어가려면 엔터키를 누르세요.')
    gu.stopTime(3)
    
    #게임 시작
    while True:
        acMoney,betMoney=0,0
        #현재 게임머니,몇 번째 게임인지 확인
        print(f'{gameCount}번째 게임이 시작됩니다.')
        print(f'현재 {player}의 게임머니: {pMoney}원')
        print(f'현재 {dealer}의 게임머니: {dMoney}원')
        
        print()
        
        #참가비 회수
        print('이제 참가비를 거두겠습니다.')
        print('양측에서 1000원씩 돈이 차감됩니다.')
        
        #게임머니 부족 여부 확인
        if pMoney<=0:
            print(f'{player} 님의 참가비가 부족해 게임에 참여할 수 없습니다.')
            return 'pstop'
        
        elif dMoney<=0:
            print(f'{dealer} 님의 참가비가 부족해 게임에 참여할 수 없습니다.')
            return 'dstop'

        pMoney-=1000
        dMoney-=1000

        acMoney+=2000
      
        #덱 생성
        print('덱을 만듭니다. 잠시만 기다려주세요.')
        gu.stopTime(3)
        deckList=cd.createDeck()
        print('덱이 완성되었습니다.')
        
        print()
        
        #덱 셔플
        print('이제 덱을 섞겠습니다.')
        gu.stopTime(3)
        cd.shuffleCards(deckList)
        print('덱을 섞었습니다.')
        
        print()
        
        #서로에게 카드 지급
        print('이제 상대와 사용자에게 두 장의 카드를 지급하겠습니다.')
        print(f'{player}에게 카드를 지급중 입니다.')
        gu.stopTime(3)
        playerCard=cd.getCard(deckList,2)
        playerCard=cd.sortCards(playerCard)
        print('사용자가 카드를 받았습니다.')
        
        print()
        
        #사용자 카드 공개
        print('곧 내 카드가 공개됩니다. 잘 봐두세요!')
        gu.stopTime(3)
        cd.viewCardList(playerCard)
        
        print(f'{dealer}에게 카드를 지급중 입니다.')
        gu.stopTime(3)
        dealerCard=cd.getCard(deckList,2)
        dealerCard=cd.sortCards(dealerCard)
        print('딜러가 카드를 받았습니다.')
        
        print()
        
        #딜러 카드 공개
        print('곧 딜러의 카드가 공개됩니다. 잘 봐두세요!')
        gu.stopTime(3)
        cd.viewCardList(dealerCard)
        
        print()
        
        print(f'현재 누적된 금액 {acMoney}원 입니다.')
        
        #선공유무 공란    
        
        #사용자의 첫 번째 drop or go
        ch=gu.dorg()
        gu.stopTime(3)
        if ch=='drop':
            print('당신이 패배했습니다.')
            gameCount+=1
            dMoney+=acMoney
            next1=input('다음 게임을 시작하시려면 엔터를 누르세요.')
            gu.stopTime(3)
            continue
            
        # 첫 번째 베팅
        print('첫 번째 베팅이 시작됩니다.')
        
        betMoney=gu.betting(pMoney,dMoney)
        
        
        pMoney-=betMoney[1]
        
        dMoney-=betMoney[2]
        
        acMoney+=betMoney[0]
        
        print('첫 번째 베팅이 완료되었습니다.')
        print(f'현재 누적 베팅 금액은 {acMoney}원 입니다.')
        gu.stopTime(3)
        
        # 첫번째 드로우
        print('이제 3번째 카드를 지급하겠습니다.')
        
        
        print('사용자에게 카드를 지급중입니다.')
        gu.stopTime(3)
        playerCard=cd.handCards(deckList,playerCard)
        print('사용자의 카드는 다음과 같습니다.')
        cd.viewCardList(playerCard)
        
        print('딜러에게 카드를 지급중입니다.')
        gu.stopTime(3)
        dealerCard=cd.handCards(deckList,dealerCard)
        print('딜러의 카드 지급이 완료 되었습니다.')#딜러 카드 공개 x
        
        gu.stopTime(3)
        #사용자의 두 번째 drop or go
        
        ch=gu.dorg()
        gu.stopTime(3)
        if ch=='drop':
            print('당신이 패배했습니다.')
            gameCount+=1
            dMoney+=acMoney
            next1=input('다음 게임을 시작하시려면 엔터를 누르세요.')
            gu.stopTime(3)
            continue
        
        #사용자의 두 번째 베팅
        print('두 번째 베팅이 시작됩니다.')
        if pMoney >0 and dMoney>0:
            betMoney=gu.betting(pMoney,dMoney,betMoney[2])

            pMoney-=betMoney[1]
            dMoney-=betMoney[2]

            acMoney+=betMoney[0]

        print('두 번째 베팅이 완료되었습니다.')
        print(f'현재 누적 베팅 금액은 {acMoney}원 입니다.')
        
        gu.stopTime(3)
        
        #두 번째 드로우
        print('이제 4번째 카드를 지급하겠습니다.')
        
        print('사용자에게 카드를 지급중입니다.')
        gu.stopTime(3)
        playerCard=cd.handCards(deckList,playerCard)
        print('사용자의 카드는 다음과 같습니다.')
        cd.viewCardList(playerCard)
        
        print('딜러에게 카드를 지급중입니다.')
        gu.stopTime(3)
        dealerCard=cd.handCards(deckList,dealerCard)
        print('딜러의 카드 지급이 완료 되었습니다.')#딜러 카드 공개 x
        
        gu.stopTime(3)
        
        #사용자의 세 번째 drop or go
        
        ch=gu.dorg()
        gu.stopTime(3)
        if ch=='drop':
            print('당신이 패배했습니다.')
            gameCount+=1
            dMoney+=acMoney
            next1=input('다음 게임을 시작하시려면 엔터를 누르세요.')
            gu.stopTime(3)
            continue
        
        #사용자의 세 번째 베팅
        print('세 번째 베팅이 시작됩니다.')
        if pMoney >0 and dMoney>0:
            dealerBet=betMoney[2]
            betMoney=gu.betting(pMoney,dMoney,betMoney[2])


            pMoney-=betMoney[1]
            dMoney-=betMoney[2]

            acMoney+=betMoney[0]
        
        print('세 번째 베팅이 완료되었습니다.')
        print(f'현재 누적 베팅 금액은 {acMoney}원 입니다.')
        
        gu.stopTime(3)
        
        #마지막 드로우
        print('이제 마지막 카드를 지급하겠습니다.')
        
        print('사용자에게 마지막카드를 지급중입니다.')
        gu.stopTime(3)
        playerCard=cd.handCards(deckList,playerCard)
        print('사용자의 카드는 다음과 같습니다.')
        cd.viewCardList(playerCard)
        
        print('딜러에게 마지막 카드를 지급중입니다.')
        gu.stopTime(3)
        dealerCard=cd.handCards(deckList,dealerCard)
        print('딜러의 마지막 카드 지급이 완료 되었습니다.')#딜러 카드 공개 x
        
        gu.stopTime(3)
        
        print('카드를 모두 받으셨습니다.')
        print('당신의 패는 다음과 같습니다.')
        cd.viewCardList(playerCard)
        print('곧 마지막 Drop or Go가 시작됩니다, 신중을 기하세요! ')
        gu.stopTime(3)
        ch=gu.dorg()
        gu.stopTime(3)
        if ch=='drop':
            print('당신이 패배했습니다.')
            gameCount+=1
            dMoney+=acMoney
            next1=input('다음 게임을 시작하시려면 엔터를 누르세요.')
            gu.stopTime(3)
            
            continue
            
        print('go 를 선택하셨습니다....')
        gu.stopTime(3)
        #사용자의 마지막 베팅
        
        if pMoney >0 and dMoney>0:
            betMoney=gu.betting(pMoney,dMoney,betMoney[2])

            pMoney-=betMoney[1]
            dMoney-=betMoney[2]

            acMoney+=betMoney[0]

        print('마지막 베팅이 완료되었습니다.')
        print(f'현재 누적 베팅 금액은 {acMoney}원 입니다.')
        
        gu.stopTime(3)
        print('이제 서로의 패를 공개하겠습니다.')
        nextTo=input('준비가 되시면 엔터키를 눌러주세요.')
        
        #서로의 패 확인
        print('현재 당신의 패 입니다.')
        gu.stopTime(3)
        cd.viewCardList(playerCard)
        gu.stopTime(5)
        print('딜러의 패 입니다.')
        cd.viewCardList(dealerCard)
        gu.stopTime(3)
        #랭크 확인
        playerRank=rk.rank(playerCard)
        dealerRank=rk.rank(dealerCard)
        
        comp=rk.compare(playerRank,dealerRank,playerCard,dealerCard)
        
        if comp == 'Player win':
            pMoney+=acMoney
            gameCount+=1
            
        elif comp == 'Dealer win':
            dMoney+=acMoney
            gameCount+=1
        elif comp == 'Draw':
            print('다음게임으로 넘어갑니다. 베팅 금액은 누적됩니다.')
            gameCount+=1
            continue
            
        next1=input('다음 게임을 시작하시려면 엔터를 누르세요.')
        gu.stopTime(3)
        

