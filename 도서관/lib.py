#도서관리 프로그램
import webbrowser
class Book():#책 클래스
    #책 상태 데이터
    def __init__(self,title,writer,trans,publisher,publishDay,price,ISBN):
        self.title=title#제목
        self.writer=writer#작가
        self.trans=trans#옮긴이
        self.publisher=publisher#출판사
        self.publishDay=publishDay#출판일
        self.price=price#가격
        self.ISBN=ISBN#국제표준도서번호
        
    #책 객체 동작
    
    def bookinfo(self):
        print(f'책 제목: {self.title}')
        print(f'지은이: {self.writer}')
        print(f'옮긴이: {self.trans}')
        print(f'출판사: {self.publisher}')
        print(f'출판일: {self.publishDay}')
        print(f'가격: {self.price}')
        print(f'ISBN: {self.ISBN}')
        
class Member():
    def __init__(self,name,stuNum,loc,univ):
        self.name=name#이름
        self.stuNum=stuNum#학번
        self.loc=loc
        self.univ=univ
        
    def peopleinfo(self):
        print(f'이름: {self.name}')
        print(f'학번: {self.stuNum}')
        print(f'지역: {self.loc}')
        print(f'학교: {self.univ}')
        
class Library():
    
    def __init__(self,peopleList=dict(),bookList=dict(),url='https://gdllc.sen.go.kr/gdllc/index.do?getContextPath='):
        self.peopleList=peopleList#회원목록
        self.bookList=bookList#도서 목록
        self.url=url#도서관 웹 링크
        self.loanList=dict()
        self.reserve=dict()
        self.titleList=dict()
        self.nameList=dict()
        
    def showpeople(self):#회원목록 보여주기
        
        if len(self.nameList)==0: print('등록된 회원이 없습니다.')
            
        elif len(self.nameList)>0: 
            print("현재 등록된 회원 목록입니다.")
            count=1
            for name in self.nameList: 
                
                print(f'{count}: {name}')
                count+=1
                
    def addpeople(self):#멤버 객체 생성 후 적용
        name=input('이름을 입력해 주세요.: ')
        stuNum=input('학번을 입력해 주세요.: ')
        loc=input('지역을 입력해 주세요.: ')
        univ=input('학교를 입력해 주세요.: ')
        
        member=Member(name,stuNum,loc,univ)#사람객체 생성
        
        self.peopleList.setdefault(name,member)# true false는 회원의 대출여부 확인
        self.nameList.setdefault(name,True)
        print(f"{name}님이 회원으로 등록되었습니다. 학번: {member.stuNum}")
    
    def showBookList(self):
        if len(self.titleList)==0: print('등록된 책이 없습니다.')
            
        elif len(self.titleList)>0: 
            print("현재 등록된 책 목록입니다.")
            count=1
            for name in self.titleList: 
                
                print(f'{count}: {name}')
                count+=1
        
    def addBook(self):#책 객체 적용
        print('책 정보를 입력하겠습니다.')
        
        title=input('책 제목을 입력해 주세요.: ')
        writer=input('지은이을 입력해 주세요.: ')
        trans=input('옮긴이를 입력해 주세요.: ')
        publisher=input('출판사를 입력해 주세요.: ')
        publishDay=input('출판일을 입력해 주세요.: ')
        price=input('가격을 입력해 주세요.: ')
        ISBN=input('국제 표준 도서 번호를 입력해주세요: ')
        
        book=Book(title,writer,trans,publisher,publishDay,price,ISBN)
        
        self.titleList.setdefault(book.title,True)# true false는 책의 대출여부 확인
        self.bookList.setdefault(book.title,book)
        print(f"{book.title} 이/가 등록되었습니다.")
        
        book.bookinfo()
        
    def loanbook(self):
        nameFind=input('책을 대출 하시려면 회원님의 이름을 입력하세요.')
        
        if nameFind not in self.nameList: print('회원 등록이 되지 않은 이름입니다.')
        
        elif self.nameList[nameFind]==False:#현 회원이 대출한 책이 있는상태
            print(f"{nameFind}님은 현재 대출중인 책이 있습니다.")
            
        else:
            bookFind =input('대출하실 책 이름을 입력하세요.')
            
            if bookFind not in self.titleList: print('등록되지 않은 책입니다.')
            
            elif self.titleList[bookFind]==False:#책이 없어 대출불가상태일때
                print(f"{bookFind} 은/는 현재 대출중입니다.")
            
            else:
                print(f"'{bookFind}' 이/가 대출 되었습니다.")
                self.titleList.update({bookFind:False})#책이 없는상태
                self.nameList.update({nameFind:False})#현 회원은 대출 불가 상태
                self.loanList.setdefault(bookFind,nameFind)#대출리스트에 추가
                
    def rebook(self):
        nameFind=input('책을 반납 하시려면 회원님의 이름을 입력하세요.')
        
        if nameFind not in self.nameList: print('회원 등록이 되지 않은 이름입니다.')
        
        elif self.nameList[nameFind]==True:
            print(f"{nameFind}님은 현재 반납할 책이 없습니다.")
            
        else:
            bookFind =input('반납하실 책 이름을 입력하세요.')
            
            if bookFind not in self.titleList: print('등록되지 않은 책입니다.')
            
            elif self.titleList[bookFind]==True:
                print(f"{bookFind} 은/는 현재 대출중이 아닙니다.")
            
            else:
                print(f"'{bookFind}' 이/가 반납 되었습니다.")
                self.titleList.update({bookFind:True})#책이 돌아온상태
                self.nameList.update({nameFind:True})#대출 제한이 해제된 상태
                self.loanList.pop(bookFind,'')#대출리스트에 삭제
                
                if bookFind in self.reserve:
                    self.titleList.update({bookFind:False})#책이 없는상태
                    self.nameList.update({self.reserve[bookFind]:False})#현 회원은 대출 불가 상태
                    self.loanList.setdefault(bookFind,self.reserve[bookFind])#대출리스트에 추가
                    self.reserve.pop(bookFind,'')
                
                
    def showloan(self):
        if len(self.loanList) ==0:
            print('현재 대출자가 없습니다.')
        else:
            for book,name in self.loanList.items():
                print(f"회원 {name} 님이 대출중인 책은, '{book}' 입니다.")

    
    def showreserve(self):
        if len(self.reserve) ==0:
            print('현재 예약자가 없습니다.')
        else:
            for book,name in self.reserve.items():
                print(f"회원 {name} 님이 예약하신 책은, '{book}' 입니다.")
                
    def reservemessege(self):
        
        nameFind=input('책을 예약 하시려면 회원님의 이름을 입력하세요.')
        
        if nameFind not in self.nameList: print('회원 등록이 되지 않은 이름입니다.')
        
        else:
            
            bookFind =input('예약하실 책 이름을 입력하세요.')
            
            if bookFind not in self.titleList: print('등록되지 않은 책입니다.')
            elif self.titleList[bookFind]: print(f"'{bookFind}'은/는 현재 예약없이 대출이 가능합니다.")
                
            else:
                print(f"현재 '{bookFind}'은/는 {self.loanList[bookFind]}님이 대출중입니다.")
                print(f"'{bookFind}'이/가 대출 예약되었습니다.")
                
                self.reserve.setdefault(bookFind,nameFind)
                
    def searbook(self):
        nameFind=input('책을 검색 하시려면 회원님의 이름을 입력하세요.')
        
        if nameFind not in self.nameList: print('회원 등록이 되지 않은 이름입니다.')
        
        else:   
            bookFind=input('찾으시려는 책 이름을 입력해주세요.')
            if bookFind not in self.titleList: print('등록되지 않은 책입니다.')
            else:
                print(f"'{bookFind}'의 세부정보 입니다.")
                self.bookList[bookFind].bookinfo()
                
    def searmember(self):
        nameFind=input('검색하시려는 회원의 이름을 입력하세요.')
        if nameFind not in self.nameList: print('회원 등록이 되지 않은 이름입니다.')
            
        else:
            print(f"'{nameFind}'님의 세부정보 입니다.")
            self.peopleList[nameFind].peopleinfo()
                
    def openweb(self):
        webbrowser.open(self.url)
