
import time
import random
def stopTime(count):
    for i in range(count):
        if i != count-1:
            time.sleep(0.5)
            print('•',end='')
        else:
            time.sleep(0.5)
            print('•',end='')
    time.sleep(0)
    print()

    

def betting(pMoney,dMoney,acMoney='first'):#베팅
    
    if dMoney==0:
        return
    
    if acMoney=='first':#첫번째 베팅
        playerbet=int(input(f'0원부터 {pMoney}원 중 금액을 골라 입력하세요.: '))
        
        if playerbet==pMoney:
            print('사용자가 올인합니다.')
            
        else:
            print(f'사용자의 {pMoney}원 중 {playerbet}원이 베팅되었습니다.')
                
        print('딜러가 배팅중입니다.')
        stopTime(3)
        dealerbet=random.randrange(playerbet,playerbet+int(playerbet/10))
        print(f'딜러의 {dMoney}원 중 {dealerbet}원이 베팅되었습니다.')
        
        return [dealerbet+playerbet,playerbet,dealerbet]
        
    else:#첫번째 이후 베팅
        
        print(f' 현재 상대가 베팅한 금액은 {acMoney}원 입니다. 그 이상의 금액을 베팅해주세요.')
        
        playerbet=int(input(f'0원부터 {pMoney}원 중 금액을 골라 입력하세요.: '))
        if playerbet>pMoney or playerbet<0:
            print('금액을 정확히 입력하세요.')
            return betting(pMoney,dMoney,acMoney)
        
        if playerbet==pMoney:
            print('사용자가 올인합니다.')
            
            
        else:
            print(f'사용자의 {pMoney}원 중 {playerbet}원이 베팅되었습니다.')
            
        print('딜러가 배팅중입니다.')
        
        stopTime(3)
        
        dealerbet=random.randrange(playerbet,playerbet+int(playerbet/10))
        
        if dealerbet>=dMoney:
            dealerbet=dMoney
            print('딜러가 올인 했습니다. 지금부터는 베팅란에 0만 입력 해주세요.')
            
        print(f'딜러의 {dMoney}원 중 {dealerbet}원이 베팅되었습니다.')
        
        return [dealerbet+playerbet,playerbet,dealerbet]
        
def dorg():#drop or go
    while True:
        dorgo=int(input('1: drop, 2: go '))
        
        if dorgo == 1:
            
            print('게임을 포기합니다.')
            
            return 'drop'
        
        elif dorgo == 2:
            print('게임을 진행합니다.')
            return
        
        else:
            print('1과 2중 하나만을 선택하세요. ')
            continue
