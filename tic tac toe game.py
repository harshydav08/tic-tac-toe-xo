
a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
gameOver = False
turn = "X"

def gameBoard():
    print(a[0], "|", a[1], "|", a[2])
    print(a[3], "|", a[4], "|", a[5])
    print(a[6], "|", a[7], "|", a[8])

def changeTurn():
    global turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"

def XTurn():
    xInp = int(input("Enter value where X should be placed: "))
    a[xInp] = "X"
    gameBoard()

def OTurn():
    oInp = int(input("Enter value where O should be placed: "))
    a[oInp] = "O"
    gameBoard()

def checkWin():
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for j in wins:
        if a[j[0]] == a[j[1]] == a[j[2]] and a[j[0]] != "":
            return True
    return False

gameBoard()

while not gameOver:
    if turn == "X":
        XTurn()
        gameOver = checkWin()
        if gameOver:
            print("X wins!")
        else:
            changeTurn()
    else:
        OTurn()
        gameOver = checkWin()
        if gameOver:
            print("O wins!")

        
        else:
            changeTurn()



















