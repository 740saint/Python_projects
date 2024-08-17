import random

players = ["Player1", "Player2"]

player1ShipBoard = [
                [],[],[],[],[],
                [],[],[],[],[]
                ]
player2ShipBoard = [
                [],[],[],[],[],
                [],[],[],[],[]
                ]
player1HMBoard = [
                [],[],[],[],[],
                [],[],[],[],[]
                ]
player2HMBoard = [
                [],[],[],[],[],
                [],[],[],[],[]
                ]
ShipDictionary = {
    "Destroyer": 2,
    "Submarine": 3,
    "Cruiser": 3,
    "Battleship": 4,
    "Carrier": 5
    }
player1ShipStatus = {
    "Destroyer": 0,
    "Submarine": 0,
    "Cruiser": 0,
    "Battleship": 0,
    "Carrier": 0
    
    }
player2ShipStatus = {
    "Destroyer": 0,
    "Submarine": 0,
    "Cruiser": 0,
    "Battleship": 0,
    "Carrier": 0
    
    }
RowDictionary = {
    "A":0,
    "B":1,
    "C":2,
    "D":3,
    "E":4,
    "F":5,
    "G":6,
    "H":7,
    "I":8,
    "J":9
    }
TokenDictionary = {
    "Empty" : 0,
    "Destroyer" : 1,
    "Submarine":2,
    "Cruiser":3,
    "Battleship":4,
    "Carrier":5,
    "Hit":6,
    "Miss":7
    }

def initBoards():
    for row in range(10):
        for col in range(10):
            player1ShipBoard[row].append(0)
            player2ShipBoard[row].append(0)

            player1HMBoard[row].append(0)
            player1HMBoard[row].append(0)


def placeShips():
    for player in players:
        print(players, "is placing ships!")
        for shipKey in ShipDictionary:
            placeShip(player, shipKey)
            print(player, "has placed their", shipKey)
        print(player, "has finsihed placing their ships.")

def placeShip(player, shipKey):
    print("Placing", shipKey, "(", ShipDictionary[shipKey],"spaces long)")

    currentBoard = []
    if player == players[0]:
        currentBoard = player1ShipBoard
    else:
        currentBoard = player2ShipBoard

    valid = False
    while not valid:
        rawRowInput = input ("What Row? (A-J): ")
        rawColInput = input ("What Column? (1-10): ")
        try:
            rawRowInput = rawRowInput.upper()
            rowInput = RowDictionary[rawRowInput]

            colInput = int(rawColInput) - 1
            isRoom = False
            isRoom = isRoom or checkBoardPlacement(currentBoard, shipKey, rowInput, colInput, "N")
            isRoom = isRoom or checkBoardPlacement(currentBoard, shipKey, rowInput, colInput, "E")
            isRoom = isRoom or checkBoardPlacement(currentBoard, shipKey, rowInput, colInput, "S")
            isRoom = isRoom or checkBoardPlacement(currentBoard, shipKey, rowInput, colInput, "W")
            if rowInput > 9 or rowInput < 0:
                print("Invalid Coordinates! Try Again!")
                
            elif colInput > 9 or colInput < 0:
                print("Invalid Coordinates! Try Again!")
            elif not isRoom:
                print(shipKey, "won't fit in that location")
            else:
                valid = True
        except:
            print("I'm sorry, that input isn't valid. Please try again.")
    validRotation = False
    while not validRotation:
        rawRotInput = input("what direction should the ship face? (N, E, S, W): ")
        isValidPlacement = checkBoardPlacement(currentBoard, shipKey, rowInput, colInput, rawRotInput)

        if isValidPlacement:
            putShipOnBoard(player, shipKey, rowInput, colInput, rawRotInput)
            validRotation = True
        else:
            print(shipKey, "did not fit in that direction! Try again!")


def checkBoardPlacement(board, shipKey, row, col, rot):
    shipLength = ShipDictionary[shipKey]

    rot = rot.lower()
    currentRow = row
    currentCol = col

    for i in range(shipLength):
        if currentRow > 9 or currentRow < 0:
            return False
        if currentCol > 9 or currentCol < 0:
            return False
        space = board[currentRow][currentCol]
        if space != 0:
            return False
        if rot == "n":
            currentRow -= 1
        elif rot == "s":
            currentRow += 1
        elif rot == "e":
            currentRow += 1
        elif rot == "w":
            currentRow -= 1
        else:
            print("Invalid Orientation")
            return False
    return True

