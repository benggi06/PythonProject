from util import util
import prt_anglefns

def print_fn(fn,x_min,x_max,width,height):
    if fn == '1':
        a=int(input('2차항 계수를 입력하세요.: '))
        b=int(input('1차항 계수를 입력하세요.: '))
        c=int(input('상수항을 입력하세요.: '))
        
        def fx(x,a,b,c):
            return a*x**2+b*x+c
            
        width=util.make_odd(width)
        height=util.make_odd(height)

        floor = util.make_floor(width,height,' ')
        print('''입력한 이차함수는 다음과 같습니다.: f(x) = ({0})x^2+({1})x+({2})'''.format(a,b,c))
        util.roofy(width)

        util.axis(width,height,floor)
        
        #x가 아래로 볼록한 2차함수
        if a>0:
            for i in range(x_min,x_max+1):
                y = fx(i,a,b,c)
                if i < 0:
                    star_row = int(height/2)-y
                    star_col = int(width/2) + i
                    floor[star_row][star_col]='*'
                
                elif i>0:
                    star_row = int(height/2)-y
                    star_col = int(width/2) + i
                    floor[star_row][star_col]='*'

                else:
                    star_row = int(height/2)-y
                    star_col = int(width/2)
                    floor[star_row][star_col]='*'


        elif a<0:
            for i in range(x_min,x_max+1):

                y = fx(i,a,b,c)
                

                util.check_i(i,width,height,floor,y)
                # elif y >0:
                #     if i < 0:
                #         star_row = int(height/2)-y
                #         star_col = int(width/2) - i
                #         floor[star_row][star_col]='*'
                    
                #     elif i>0:
                #         star_row = int(height/2)-y
                #         star_col = int(width/2) + i
                #         floor[star_row][star_col]='*'

                #     else:
                #         star_row = int(height/2)-y
                #         star_col = int(width/2)
                #         floor[star_row][star_col]='*'

        
        for i in floor:
            print(*i)

    elif fn == '2':
        prt_anglefns.print_anglefns(fn,x_min,x_max,width,height)
    elif fn == '3':
        prt_anglefns.print_anglefns(fn,x_min,x_max,width,height)


