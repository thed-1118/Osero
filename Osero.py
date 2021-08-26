rows,cols= 8,8
boards= [[0]*rows for i in range(cols)]
boolBoards= [[True]* rows for i in range(cols)]
player=-1 #-1が〇プレイヤー,1が×プレイヤー

def debug():
    for row in range(rows):
        print()
        for col in range(cols):
            print(boolBoards[row][col],end='')

def initialize(): #初期化
    boards[3][3],boards[4][4]= 1,1
    boards[3][4],boards[4][3]= -1,-1
    
def checkLeft(row,col):
    tmpCol = col-1
    if(tmpCol<0 or boards[row][tmpCol]!= -1*player): return False

    while(tmpCol>0):
        tmpCol -= 1
        if(boards[row][tmpCol]==0): break
        if(boards[row][tmpCol]==player): return True
        
    return False

def checkUpper(row,col):
    tmpRow = row-1
    if(tmpRow<0 or boards[tmpRow][col]!= -1*player): return False

    while(tmpRow>0):
        tmpRow -= 1
        if(boards[tmpRow][col]==0): break
        if(boards[tmpRow][col]==player): return True

    return False

def checkRight(row,col):
    tmpCol = col+1
    if(tmpCol> cols-1 or boards[row][tmpCol]!= -1*player): return False

    while(tmpCol<cols-1):
        tmpCol += 1
        if(boards[row][tmpCol]==0): break
        if(boards[row][tmpCol]==player): return True
        
    return False

def checkLower(row,col):
    tmpRow = row+1
    if(tmpRow > rows-1 or boards[tmpRow][col]!= -1*player): return False

    while(tmpRow< rows-1):
        tmpRow += 1
        if(boards[tmpRow][col]==0): break
        if(boards[tmpRow][col]==player): return True
     
    return False

def checkUpperLeft(row,col):
    tmpRow= row-1
    tmpCol= col-1
    if(tmpRow< 0 or tmpCol< 0 or boards[tmpRow][tmpCol]!= -1*player): return False

    while(tmpRow>0 and tmpCol>0):
        tmpRow -= 1
        tmpCol -= 1
        if(boards[tmpRow][tmpCol]==0): break
        if(boards[tmpRow][tmpCol]==player): return True
      
    return False

def checkUpperRight(row,col):
    tmpRow= row-1
    tmpCol= col+1
    if(tmpRow< 0 or tmpCol> cols-1 or boards[tmpRow][tmpCol]!= -1*player): return False

    while(tmpRow>0 and tmpCol<cols-1):
        tmpRow -= 1
        tmpCol += 1
        if(boards[tmpRow][tmpCol]==0): break
        if(boards[tmpRow][tmpCol]==player): return True
       
    return False

def checkLowerRight(row,col):
    tmpRow= row+1
    tmpCol= col+1
    if(tmpRow> rows-1 or tmpCol> cols-1 or boards[tmpRow][tmpCol]!= -1*player): return False

    while(tmpRow< rows-1 and tmpCol< cols-1):
        tmpRow += 1
        tmpCol += 1
        if(boards[tmpRow][tmpCol]==0): break
        if(boards[tmpRow][tmpCol]==player):return True
       
    return False

def checkLowerLeft(row,col):
    tmpRow= row+1
    tmpCol= col-1
    if(tmpRow> rows-1 or tmpCol< 0 or boards[tmpRow][tmpCol]!= -1*player): return False

    while(tmpRow<rows-1 and tmpCol>0):
        tmpRow += 1
        tmpCol -= 1
        if(boards[tmpRow][tmpCol]==0): break
        if(boards[tmpRow][tmpCol]==player): return True
        
    return False

def isPlacable():   #置ける判定
    global player
    for row in range(rows):
        for col in range(cols):
            if(boards[row][col]==0):
                if(checkLeft(row,col) or checkUpper(row,col) or checkRight(row,col) or 
                   checkLower(row,col) or checkUpperLeft(row,col) or checkUpperRight(row,col) 
                   or checkLowerRight(row,col) or checkLowerLeft(row,col)): return True
     
    print("\n置ける場所がないのでパスします")
    player = player* -1

    for row in range(rows):
        for col in range(cols):
            if(boards[row][col]==0):
                if(checkLeft(row,col) or checkUpper(row,col) or checkRight(row,col) or 
                   checkLower(row,col) or checkUpperLeft(row,col) or checkUpperRight(row,col) 
                   or checkLowerRight(row,col) or checkLowerLeft(row,col)): return True
        
def updateLeft(row,col):
    col-= 1
    if(boards[row][col]==player): return
    while(col>0 and boards[row][col]==-1*player):col -= 1
    if(boards[row][col]==player):
        print("Left")
        col+=1
        while(boards[row][col]==-1*player): 
            boards[row][col]= player
            col+= 1
        boards[row][col]= player
    return

