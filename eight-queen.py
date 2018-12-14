
n = 8    # n*n size
cb = n*n*[0] #checkboard
sum = 0
succ = [cb]


def negline(row,col,num):
    if(col>=row):
        for i in range(0,num-col+row):
            colc = i + col-row
            rowc = i  
            yield rowc,colc
    else:
        for i in range(0,num+col-row):
            colc = i
            rowc = i + row - col  
            yield rowc,colc

def posline(col,row,num):
    if(num-col-1>=row):
        for i in range(0,col-row+1):
            colc = col+row-i
            rowc = i  
            yield rowc,colc
    else:
        for i in range(0,2*num-row-1-col):
            colc = num-1-i
            rowc = i + row - (num-col-1) 
            yield rowc,colc

def check(num):
    for val in range(0,num*num):
        if(cb[val] == 1):
            row_c = int(val/num)
            col_c = int(val-row_c*num)
            for row in range(0,num): # check row 
                ind = row*num+col_c
                if(ind != val and cb[ind]==1):
                    return 0
            for col in range(0,num): # check col
                ind = row_c*num+col
                if(ind != val and cb[ind]==1):
                    return 0
            for x,y in negline(row_c,col_c,num): # check diagonal
                if(x*num+y != val and cb[x*num+y] == 1):
                    return 0
            for x,y in posline(row_c,col_c,num):
                if(x*num+y != val and cb[x*num+y] == 1):
                    return 0
    return 1

def backtrace(row,col,num):
    if(check(num)==0):
        return 0
    if(row == num):
        return 1
    for i in range(0,num-col):
        cb[row*num+col+i] = 1
        if(backtrace(row+1,0,num)==0):
            cb[row*num+col+i] = 0
        else:
            return 1
    return 0

backtrace(0,0,n)

for i in range(0,n): #print
    print(cb[i*n:(i+1)*n])

