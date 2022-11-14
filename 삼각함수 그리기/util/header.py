
def header_print(title,date,name):
    len_line=max(len(title),len(date),len(name))
    star_line(len_line+4)
    header_txt(len_line+2,title)
    header_txt(len_line+2,date)
    header_txt(len_line+2,name)
    star_line(len_line+4)
    
def star_line(count):
    for i in range(count):
        print('*',end='')
    print()
    
def print_space(count):
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
