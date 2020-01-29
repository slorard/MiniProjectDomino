from Player import Player
from Table import table, dominoes_tokens
import os
import random

playerList = []

while 1:
    inputNumPlayer = input('How many wants to play? ')
    try:
        inputNumPlayer = int(inputNumPlayer)
        if int(inputNumPlayer) >= 1 and int(inputNumPlayer) <= 4:
            os.system('clear')
            break
        else:
            print("That number isn't valid, please write one between 2-4")
    except:
        print('Write a real number')



def createPlayer():
    for i in range (int(inputNumPlayer)): #Create the players in a list
        playerList.append(Player(input("Player {}: ".format(i + 1))))
        playerList[i].TakeHand(dominoes_tokens)

listSumTokenPlayer = []
listMaxAllPlayersToken = []
maxToken = []
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
    join = " ".join(table.tableDomino).replace("-", "+").replace(" ", "+")
    totalPoint = (abs(int(eval(join))))
    if dominoes_tokens != []:
        totalPoint += abs(int(eval(" ".join(dominoes_tokens).replace("-","+").replace(" ", "+"))))
    return int(168 - totalPoint)

def block():
        countTokenDoesntGo = 0
        lenHands = 0
        table.showDominos()
        if table.tableDomino != []:
            for player in playerList:
                lenHands += len(player.hand)
                for i in range(len(player.hand)):
                    if player.hand[i][0] != table.join[0] and player.hand[i][0] != table.join[-1] and player.hand[i][2] != table.join[0] and player.hand[i][2] != table.join[-1]:
                        countTokenDoesntGo += 1
            if countTokenDoesntGo == lenHands:
                return True

def win(player):
    if player.hand == [] or block():
        os.system('clear')
        player.points += countPoints()
        print(f"{player.name} has won with {countPoints()} points, now has {player.points} points.")
        for tokenTable in table.tableDomino:
            dominoes_tokens.append(tokenTable)
        for playerHands in playerList:
            for i in range(len(playerHands.hand)):
                if playerHands.hand != []:
                    dominoes_tokens.append(playerHands.hand[i])
            playerHands.hand = []
            random.shuffle(dominoes_tokens)
            playerHands.TakeHand(dominoes_tokens)
            table.join = None
            table.tableDomino = []

def start():
    turns = turn()
    while playerList[turns].points <= 200:
        while True:
            if playerList[turns-1].hand == [] or block():
                win(playerList[turns-1])
                turns -= 1
            win(playerList[turns-1])
            playerList[turns].show_hand()
            playerList[turns].drop_tokens()
            if turns+1 < int(inputNumPlayer):
                turns += 1
            else:
                turns = 0

createPlayer()
playerTurnFirst()
start()
