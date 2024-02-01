# Graysen Schwaller             11/29/2023
# Assignment 6
# The popular Candy Land Game but copyright complacent (lame)| Randomly draw a card to move ahead to the next corresponding spot
import os
import random
from colorama import Fore, Back, Style
def pause():
    printRainbow("Press Enter to Continue: ")
    input()
def printTitleMaterial():
    """Prints the title material for the game, including the student's name, class, and section number.
    """
    printRainbow("Candy Realm!")
    print()
    printRainbow("By: Graysen Schwaller")
    printRainbow("[COM S 127 J]")
    print()
def printRainbow(text):
    backList = [Back.RED,Back.YELLOW,Back.GREEN,Back.CYAN,Back.BLUE,Back.MAGENTA]
    print(Fore.WHITE)
    for i in range(len(text)):
        print(backList[(i)%len(backList)],text[i],end=" ")
    print(Style.RESET_ALL)
def initBoard():
    pepperMintValley, gumdropDitch, truffleTown, lollipopWoods, licoriceCastle, END = "PV", "GD","TT","LW","LC","FN"
    R,P,Y,B,O,G = "Red", "Purple","Yellow", "Blue" ,"Cyan","Green"
    SPECIAL,SPECIAL2,SPECIAL3,SPECIAL4,SPECIAL5,FINISH = pepperMintValley,gumdropDitch,truffleTown,lollipopWoods, licoriceCastle, END
    boardNorm = [R,P,Y,B,O,G,R,P,Y,B,O,G,R,P,Y,B,O,G,R,P,SPECIAL,Y,B,O,G,R,P,Y,B,O,G,R,SPECIAL2,P,Y,B,O,G,R,P,Y,B,O,SPECIAL3,R,P,Y,B,O,G,R,SPECIAL4,P,Y,B,O,G,R,P,Y,B,O,G,R,P,Y,SPECIAL5,B,O,G,R,P,Y,B,O,G,R,P,Y,B,O,G,FINISH]
    return boardNorm
def printBoard(board,deck,playerPos1,playerPos2,playerPos3,playerPos4):
    spaceToColor = {"Red":Back.RED, "Purple":Back.MAGENTA,"Yellow":Back.YELLOW,"Blue":Back.BLUE,"Cyan":Back.CYAN,"Green":Back.GREEN,"PV":Back.WHITE,"GD":Back.WHITE,"TT":Back.WHITE,"LW":Back.WHITE,"LC":Back.WHITE,"FN":Back.WHITE}
    player1Piece = {}
    player1Piece[playerPos1] = "1"
    player2Piece = {20:"P",32:"G",43:"T",51:"L",66:"L",82:"F"}
    player2Piece[playerPos2] = "2"
    player3Piece = {20:"V",32:"D",43:"T",51:"W",66:"C",82:"N"}
    player3Piece[playerPos3] = "3"
    player4Piece = {}
    player4Piece[playerPos4] = "4"
    roadLength = 8
    for i in range(len(board)):
        print(spaceToColor[board[i]]+player1Piece.get(i," ")+player2Piece.get(i," ")+player3Piece.get(i," ")+player4Piece.get(i," ")+Style.RESET_ALL, end=" ")
        if((i+1)%roadLength ==0):
            print()
    print()
    print("Cards in deck: [",end="")
    for i in range(len(deck)):
        print(spaceToColor[deck[i]]+" "+ deck[i]+" "+Style.RESET_ALL, end=" ")
    print("]")
    pass
def initDeck():
    return ["Red", "Purple","Yellow", "Blue" ,"Cyan","Green","PV", "GD","TT","LW","LC"]
def drawFromDeck(deck):
    drawnCard = random.choices(deck,weights=(15,15,15,15,15,15,1,1,1,1,1))
    return drawnCard[0]
def menu():
    choice = input("[p]lay, [r]ules, [q]uit: ")
    if(choice == "q"):
        quit()
    elif(choice == "p"):
        pass
    elif(choice == "r"):
        rules()
        pause()
        menu()
    else:
        menu()
        pass
def rules():
    printRainbow("WELCOME TO THE RULES PAGE!")
    print("The rules are simple, draw a card, and be moved to the closest space of the same color (forwards prioritized)")
    print("There are special locations with respective cards that have a far lower chance of being drawn, and when drawn, will instantly move you towards their respective space")
    print("There is no skill in this game, the winner is whoever is lucky enough to get to the FN spot first!")
    print("Percentages - [Basic Colors]: 15%, [Peppermint Valley, Gumdrop Ditch, Truffle Town, Lollipop Woods & Licorice Castle]: 1%")
    printRainbow("GOOD LUCK!")
def movePlayer(board, turn, playerPos, card):
    if(card == "PV"):
        spaceMoved = 20-playerPos
    elif(card == "GD"):
        spaceMoved = 32-playerPos
    elif(card == "TT"):
        spaceMoved = 43-playerPos
    elif(card == "LW"):
        spaceMoved = 51-playerPos
    elif(card == "LC"):
        spaceMoved = 66-playerPos
    else:
        spaceMoved = findNextSpace(board,playerPos,card) - playerPos
    return spaceMoved
def findNextSpace(board,playerPos,card):
    for i in range(playerPos+1, len(board)):
        if board[i] == card:
            return i
    return 82
def takeTurn(board,deck,p1,p2,p3,p4,playerTurn):
    printBoard(board,deck,p1,p2,p3,p4)
    input("Player {}, please draw a card".format(playerTurn))
    os.system("cls")
    card = drawFromDeck(deck)
    print("Player {} has drawn the {} card!".format(playerTurn,card))
    whoMove = {1:p1,2:p2,3:p3,4:p4}
    spotsMoved = movePlayer(board, playerTurn,whoMove[playerTurn] ,card)
    print("Player {} has moved {} spots forward!".format(playerTurn,spotsMoved))
    if playerTurn == 1:
        p1 += spotsMoved
    elif playerTurn == 2:
        p2 +=spotsMoved
    elif playerTurn == 3:
        p3 +=spotsMoved
    elif playerTurn == 4:
        p4 +=spotsMoved
    gameWon = checkWin(board,p1,p2,p3,p4)
    if not gameWon:
        playerTurn = nextTurn(playerTurn)
    return p1,p2,p3,p4,playerTurn,gameWon
def checkWin(board,p1,p2,p3,p4):
    winNum = len(board)-1
    win = p1 == winNum or p2 == winNum or p3 == winNum or p4 == winNum
    return win
def nextTurn(playerTurn):
    if(playerTurn ==4):
        playerTurn = 1
    else:
        playerTurn += 1
    return playerTurn
def main():
    """This function is where all the fun happens!
    """
    printTitleMaterial()
    menu()
    board = initBoard()
    deck = initDeck()
    playerPos1,playerPos2,playerPos3,playerPos4 = 0,0,0,0
    turn = 1
    gameWon = False
    while not gameWon:
        playerPos1,playerPos2,playerPos3,playerPos4, turn,gameWon = takeTurn(board,deck,playerPos1,playerPos2,playerPos3,playerPos4,turn)
    printBoard(board,deck,playerPos1,playerPos2,playerPos3,playerPos4)
    printRainbow("player {} WON!".format(turn))
if __name__ == "__main__":
    main()