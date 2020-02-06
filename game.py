from Player import Player
from Table import Table, dominoesTokens, generateTokens
import os
import random
import time
from playsound import playsound
import threading

print("╔══════════════════════════════════════════════════════════╗")
print("║                                                          ║")
print("║                   𝓦 𝓮𝓵𝓬𝓸𝓶 𝓮 𝓽𝓸 𝓭𝓸𝓶𝓲𝓷𝓸                    ║")
print("║         𝓒𝓲𝓷𝓬𝓲𝓷𝓷 𝓪𝓽𝓾𝓼 𝓘𝓷𝓼𝓽𝓲𝓽𝓾𝓽𝓮 𝓸𝓯 𝓒𝓻𝓪𝓯𝓽𝓼𝓶 𝓪𝓷𝓼𝓴𝓲𝓹         ║")
print("║                                                          ║")
print("╚══════════════════════════════════════════════════════════╝\n")
time.sleep(1)
print("◤                                                        ◥\n")
print("                          𝘾𝙧𝙚𝙖𝙩𝙚 𝙗𝙮                          ")
print("               𝘚𝘵𝘢𝘳𝘭𝘪𝘯𝘨 𝘓𝘰𝘳𝘢 𝘢𝘯𝘥 𝘙 𝘪𝘷𝘪𝘦𝘳 𝘎𝘳𝘶𝘭𝘭𝘰𝘯                 \n")
print("◣                                                        ◢")

playerList = []

while True:
    inputNumPlayer = input('How many wants to play? ')
    try:
        if int(inputNumPlayer) > 1 and int(inputNumPlayer) <= 4:
            os.system('clear')
            break
        else:
            print("That number isn't valid, please write one between 2-4")
    except:
        print('Write a real number')

def createPlayer():
    for i in range (int(inputNumPlayer)): #Create the players in a list
        playerList.append(Player(input("Write name of player {}: ".format(i + 1))))
        playerList[i].TakeHand(dominoesTokens)
    playsound('./music/baraje2.mp3')

def playerTurnFirst():
    playerTurn = 0
    maxToken = 0
    numTokenPlayer = 7
    for player in range(int(inputNumPlayer)):#range each player
        for i in range(numTokenPlayer):#range each player hand token
            test = eval(playerList[player].hand[i-1].replace("-","+"))
            if test > maxToken:
                playerTurn = player
                maxToken = test
    return playerTurn

def countPoints():
    join = " ".join(Table.tableDomino).replace("-", "+").replace(" ", "+")
    totalPoint = (abs(int(eval(join))))
    if dominoesTokens != []:
        totalPoint += abs(int(eval(" ".join(dominoesTokens).replace("-","+").replace(" ", "+"))))
    return int(168 - totalPoint)

def block():
        countTokenDoesntGo = 0
        lenHands = 0
        tokensGoOfDominoesToken = 0
        Table.showDominos()

        if Table.tableDomino != []:
            for tokens in dominoesTokens:
                if Table.join[0] != tokens[0] and Table.join[0] != tokens[-1] and Table.join[-1] != tokens[0] and Table.join[-1] != tokens[-1]:
                    tokensGoOfDominoesToken += 1

            if Table.tableDomino != [] and tokensGoOfDominoesToken == len(dominoesTokens):
                for player in playerList:
                    lenHands += len(player.hand)
                    for i in range(len(player.hand)):
                        if player.hand[i][0] != Table.join[0] and player.hand[i][0] != Table.join[-1] and player.hand[i][2] != Table.join[0] and player.hand[i][2] != Table.join[-1]:
                            countTokenDoesntGo += 1
                if countTokenDoesntGo == lenHands:
                    return True

def againPlay(player):
    os.system('clear')
    if Table.tableDomino != []:
        player.points += countPoints()

    if Table.tableDomino != [] and block():
        print(f"{player.name} has block with {countPoints()} points, now has {player.points} points.")
    elif Table.tableDomino != [] and player.hand == []:
        print(f"{player.name} has won with {countPoints()} points, now has {player.points} points.")

    Table.join = None
    Table.tableDomino = []

    generateTokens()
    random.shuffle(dominoesTokens)

    for player in playerList:
        player.hand = []
        player.TakeHand(dominoesTokens)

def askAgainPlay(turns):
    while True:
        playAgain = input("Do you want to keep playing?, Y/N ")
        if playAgain.upper() == "Y":
            turns -= 1
            start()
        elif playAgain.upper() == "N":
            print('Thanks for play! :D')
            time.sleep(1.5)
            os._exit(1)

def checkWin(turns):
    if int(playerList[turns].points) >= 200:
            print(f"{playerList[turns].name} has won with {playerList[turns].points} points")
            while True:
                playAgainLoop = input("Do you want to keep playing?, Y/N ")
                if playAgainLoop.upper() == "Y":
                    createPlayer()
                    playerTurnFirst()
                    start()
                elif playAgainLoop.upper() == "N":
                    print("Thanks for play! :D")
                    time.sleep(1.5)
                    os._exit(1)


def start():
    turns = playerTurnFirst()
    while True:
        if playerList[turns-1].hand == [] or block():
            againPlay(playerList[turns-1])
            turns -= 2
            askAgainPlay(turns)

        checkWin(turns)

        playerList[turns].showHand()
        playerList[turns].dropTokens()
        playsound('./music/golpe.mp3')

        if turns+1 < int(inputNumPlayer):
            turns += 1
        else:
            turns = 0

def music():
    playsound('./music/Bachata.mp3')

createPlayer()

thread1 = threading.Thread(target= start)
thread2 = threading.Thread(target= music)

thread1.start()
thread2.start()
