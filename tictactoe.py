board =  ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

currentplayer = "X"
winner = None 
gamerunning = True

#print game board

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
printboard(board)


#input move
def playerinput(board):
    inp = int(input("Enter a number 1-9: "))
    if 1 <= inp <= 9 and board[inp-1] == "-":
        #If there is a number from 1-9 check to see if there is a blank spot("-") by -1 because the board is indexed 0 and input is indexed 1
        board[inp-1] = currentplayer
        #If there is a blank spot("-") incser current_player("X")
    else:
        print("Sorry, spot is taken")

#check for win or tie

def checkrow(board):
    global winner
    #global editing of winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        #If all values in row equals are equal and not "-" print winner
        winner = board[0]
        return True
        #Using boolean so that we can efficently break out of loops
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkcolumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkdiagonal(board):
    global winner
    if board[0] == board[4]== board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board [2] != "-":
        winner = board[2]
        return True



#switch player

#check for win or tie again

while gamerun:
    printboard(board)
    playerinput(board)



