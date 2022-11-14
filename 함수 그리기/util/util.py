
def header_print(title,date,name):
    len_line=max(len(title),len(date),len(name))
    star_line(len_line+4)
    header_txt(len_line+2,title)
    header_txt(len_line+2,date)
    header_txt(len_line+2,name)
    star_line(len_line+4)
    
def star_line(count):#별라인 출력 함수
    for i in range(count):
        print('*',end='')
    print()
    
def print_space(count):#공백 출력함수
    for i in range(count):
        print(' ',end='')
        
def header_txt(width,txt):#width= 전체 header길이
    print('*',end='')
    lspace=int((width-len(txt))/2)
    print_space(lspace)
    print(txt,end='')
    rspace=width-lspace-len(txt)
    print_space(rspace)
    print('*')


def print_bar(size):# -출력함수
    for i in range(size):
        print('-', end='')

def make_odd(num):#짝수 ->홀수 만드는 함수
    if num % 2 == 0:
        num+=1

    return num

def make_floor(width,height,str):#평면 생성 함수
    floor=[[str for i in range(width)] for j in range(height)]

    return floor            

def roofy(width):#y의 최상단 출력 함수
    roofy=[' ' for i in range(width)]

    start=int(width/2)-1
    for i in range(start):
        roofy[i] = ' '

    roofy[start]='y'
    roofy[start+1]='│'

    for i in range(start+2,width):
        roofy[i] = ' '
    
    print(*roofy)

def axis(width,height,floor):
    for i in range(width):
        floor[int(height/2)][i]='-'

    floor[int(height/2)+1][int(width/2)-1]=0

    floor[int(height/2)+1][width-1]='x'

    for i in floor:
        i[int(width/2)]='│'

def check_i(i,width,height,floor,y):
    if i < 0:
        star_row = int(height/2)-y
        star_col = int(width/2) - i
        floor[star_row][star_col]='*'
    
    elif i>0:
        star_row = int(height/2)-y
        star_col = int(width/2) + i
        floor[star_row][star_col]='*'

    else:
        star_row = int(height/2)-y
        star_col = int(width/2)
        floor[star_row][star_col]='*'