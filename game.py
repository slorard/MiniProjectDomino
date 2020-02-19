from Player import Player
from Table import Table, dominoesTokens, generateTokens
from playsound import playsound
import os, random, time, threading

playerList = []

while True:
    inputNumPlayer = input('How many wants to play? ')
    try:
        if int(inputNumPlayer) > 1 and int(inputNumPlayer) <= 4:
            os.system('clear')
            break
        else:
            os.system("clear")
            print("That number isn't valid, please write one between 2-4")
    except:
        os.system("clear")
        print('Write a real number')

def createPlayer():
    for i in range(int(inputNumPlayer)): #Create the players in a list
        playerList.append(Player(input("Write name of player {}: ".format(i + 1))))
        playerList[i].TakeHand(dominoesTokens)
    os.system("clear")
    print("Mixing...")
    playsound('./music/baraje2.mp3')
    os.system("clear")

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
    join = " ".join(Table.tableDomino).replace("-", "+").replace(" ", "+")#sum the all points the table
    tablePoints = abs(int(eval(join)))
    allDominoPoints = 168
    if dominoesTokens != []:
        boxDominoPoint = abs(int(eval(" ".join(dominoesTokens).replace("-","+").replace(" ", "+"))))
        tablePoints += boxDominoPoint
    return abs(int(allDominoPoints - tablePoints))

def block():
        countTokenDoesntGo = 0
        lenHands = 0
        tokensGoOfDominoesToken = 0
        Table.showDominos()

        #count the tokens inside the domino box you can't play
        if Table.tableDomino != []:
            if dominoesTokens != []:
                for tokens in dominoesTokens:
                    if Table.join[0] != tokens[0] and Table.join[0] != tokens[-1] and Table.join[-1] != tokens[0] and Table.join[-1] != tokens[-1]:
                        tokensGoOfDominoesToken += 1
                    else:
                        break
            #count the tokens the players they can't play
            if tokensGoOfDominoesToken == len(dominoesTokens) or dominoesTokens == []:
                for player in playerList:
                    lenHands += len(player.hand)
                    for i in range(len(player.hand)):
                        if player.hand[i][0] != Table.join[0] and player.hand[i][0] != Table.join[-1] and player.hand[i][2] != Table.join[0] and player.hand[i][2] != Table.join[-1]:
                            countTokenDoesntGo += 1
                        else:
                            break
                #compare if the all tokens the players can't play
                if countTokenDoesntGo == lenHands:
                    return True

def askAgainPlay(player):
    while True:
        playAgain = input("Do you want to keep playing?, Y/N ")
        if playAgain.upper() == "Y":
            if player.points >= 200:
                os.system("python -B game.py") or os.system("python3 game.py")
            else:
                os.system("clear")
                break
        elif playAgain.upper() == "N":
            os.system("clear")
            print('Thanks for play! :D')
            time.sleep(1.5)
            os._exit(1)

def againPlay(player):
    os.system('clear')
    if Table.tableDomino != []:
        player.points += countPoints()
        if block():
            print(f"{player.name} has block with {countPoints()} points, now has {player.points} points.")
        else:
            print(f"{player.name} has won with {countPoints()} points, now has {player.points} points.")

    askAgainPlay(player)

    if dominoesTokens != []:#clear the box domino
        for i in range(len(dominoesTokens)):
            dominoesTokens.pop()

    Table.join = None
    Table.tableDomino = []

    generateTokens()
    random.shuffle(dominoesTokens)

    if player.points < 200:
        for players in playerList:
            players.points = 0
            players.hand = []
            players.TakeHand(dominoesTokens)

def start():
    turns = playerTurnFirst()
    while True:
        if playerList[turns-1].hand == [] or block() or int(playerList[turns-1].points) >= 200:
            againPlay(playerList[turns-1])
            turns -= 1

        playerList[turns].showHand()
        print(len(dominoesTokens))
        playerList[turns].dropTokens()
        playsound('./music/golpe.mp3')

        #change the turns
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
