from Player import Player
from Table import Table, dominoesTokens
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

listSumTokenPlayer = []
listMaxAllPlayersToken = []
maxToken = []

while 1:
    inputNumPlayer = input('How many wants to play? ')
    try:
        inputNumPlayer = int(inputNumPlayer)
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
    numTokenPlayer = 7
    for i in range(int(inputNumPlayer)):#range each player
        listSumTokenPlayer = []
        for playerToken in range(numTokenPlayer):#range each player hand token
            listSumTokenPlayer.append(eval("".join(playerList[i].hand[playerToken]).replace("-","+")))
        listMaxAllPlayersToken.append(playerList[i].hand[listSumTokenPlayer.index(max(listSumTokenPlayer))])
    for compareMaxTokenAllPlayer in listMaxAllPlayersToken:
        maxToken.append(eval("".join(compareMaxTokenAllPlayer).replace("-","+")))

def turn():
    turns = maxToken.index(max(maxToken))
    return turns

def countPoints():
    join = " ".join(Table.tableDomino).replace("-", "+").replace(" ", "+")
    totalPoint = (abs(int(eval(join))))
    if dominoesTokens != []:
        totalPoint += abs(int(eval(" ".join(dominoesTokens).replace("-","+").replace(" ", "+"))))
    return int(168 - totalPoint)

def block():
        countTokenDoesntGo = 0
        lenHands = 0
        Table.showDominos()
        if Table.tableDomino != [] and dominoesTokens == []:
            for player in playerList:
                lenHands += len(player.hand)
                for i in range(len(player.hand)):
                    if player.hand[i][0] != Table.join[0] and player.hand[i][0] != Table.join[-1] and player.hand[i][2] != Table.join[0] and player.hand[i][2] != Table.join[-1]:
                        countTokenDoesntGo += 1
            if countTokenDoesntGo == lenHands:
                return True

def win(player):
    if player.hand == [] or block():
        os.system('clear')
        if Table.tableDomino != []:
            player.points += countPoints()

        if Table.tableDomino != [] and block():
            print(f"{player.name} has block with {countPoints()} points, now has {player.points} points.")
        elif Table.tableDomino != [] and player.hand == []:
            print(f"{player.name} has won with {countPoints()} points, now has {player.points} points.")

        for tokenTable in Table.tableDomino:
            dominoesTokens.append(tokenTable)
        for playerHands in playerList:
            for i in range(len(playerHands.hand)):
                if playerHands.hand != []:
                    dominoesTokens.append(playerHands.hand[i])
            playerHands.hand = []
            random.shuffle(dominoesTokens)
            playerHands.TakeHand(dominoesTokens)
            Table.join = None
            Table.tableDomino = []

def start():
    turns = turn()
    while True:
        if playerList[turns-1].hand == [] or block() and dominoesTokens != []:
            win(playerList[turns-1])
            turns -= 1
            while True:
                playAgain = input("Do you want to keep playing?, Y/N ")
                if playAgain.upper() == "Y":
                    turns -= 1
                    start()
                elif playAgain.upper() == "N":
                    print('Thanks for play! :D')
                    time.sleep(1.5)
                    os._exit(1)
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
        if Table.tableDomino == []:
            os.system("clear")
            playerList[turns].showHand()
            playerList[turns].dropTokens()
            playsound('./music/golpe.mp3')
        else:
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
playerTurnFirst()

thread1 = threading.Thread(target= start)
thread2 = threading.Thread(target= music)

thread1.start()
thread2.start()
