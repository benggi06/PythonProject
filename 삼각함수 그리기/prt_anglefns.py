import math
def  print_anglefns(fn,start_deg, end_deg, width,length):#사인함수 그리기
    start_deg = int(start_deg/10)
    end_deg = int(end_deg/10)
    length = int(length/10)
        
    if width % 2 == 0:#폭이 짝수일때 1더해서 홀수 만들기
            width+=1

    half=int((width-1)/2)
    
    if fn == 'math.sin':
        
        print(' x ','-'*width,'sin(x)')

        for i in range(start_deg,end_deg+1):#시작 각도 ~ 마지막 각도
            i*=10
            new_i=str(i).zfill(3) #입력되는 각도가 100이하일때 0채우기

            sin_value=round(math.sin(math.radians(i)),3)#사인값 소수점 4번째에서 반올림
            loc1=int(round(sin_value*half,1))#절반 이후 첫번째 공백

            if sin_value == 0:#사인값이 0일때

                sin_value='{:.3f}'.format(sin_value)#사인값 소수점 3번째 자리까지 출력
                print('{0}{1}*{2} {3}'.format(new_i,' '*(half+1),' '*(half+1),sin_value))
                
            elif sin_value>0:#사인값이 0 이상일때

                loc2=half-loc1
                sin_value='{:.3f}'.format(sin_value)
                print('{0}{1}│{2}*{3}{4}'.format(new_i,' '*(half+1),' '*loc1,' '*loc2,sin_value))
            
            elif sin_value<0:#사인값이 0 이하일때
                loc2=half+loc1
                sin_value='{:.3f}'.format(sin_value)
                print('{0}{1}*{2}│{3}{4}'.format(new_i,' '*loc2,' '*(half-loc2),' '*(half-1),sin_value))
            
        for i in range(end_deg+1,length+1):#마지막 각도 ~  길이
            i*=10
            new_i=str(i).zfill(3)
            sin_value=round(math.sin(math.radians(i)),3)
            sin_value='{:.3f}'.format(sin_value)

            print('{0}{1}│{2}{3}'.format(new_i,' '*(half+1),' '*(half+1),sin_value))
    
    elif fn == 'math.cos':

        print(' x ','-'*width,'cos(x)')

        for i in range(start_deg,end_deg+1):#시작 각도 ~ 마지막 각도
            i*=10
            new_i=str(i).zfill(3) #입력되는 각도가 100이하일때 0채우기

            cos_value=round(math.cos(math.radians(i)),3)#코사인값 소수점 4번째에서 반올림
            loc1=int(round(cos_value*half,1))#절반 이후 첫번째 공백

            if cos_value == 0:#코사인값이 0일때

                cos_value='{:.3f}'.format(cos_value)#코사인값 소수점 3번째 자리까지 출력
                print('{0}{1}*{2} {3}'.format(new_i,' '*(half+1),' '*(half+1),cos_value))#
                
            elif cos_value>0:#코사인값이 0 이상일때

                loc2=half-loc1
                cos_value='{:.3f}'.format(cos_value)
                print('{0}{1}│{2}*{3}{4}'.format(new_i,' '*(half+1),' '*loc1,' '*loc2,cos_value))
            
            elif cos_value<0:#코사인값이 0 이하일때
                loc2=half+loc1
                cos_value='{:.3f}'.format(cos_value)
                print('{0}{1}*{2}│{3}{4}'.format(new_i,' '*loc2,' '*(half-loc2),' '*(half),cos_value))
            
        for i in range(end_deg+1,length+1):#마지막 각도 ~  길이
            i*=10
            new_i=str(i).zfill(3)
            cos_value=round(math.cos(math.radians(i)),3)
            cos_value='{:.3f}'.format(cos_value)

            print('{0}{1}│{2}{3}'.format(new_i,' '*(half+1),' '*(half+1),cos_value))