def updateUpper(row,col):
    row-= 1
    if(boards[row][col]==player): return
    while(row>0 and boards[row][col]==-1*player): row-= 1
    if(boards[row][col]==player):
        print("upper")
        row+=1
        while(boards[row][col]==-1*player):
            boards[row][col]= player
            row+= 1
        boards[row][col]= player
    return

def updateRight(row,col):
    col+= 1
    if(boards[row][col]==player): return
    while(col< cols and boards[row][col]==-1*player): col += 1
    if(boards[row][col]==player):
        print("Right")
        col-= 1
        while(boards[row][col]==-1*player):
            boards[row][col]= player
            col-= 1
        boards[row][col]= player
    return

def updateLower(row,col):
    row+= 1
    if(boards[row][col]==player): return
    while(row< rows and boards[row][col]==-1*player): row += 1
    if(boards[row][col]==player):
        print("Lower")
        row-= 1
        while(boards[row][col]==-1*player):
            boards[row][col]= player
            row-= 1
        boards[row][col]= player
    return

def updateUpperLeft(row,col):
    row-= 1 
    col-= 1
    if(boards[row][col]==player): return
    while(row> 0 and col> 0  and boards[row][col]==-1*player):
        row -= 1
        col -= 1
    if(boards[row][col]==player):
        print("upperLeft")
        row+= 1
        col+= 1
        while(boards[row][col]==-1*player):
            boards[row][col]= player
            row+= 1
            col+= 1
        boards[row][col]= player
    return

def updateUpperRight(row,col):
    row-= 1 
    col+= 1
    if(boards[row][col]==player): return
    while(row> 0 and col< cols  and boards[row][col]==-1*player):
        row -= 1
        col += 1
    if(boards[row][col]==player):
        print("upperRight")
        row+= 1
        col-= 1
        while(boards[row][col]==-1*player):
            boards[row][col]= player
            row+= 1
            col-= 1
        boards[row][col]= player
    return

def updateLowerRight(row,col):
    row+= 1 
    col+= 1
    if(boards[row][col]==player): return
    while(row< rows and col< cols  and boards[row][col]==-1*player):
        row += 1
        col += 1
    if(boards[row][col]==player):
        print("LowerRight")
        row-= 1
        col-= 1
        while(boards[row][col]==-1*player):
            boards[row][col]= player
            row-= 1
            col-= 1
        boards[row][col]= player
    return

def updateLowerLeft(row,col):
    row+= 1 
    col-= 1
    if(boards[row][col]==player): return
    while(row< rows and col> 0  and boards[row][col]==-1*player):
        row += 1
        col -= 1
    if(boards[row][col]==player):
        print("LowerLeft")
        row-= 1
        col+= 1
        while(boards[row][col]==-1*player):
            boards[row][col]= player
            row-= 1
            col+= 1
        boards[row][col]= player
    return

def updateBoards(row,col):
    #print(boolBoards[row][col])
    if(boards[row][col]!=0 or boolBoards[row][col]==False): return False
    updateLeft(row,col)
    updateUpper(row,col)
    updateRight(row,col)
    updateLower(row,col)
    updateUpperLeft(row,col)
    updateUpperRight(row,col)
    updateLowerRight(row,col)
    updateLowerLeft(row,col)
    if(boards[row][col]==0): 
        boolBoards[row][col]= False
        return False
    else: return True

def placeStone():
    while(True):
        col= input("\nx座標を入力してください\n")
        row= input("\ny座標を入力してください\n")
        row= int(row)
        col= int(col)
        if(boolBoards[row][col]==True):
            if(updateBoards(row,col)): return
            else: print("そこには置けません")
        else:print("そこには置けません")
        
def printBoards():
    print("  0 1 2 3 4 5 6 7")
    for row in range(rows):
        print('{}'.format(row),end='')
        for col in range(cols):
            if(boards[row][col]==-1): print(" o",end="")
            elif(boards[row][col]==1): print(" x",end="")
            else: print(" *",end="")
        print()

    if(player==-1): print("oの番です")
    else: print("xの番です")

def judge():
    player1=0
    player2=0

    for row in range(rows):
        for col in range(cols):
            if(boards[row][col]==1): player1 +=1
            else: player2 += 1

    if(player1>player2): print("〇の勝ち")
    elif(player1==player2): print("引き分け")
    else: print("×の勝ち")
    return

def initializeBoolBoards():
    global boolBoards
    boolBoards= [[True]* rows for i in range(cols)]

def main():
    global player
    initialize()
    printBoards()
    
    while(isPlacable()):
        initializeBoolBoards()
        placeStone(); #石を置く
        player *= -1
        printBoards()

    judge() #勝敗判定

if (__name__== '__main__'):
    main()