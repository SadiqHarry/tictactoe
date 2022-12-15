board =  ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

currentplayer = "X"
winner = None 
gamerunning = True
has_lost = True


#print game board

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


#input move
def playerinput(board):
    inp = int(input("Enter a number 1-9: "))
    #If there is a number from 1-9 check to see if there is a blank spot("-") by -1 because input is indexed at 1
    if 1 <= inp <= 9 and board[inp-1] == "-":
                #If there is a blank spot("-") insert current_player("X")
        board[inp-1] = currentplayer
    else:
        print("Sorry, spot is taken")

#check for win or tie

def checkrow(board):
    #global editing of winner
    global winner
    #If all values in row are equal and not "-" print winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        #Using boolean so that we can efficently break out of loops
        return True
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



def checkwin():
    if checkcolumn(board) or checkdiagonal(board) or checkrow(board):
        print(f"The winner is {winner}")
        has_lost = False
        



def checktie(board):
    
    global gamerunning
    #If no winner(has_lost) + no blank spaces = tie
    if "-" not in board and has_lost == False:
        printboard(board)
        print("It is a tie!")
        gamerunning = False



#switch player

def switchplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"

#check for win or tie again


while gamerunning:
    printboard(board)
    playerinput(board)
    checkwin()
    checktie(board)
    switchplayer()
 