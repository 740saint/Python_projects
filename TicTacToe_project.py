import turtle
import random

pen = turtle.Turtle()
screen = turtle.Screen()

pen.speed(0)
pen.pensize(20)

EMPTY_SPACE = ''

board = [
            [EMPTY_SPACE,EMPTY_SPACE,EMPTY_SPACE],
            [EMPTY_SPACE,EMPTY_SPACE,EMPTY_SPACE],
            [EMPTY_SPACE,EMPTY_SPACE,EMPTY_SPACE]
        ]
playerList = ["Player1", "Player2"]
playerTokens = ["X", "O"]

oCords = {
            1: (-200, 100), 2: (0, 100), 3: (200, 100),
            4: (-200, -100),5: (0, -100),6: (200, -100),
            7: (-200, -300),8: (0, -300),9: (200, -300)
         } 

xCords = {
            1 : (-300, 300), 2 : (-100, 300), 3 : (100, 300),
            4 : (-300, 100), 5 : (-100, 100), 6 : (100, 100),
            7 : (-300, -100),8 : (-100, -100),9 : (100, -100)
         }
def drawO(location):
    pen.color("blue")

    pen.up()
    pen.setpos(oCords[location])
    pen.down()
    pen.circle(100)

def drawX(location):
    pen.color("red")

    pen.up()
    pen.setpos(xCords[location])
    pen.down()
    pen.setpos(pen.xcor() + 200, pen.ycor() -200)

    pen.up()
    pen.setpos(pen.xcor() -200, pen.ycor())
    pen.down()
    pen.setpos(pen.xcor()+200, pen.ycor()+200)

def placeToken(player, row, col):
    location = (3 * row) + col + 1
    token = EMPTY_SPACE
    if player == playerList[0]:
        drawX(location)
        token = playerTokens[0]
    else:
        drawO(location)
        token = playerTokens[1]
    board[row][col] = token

def checkifValidMove(row, col):
    if row > 2 or row < 0:
        return False
    if col > 2 or col < 0:
        return False
    if board[row][col] != EMPTY_SPACE:
        return False

    return True

def checkForHorizontalWin(token):
    for row in board:
        counter = 0
        for col in row:
            if col == token:
                counter += 1
            else:
                break
        if counter == 3:
            return True
    return False

def checkForVerticalWin(token):
    for col in range(3):
        counter = 0
        for row in board:
            if row[col] == token:
                counter += 1
            else:
                break
        if counter == 3:
            return True
    return False

def checkForDiagonalWin(token):
    counter = 0
    for i in range(3):
        if board[i][i] == token:
            counter += 1
        else:
            break
    if counter == 3:
        return True
    counter = 0
    row = 0
    col = 2
    for i in range(3):
        if board[row][col] == token:
            counter += 1
        else:
            break
        row += 1
        col -= 1
    if counter == 3:
        return True
    return False

def checkForWin(player):
    token = EMPTY_SPACE
    if player == playerList[0]:
        token = playerTokens[0]
    else:
        token = playerTokens[1]

    if checkForHorizontalWin(token):
        return True
    if checkForVerticalWin(token):
        return True
    if checkForDiagonalWin(token):
        return True

    return False

def checkForDraw():
    for row in board:
        for col in row:
            if col == EMPTY_SPACE:
                return False
    return True

def checkForGameOver():
    if checkForWin(playerList[0]) or checkForWin(playerList[1]):
        return True

    if checkForDraw():
        return True

    return False


def PlayGame():
    #currentPlayer = playerList[0]
    currentPlayer = random.choice(playerList)
    gameOver = False

    while not gameOver:
        print(currentPlayer + "'s turn!")
        isValid = False
        row = -1
        col = -1

        while not isValid:
            row = int(input("Enter a row 0-2:"))
            col = int(input("Enter a column 0-2:"))

            isValid = checkifValidMove(row, col)

            if not isValid:
                print("That move is invalid. Please try again")
        placeToken(currentPlayer, row, col)

        gameOver = checkForGameOver()

        if not gameOver:
            if currentPlayer == playerList[0]:
                currentPlayer = playerList[1]
            else:
                currentPlayer = playerList[0]

def declareWinner():
    if checkForWin(playerList[0]):
        print(playerList[0], "has won!")
    elif checkForWin(playerList[1]):
        print(playerList[1], "has won!")
    elif checkForDraw():
        print("It's a draw!")
    
def drawBoard():
    pen.color("Black")

    pen.up()
    pen.setpos(-100, 300)
    pen.down()
    pen.setpos(-100, -300)

    pen.up()
    pen.setpos(100, 300)
    pen.down()
    pen.setpos(100, -300)

    pen.up()
    pen.setpos(-300, 100)
    pen.down()
    pen.setpos(300, 100)

    pen.up()
    pen.setpos(-300, -100)
    pen.down()
    pen.setpos(300, -100)


def ResetGame():
    screen.clear()
    for row in range(3):
        for col in range(3):
            board[row][col] = EMPTY_SPACE
    drawBoard()

def SetUpGame():
    print("Welcome to TickTacToe!")

    playerList[0] = input("What is the first player's name?")
    playerList[0] = input("What is the second player's name?")
    drawBoard()


#Application Loop

exitGame = False
SetUpGame()
while not exitGame:
    PlayGame()
    declareWinner()


    userInput = input("Would you like to play again? y/n")
    userInput = userInput.lower()

    if userInput == "y":
        ResetGame()
    else:
        print("Thank you for playing!")
        exitGame = True