def putShipOnBoard(player, shipKey, row, col, rot):
    currentBoard = []
    if player == players[0]:
        currentBoard = player1ShipBoard
    else:
        currentBoard = player2ShipBoard

    shipLenght = ShipDictionary[shipKey]
    shipToken = TokenDictionary[shipKey]

    currentRow = row
    currentCol = col
    rot = rot.lower()

    for i in range(shipLenght):
        currentBoard[currentRow][currentCol] = shipToken

        if rot == "n":
            currentRow -= 1
        elif rot == "s":
            currentRow += 1
        elif rot == "e":
            currentRow += 1
        elif rot == "w":
            currentRow -= 1                   
    
def playGame():
    gameOver = False

    currentplayer = random.choice(players)
    while not gameOver:
        playerTurn(currentPlayer)
        gameOver = checkForGameOver(currentPlayer)

        if not gameOver:
            if currentPlayer == players[0]:
                currentPlayer = players[1]
            else:
                currentPlayer = player[0]
    print("Game Over!")
        
def printBoard(board):
    output = ""
    for row in board:
        for col in row:
            output += "["
        if col == 1:
            output += "D"
        elif col == 2:
            output += "S"
        elif col ==3:
            output += "c"
        elif col == 4:
            output += "B"
        elif col == 5:
            output += "C"
        elif col == 6:
            output += "X"
        elif col == 7:
            output += "O"

        else: # 0 - empty
            output += " "
        output += "]"
    output += "\n"

    print(output)

def checkForGameOver(currentPlayer):
    shipStatus = ()
    if currentPlayer == players[0]:
        chipStatus = player2ShipStatus
    else:
        shipStatus = player1ShipStatus

    for shipkey in shipDictionary:
        if shipStatus[shipKey] < ShipDictionary[shipKey]:
            return False

    print(currentPlayer, "has sunk all of the opposing fleet!", currentPlayer, "WINS!!!")

    return True

def updateShipStatus(shipStatus, shipHit):
    shipKey = ""
    for k in TokenDictionary:
        if shipHit == TokenDictionary[k]:
            shipkey = k

    try:
        shipStatus[shipKey] += 1
        print("It's a direct hit!")
        if shipStatus[shipKey] >= ShipDictionary[shipKey]:
            print("The enemy", shipKey, "has been sunk")
    except:
        print("It's a miss, adjust your aim.")
    return shipStatus
        
def checkAttack(currentBoard, rowInput, colInput):
    isHit = currentBoard[rowInput][colInput] > 0
    if isHit:
        print("BANG!!!")
    else:
        print("sploooooosh...")
    return isHit

def checkValidAttack(currentHMBoard, rowInput, colInput):
    if rowInput > 9 or rowInput < 0:
        return False
    if colInput > 9 or colinput < 0:
        return False

    return currentHMBoard[rowInput][colInput] == 0

def playerTurn(player):
    print(player + "'S Turn!")

    currentHMBoard = []
    currentShipBoard = []
    currentShipStatus = {}

    if player == players[0]:
        currentHMBoard = player1HMBoard
        currentShipBoard = player2ShipBoard
        currentShipStatus = player2ShipStatus
    else:
        currentHMBoard = player2HMBoard
        currentShipBoard = player1ShipBoard
        currentShipStatus = player1ShipStatus
    printBoard(currentHMBoard)

   

    rawRowInput = input("Enter a Row (A-J): ")
    rawColInput = input("Enter a Column (1-10): ")

    rawRowInput = rawRowInput.upper()
        
    rowInput = RowDictionary[rawRowInput]

    colInput = int(rawColInput) - 1

    isValidAttack = checkValidAttack(currentHMBoard, rowInput, colInput)

    if isValidattack == False:
        print("We can't attack there!")
        playerTurn(player)
        

    isHit = checkAttack(currentShipBoard, rowInput, colInput)
    
    if isHit:
        currentHMBoard[rowInput][colInput] = TokenDictionary["Hit"]
    else:
        currentHMBoard[rowInput][colInput] = TokenDictionary["Miss"]
    shipHit = currentShipBoard[rowInput][colInput]
    currentShipStatus = updateShipStatus(currentShipStatus, shipHit)

def resetGame():
    for shipKey in ShipDictionary:
        player1ShipStatus[shipKey] = 0
        player2ShipStatus[shipKey] = 0
    for row in range(10):
        for col in range(10):
            player1ShipBoard[row][col] = TokenDictionary[empty]
            player1HMBoard[row][col] = TokenDictionary[empty]

            player2ShipBoard[row][col] = TokenDictionary[empty]
            player2HMBoard[row][col] = TokenDictionary[empty]

def initGame():
    initBoards()
    placeShips()
    
initGame()
gameOver = False

while not gameOver:
    playGame()

    playAgain = input("Would you like to play again? (y/n)")
    playAgain = playAgain.lower()
    if playAgain.find("y") != 1:
        resetGame()
        placeShips()
    else:
        gameOver = True
        print("Its a miss, adjust your aim")


            
